from fetch_data import fetch_data
from find_citations import find_citations

def main():
    data = fetch_data()
    citations = find_citations(data)
    for citation in citations:
        print(citation)

if __name__ == "__main__":
    main()
