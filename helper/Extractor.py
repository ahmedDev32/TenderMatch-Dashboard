import re
from bs4 import BeautifulSoup as bs

def parse_html(html_content):
    """
    Parse HTML content and extract text.
    """
    soup = bs(html_content, 'html.parser')
    text = soup.get_text(separator="\n")
    return text

def extract_entities(data):
    text = parse_html(data) if data.endswith('.html') else data
    project_name = re.search(r'Project Name: (.+)', text)
    location = re.search(r'Location: (.+)', text)
    budget_300 = re.search(r'- Kostengruppe 300: €?([\d,.]+)', text)
    budget_400 = re.search(r'- Kostengruppe 400: €?([\d,.]+)', text)
    project_type = re.search(r'Project Type: (.+)', text)
    phases = re.search(r'Phases: (.+)', text)
    deadline = re.search(r'Submission Deadline: (.+)', text)

    # Clean and convert budget values
    budget_300_val = int(budget_300.group(1).replace(',', '').replace('.', '')) if budget_300 else 0
    budget_400_val = int(budget_400.group(1).replace(',', '').replace('.', '')) if budget_400 else 0

    return {
        "Project Name": project_name.group(1) if project_name else "",
        "Location": location.group(1) if location else "",
        "Budget": budget_300_val + budget_400_val if budget_300 and budget_400 else None,
        "Project Type": project_type.group(1) if project_type else "",
        "Phases": phases.group(1) if phases else "",
        "Submission Deadline": deadline.group(1) if deadline else ""
    }
