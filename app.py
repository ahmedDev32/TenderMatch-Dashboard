import streamlit as st
import pandas as pd
from helper.Extractor import extract_entities
from helper.consinescore import calculate_cosine_similarity
from helper.save_to_csv import createCsv
import os

st.set_page_config(page_title="Mini TED Tender Parser", layout="wide")
st.sidebar.title('Navigation')
page = st.sidebar.selectbox("Go to", ["Upload & Extract", "Dashboard"])
st.title("Mini TED Tender Parser MVP")


if page == "Upload & Extract":
        # File uploaders
    tender_files = st.file_uploader("Upload Tender Description Files (.txt or .html)", type=["txt", "html"], accept_multiple_files=True)
    reference_file = st.file_uploader("Upload Internal Reference Excel File", type=["xlsx"])

    if tender_files and reference_file:
        st.success("Files uploaded successfully!")

        try:
            xlsx_df = pd.read_excel(reference_file)
            st.write("Reference Data Preview:")
            st.dataframe(xlsx_df)

            if st.button('Process Tenders'):
                st.info("Extracting and matching tenders...")

                for tender in tender_files:
                    text = tender.read().decode("utf-8")  
                    data = extract_entities(text)
                    score = calculate_cosine_similarity(data, xlsx_df)
                    st.success("Process Completed...")
                    createCsv(score)
                    st.write('Scores Saved Into CSV File')
                    

        except Exception as e:
            st.error(f"Error reading the Excel file: {e}")

    else:
        st.warning("Please upload both tender text files and the Excel reference file to proceed.")
else:
    st.write("This is the dashboard page. You can visualize the data here.")
    csv_file = "template/parsed_tenders.csv"
     
    if not os.path.exists(csv_file):
        st.warning("No data available. Please upload and process tenders first.")
    else:
        df = pd.read_csv(csv_file)

        # filter boxes
        location = st.sidebar.multiselect("Select Location", df['Location'].unique())
        min_budget = st.sidebar.number_input("Min Budget", value=int(df["Budget"].min()), step=10000)
        max_budget = st.sidebar.number_input("Max Budget", value=int(df["Budget"].max()), step=10000)

        

        # filter by balance
        filter_df = df[
            (df['Budget'] >= min_budget) &
            (df['Budget'] <= max_budget) 
        ]

        if location:
            filter_df = filter_df[filter_df['Location'].isin(location)]
        st.subheader(f"📄 Showing {len(filter_df)} Tenders")
        st.dataframe(filter_df)   
        st.download_button("📥 Export Filtered Tenders to CSV", filter_df.to_csv(index=False), "filtered_tenders.csv", "text/csv") 
         
      
