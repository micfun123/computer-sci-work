import requests

def fetch_all_wikipedia_titles():
    """
    Fetch all Wikipedia page titles using the `allpages` API action.
    """
    session = requests.Session()
    url = "https://en.wikipedia.org/w/api.php"

    titles = []

    params = {
        "action": "query",
        "format": "json",
        "list": "allpages",
        "aplimit": "max"  # Fetch all titles
    }

    while True:
        response = session.get(url=url, params=params)
        data = response.json()

        titles.extend([page['title'] for page in data['query']['allpages']])

        if 'continue' in data:
            params.update(data['continue'])
        else:
            break

    return titles

def save_titles_to_file(titles, filename="wikipedia_titles.txt"):
    """
    Save the list of Wikipedia titles to a text file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        for title in titles:
            print(title)
            file.write(title + "\n")

if __name__ == "__main__":
    all_titles = fetch_all_wikipedia_titles()
    save_titles_to_file(all_titles)
    print("All Wikipedia titles have been saved to 'wikipedia_titles.txt'.")
