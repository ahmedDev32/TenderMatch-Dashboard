Running Guide
run command on terminal by creating venv --> pip3 install -r requirements.txt
 
confusion :
i do not get what is need of cron job we have to directly parse the csv file so thats i donot implement it but i do it with schedule module

Mini TED Tender Parser

This is a simplified MVP version of a TED-style Tender Parser. It allows users to extract key information from tender descriptions (in TXT or HTML format), match them against internal project references using semantic similarity, and display results interactively via a Streamlit dashboard.

Features

Tender Data Extraction** from TXT or HTML
Similarity Matching** using TF-IDF and Cosine Similarity
Streamlit Dashboard with filters and detailed views
CSV Export of filtered tender matches

