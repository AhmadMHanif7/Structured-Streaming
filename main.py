import requests
import json
 

def get_api_data(url: str = 'https://randomuser.me/api/') -> dict:
   
    """
    Pulls data from the Random API URL
    """
    response = requests.get(url)
    data = response.json()
    results = data['results'][0]
 
    return results




def create_final_json() -> dict:
 
    """
    Parses the raw data and pulls in relavent fields only
    """
 
    results = get_api_data()
 
    final_dict= {}
 
    final_dict['full_name'] = f"{results['name']['first']} {results['name']['last']}"
    final_dict['gender']  = results['gender']
    final_dict['street_address'] = f"{results['location']['street']['number']} {results['location']['street']['name']}"
    final_dict['city'] = results['location']['city']
    final_dict['country'] = results['location']['country']
    final_dict['zip_code'] = int(results['location']['postcode'])
    final_dict['latitude'] = float(results['location']['coordinates']['latitude'])
    final_dict['longitude'] = float(results['location']['coordinates']['longitude'])
    final_dict['email_address'] = results['email']
 
    return final_dict
 
new_dict = create_final_json()
 
print(new_dict['full_name'])