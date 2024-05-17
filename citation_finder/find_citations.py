def find_citations(data):
    citations = []
    for item in data:
        response_text = item['response']
        sources = item['sources']
        response_citations = []

        for source in sources:
            if source['context'] in response_text:
                citation = {
                    'id': source['id'],
                    'link': source.get('link', '')
                }
                response_citations.append(citation)

        citations.append({
            'response': response_text,
            'citations': response_citations
        })
    return citations
