import requests
print("Testing the endpoint create Topic")
HOST = "127.0.0.1"
PORT = 5000
base_url = f"http://{HOST}:{PORT}"
url = base_url + "/topics"
data = {
    "topic_name": "tp_1"
}

try:
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