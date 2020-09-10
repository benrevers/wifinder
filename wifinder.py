import sys
import requests

# Define constants
API_KEY = "INSERT_API_KEY_HERE"
GEOCODE_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
GEOLOCATE_BASE_URL ="https://www.googleapis.com/geolocation/v1/geolocate"

# Sanity check
if len(sys.argv) < 3:
    print("At least two mac addresses required for search!")
    sys.exit()

# Grab mac addresses from command line and build json object
macs = dict([("considerIp", "false"), ("wifiAccessPoints", [{"macAddress": str(x)} for x in sys.argv[1:]])])

# Compose a url to query the Google Geolocate API with our mac addresses
url = (f"{GEOLOCATE_BASE_URL}?key={API_KEY}")
response = requests.post(url, json=macs)
data = response.json()

# If we get a success, query the Google Geocode API with latitude and longitude coordinates
if response.status_code == 200:
    lat, lng, accuracy = data['location']['lat'], data['location']['lng'], data['accuracy']
    print(f"Estimated location @ {lat},{lng} with {accuracy} meter accuracy.\n")
    url = (f"{GEOCODE_BASE_URL}?latlng={lat},{lng}&key={API_KEY}")
    data = requests.get(url).json()

    for result in range(len(data['results'])):
        try:
            print(f"{data['results'][result]['geometry']['location_type']}: {data['results'][result]['formatted_address']}")
        except Exception:
            print("Unable to parse result, manually view at following url:\n", url)
            pass
        
else:
    print("Error:", data['error']['code'], data['error']['message'])
    sys.exit()
