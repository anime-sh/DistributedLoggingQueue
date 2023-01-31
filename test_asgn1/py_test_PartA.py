import requests
HOST = "127.0.0.1"
PORT = 5000
base_url = f"http://{HOST}:{PORT}"


print("Testing the endpoint create Topic")
url = base_url + "/topics"
data = {
    "topic_name": "tp_1"
}

try:
    print(f"request = {data}")
    r = requests.post(url, json=data)
    r.raise_for_status()
    response = r.json()
    if response["status"] == "Success":
        print("Sent successfully")
    else:
        print("Failed")
    print("Response")
    print(response)
except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)

except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)

print()
print("Testing the endpoint get Topic")
url = base_url + "/topics"


try:
    r = requests.get(url)
    r.raise_for_status()
    response = r.json()
    print("Response")
    print(response)
except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)

except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)