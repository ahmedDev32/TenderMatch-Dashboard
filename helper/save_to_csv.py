import pandas as pd
import os

def createCsv(score):
    score_df = pd.DataFrame(score)
    output_path = "template/parsed_tenders.csv"
    os.makedirs("template", exist_ok=True)

    if os.path.exists(output_path):
        score_df.to_csv(output_path, mode='a', header=False, index=False)
    else:
        score_df.to_csv(output_path, mode='w', header=True, index=False) 
