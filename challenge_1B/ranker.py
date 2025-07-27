from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def rank_sections(sections, persona, job):
    query = f"{persona}. Task: {job}"
    query_embedding = model.encode(query, convert_to_tensor=True)

    for section in sections:
        section["score"] = util.cos_sim(query_embedding, model.encode(section["text"], convert_to_tensor=True)).item()

    sorted_sections = sorted(sections, key=lambda x: x["score"], reverse=True)

    # Add importance rank
    for i, section in enumerate(sorted_sections[:10]):
        section["importance_rank"] = i + 1

    return [{
        "document": s["document"],
        "page": s["page"],
        "section_title": s["section_title"],
        "importance_rank": s["importance_rank"]
    } for s in sorted_sections[:10]]
