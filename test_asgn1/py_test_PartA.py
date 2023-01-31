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

    print("Response")
    print(response)
except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)

except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)

print()
print("Testing the endpoint create Topic (topic already exists case)")
url = base_url + "/topics"
data = {
    "topic_name": "tp_1"
}

try:
    print(f"request = {data}")
    r = requests.post(url, json=data)
    r.raise_for_status()
    response = r.json()

    print("Response")
    print(response)
except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)

except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)


print()
print("Testing the endpoint get Topics")
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


print()
print("Testing the endpoint register consumer")
url = base_url + "/consumer/register"
data = {
    "topic": "tp_1"
}

consumer_id = None
try:
    print(f"request = {data}")
    r = requests.post(url, json=data)
    r.raise_for_status()
    response = r.json()
    print("Response")
    consumer_id = response['consumer_id']
    print(response)
except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)

except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)


print()
print("Testing the endpoint register consumer (case with invalid topic name)")
url = base_url + "/consumer/register"
data = {
    "topic": "tp_2"
}

try:
    print(f"request = {data}")
    r = requests.post(url, json=data)
    r.raise_for_status()
    response = r.json()
    print("Response")
    print(response)
except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)

except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)


print()
print("Testing the endpoint register producer")
url = base_url + "/producer/register"
data = {
    "topic": "tp_1"
}
producer_id = None
try:
    print(f"request = {data}")
    r = requests.post(url, json=data)
    r.raise_for_status()
    response = r.json()
    print("Response")
    producer_id = response["producer_id"]
    print(response)
except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)

except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)

print()
print("Testing the endpoint register producer (missing topic name)")
url = base_url + "/producer/register"
data = {
    "topic": "tp_2"
}
try:
    print(f"request = {data}")
    r = requests.post(url, json=data)
    r.raise_for_status()
    response = r.json()
    print("Response")
    print(response)
except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)

except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)

print()
print("calling the endpoint get Topics")
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

print("Note : Topic tp_2 was created while registering the producer.")