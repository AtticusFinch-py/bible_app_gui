import sys
import requests
import json

API_KEY = '7caf2d4d258d691616e8e235d931fce7956d149f'
API_URL = 'https://api.esv.org/v3/passage/text/'

# Load the JSON data
with open('cross_references.json', 'r') as f:
    cross_references_data = json.load(f)

def retrieve_verses(search_query):
    headers = {
        'Authorization': 'Token %s' % API_KEY
    }

    params = {
        'q': search_query,
        'include-headings': False,
        'include-footnotes': False,
        'include-verse-numbers': False,
        'include-passage-references': False
    }

    response = requests.get(API_URL, params=params, headers=headers)
    
    try:
        response.raise_for_status()
        data = response.json()
        
        passages = data.get('passages', [])
        print("Passages for the search query: ", passages) # print the passages
        
        if passages:
            # Get cross-references for the searched verse
            cross_references = cross_references_data.get(search_query, [])
            print("Cross references from JSON: ", cross_references) # print the cross_references
            
            cross_references_texts = []
            
            for ref in cross_references:
                params['q'] = ref
                response_ref = requests.get(API_URL, params=params, headers=headers)
                response_ref.raise_for_status()
                data_ref = response_ref.json()
                passages_ref = data_ref.get('passages', [])
                if passages_ref:
                    cross_references_texts.extend([ref + ": " + text for text in passages_ref])
                else:
                    cross_references_texts.append('Text not found for reference: ' + ref)


            return passages, cross_references_texts
        else:
            return ['Verse not found'], []  # Return an empty list for cross-references
    except requests.exceptions.RequestException as e:
        print('Error occurred:', e)
        return ['Error occurred'], []  # Return an empty list for cross-references



