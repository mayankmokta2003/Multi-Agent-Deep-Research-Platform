import requests 
import xml.etree.ElementTree as ET

BASE_URL = "https://export.arxiv.org/api/query"

def search_papers(query: str, max_results: int = 5):
    params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": max_results,
    }
    response = requests.get(BASE_URL, params=params, timeout=30)
    response.raise_for_status()
    root = ET.fromstring(response.text)

    namespace = {
        "atom": "http://www.w3.org/2005/Atom"
    }
    papers = []
    for entry in root.findall("atom:entry",namespace):
        title = entry.find("atom:title",namespace).text.strip()
        summary = entry.find("atom:summary",namespace).text.strip()
        link = entry.find("atom:id", namespace).text.strip()
        authors = []
        for author in entry.findall("atom:author",namespace):
            authors.append(author.find("atom:author",namespace).text.strip())
        papers.append({
            "title": title,
            "summary": summary,
            "url": link,
            "authors": authors
        })
    return papers