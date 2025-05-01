from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_cosine_similarity(tender, refs):
    tender_desc = f"{tender['Location']} {tender['Budget']} {tender['Project Type']} {tender['Phases']}"
    ref_descs = refs.apply(lambda row: f"{row['Location']} {row['Budget']} {row['Project Type']} {row['Phases']}", axis=1)
    
    vectorizer = TfidfVectorizer().fit([tender_desc] + list(ref_descs))
    tender_vec = vectorizer.transform([tender_desc])
    ref_vecs = vectorizer.transform(ref_descs)

    similarities = cosine_similarity(tender_vec, ref_vecs)[0]
    refs["similarity"] = similarities
    return refs.sort_values("similarity", ascending=False).head(3)