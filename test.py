import pandas as pd

# Data as a dictionary
data = {
    'Location': ['Karachi', 'Lahore', 'Karachi', 'Islamabad', 'Karachi'],
    'Budget': [1900000, 2500000, 3000000, 2000000, 1800000],
    'Project Type': ['Library', 'School', 'Hospital', 'Library', 'Library'],
    'Phases': ['Planning, Construction', 'Planning, Construction', 'Design, Construction', 'Planning, Construction', 'Planning, Design'],
    'Certifications': ['ISO 9001', 'ISO 14001', 'ISO 45001', 'ISO 9001', 'ISO 9001']
}

# Creating a pandas DataFrame from the dictionary
df = pd.DataFrame(data)

# Saving the DataFrame to an Excel file
df.to_excel('references.xlsx', index=False)

print("Excel file created successfully!")
