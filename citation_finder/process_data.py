def find_citations(response, sources):
    citations = []
    for source in sources:
        if source['context'] in response:
            citation = {
                'id': source['id'],
                'link': source.get('link', '')
            }
            citations.append(citation)
    return citations

def process_data(data):
    results = []
    for item in data:
        response = item.get('response', '')
        sources = item.get('sources', [])
        citations = find_citations(response, sources)
        results.append(citations)
    return results
