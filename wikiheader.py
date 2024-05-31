import requests

def filter_religious_titles(titles):
    """
    Filter out titles that are related to religion.
    """
    religion_keywords = [
        "religion", "church", "mosque", "temple", "synagogue", "faith", 
        "god", "goddess", "bible", "quran", "torah", "scripture", "prayer", 
        "worship", "christian", "muslim", "hindu", "buddhist", "jewish"
    ]
    
    filtered_titles = [title for title in titles if not any(keyword.lower() in title.lower() for keyword in religion_keywords)]
    return filtered_titles

def create_wikipedia_dict(titles):
    """
    Create a dictionary from a list of Wikipedia titles with 0 as the value for each key.
    """
    wiki_dict = {title: 0 for title in titles}
    return wiki_dict

def fetch_wikipedia_titles(limit=500, max_requests=10):
    """
    Fetch Wikipedia titles using the `allpages` API call with pagination.
    """
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"

    titles = []
    params = {
        "action": "query",
        "format": "json",
        "list": "allpages",
        "aplimit": "max"
    }

    for _ in range(max_requests):
        response = S.get(url=URL, params=params)
        data = response.json()

        titles.extend([page['title'] for page in data['query']['allpages']])

        if 'continue' in data:
            params['apcontinue'] = data['continue']['apcontinue']
        else:
            break

    return titles

# Example usage
titles = fetch_wikipedia_titles(500, max_requests=1000000000000000000)  # Fetch more titles with pagination
filtered_titles = filter_religious_titles(titles)
wiki_dict = create_wikipedia_dict(filtered_titles)

# Print the dictionary
for title, value in wiki_dict.items():
    print(f"{title}: {value}")

# Optionally, save the dictionary to a JSON file
import json
with open('filtered_wikipedia_titles.json', 'w') as json_file:
    json.dump(wiki_dict, json_file)
