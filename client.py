import requests

# Set the URL of your Flask API endpoint
url = 'http://localhost:5000/recognize'

# Path to the image file you want to send
image_path = 'Data/elcan.jpg.'

# Send the POST request to the Flask API endpoint
with open(image_path, 'rb') as image_file:
    response = requests.post(url, files={'image': image_file})

# Check the response status code
if response.status_code == 200:
    # Get the JSON response
    json_output = response.json()
    print(json_output)
else:
    print('Error:', response.text)
