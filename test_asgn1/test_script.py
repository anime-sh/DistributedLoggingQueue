import requests
import json
HOST = "127.0.0.1"
PORT = 5000

# witout concurrency
base_url = f"http://{HOST}:{PORT}"
response = requests.get(f"{base_url}/topics")
print(json.dumps(response.json(), indent=4))

payload = {"topic_name": "Kagenou"}
response = requests.post(f"{base_url}/topics", json=payload)
print(json.dumps(response.json(), indent=4))

payload = {"topic_name": "Kagenou"}
response = requests.post(f"{base_url}/topics", json=payload)
print(json.dumps(response.json(), indent=4))


payload = {"topic_name": "Minoru"}
response = requests.post(f"{base_url}/topics", json=payload)
print(json.dumps(response.json(), indent=4))


base_url = f"http://{HOST}:{PORT}"
response = requests.get(f"{base_url}/topics")
print(json.dumps(response.json(), indent=4))


payload = {"topic": "Minoru"}
response = requests.post(f"{base_url}/producer/register", json=payload)
print(json.dumps(response.json(), indent=4))
m_producer_id = response.json()['producer_id']


payload = {"topic": "Kagenou"}
response = requests.post(f"{base_url}/producer/register", json=payload)
print(json.dumps(response.json(), indent=4))
k_producer_id = response.json()['producer_id']

payload = {"topic": "Minoru"}
response = requests.post(f"{base_url}/consumer/register", json=payload)
print(json.dumps(response.json(), indent=4))
m_consumer_id = response.json()['consumer_id']

payload = {"topic": "Kagenou"}
response = requests.post(f"{base_url}/consumer/register", json=payload)
print(json.dumps(response.json(), indent=4))
k_consumer_id = response.json()['consumer_id']


payload = {"topic": "Minoru", "consumer_id": m_consumer_id}
response = requests.get(f"{base_url}/size", json=payload)
print(json.dumps(response.json(), indent=4))


payload = {"topic": "Kagenou", "consumer_id": k_consumer_id}
response = requests.get(f"{base_url}/size", json=payload)
print(json.dumps(response.json(), indent=4))

payload = {"topic": "Minoru", "consumer_id": k_consumer_id}
response = requests.get(f"{base_url}/size", json=payload)
print(json.dumps(response.json(), indent=4))


payload = {"topic": "Kagenou", "consumer_id": m_consumer_id}
response = requests.get(f"{base_url}/size", json=payload)
print(json.dumps(response.json(), indent=4))


payload = {"topic": "Kagenou", "consumer_id": k_consumer_id}
response = requests.get(f"{base_url}/consumer/consume", json=payload)
print(json.dumps(response.json(), indent=4))


payload = {"topic": "Minoru", "consumer_id": m_consumer_id}
response = requests.get(f"{base_url}/consumer/consume", json=payload)
print(json.dumps(response.json(), indent=4))


payload = {"topic": "Kagenou", "consumer_id": m_consumer_id}
response = requests.get(f"{base_url}/consumer/consume", json=payload)
print(json.dumps(response.json(), indent=4))


payload = {"topic": "Minoru", "consumer_id": k_consumer_id}
response = requests.get(f"{base_url}/consumer/consume", json=payload)
print(json.dumps(response.json(), indent=4))

payload = {"topic": "Kagenou", "producer_id": k_producer_id, "message": "Big W1"}
response = requests.post(f"{base_url}/producer/produce", json=payload)
print(json.dumps(response.json(), indent=4))


payload = {"topic": "Minoru", "producer_id": m_producer_id, "message": "Big W2"}
response = requests.post(f"{base_url}/producer/produce", json=payload)
print(json.dumps(response.json(), indent=4))

payload = {"topic": "Minoru", "consumer_id": m_consumer_id}
response = requests.get(f"{base_url}/size", json=payload)
print(json.dumps(response.json(), indent=4))


payload = {"topic": "Kagenou", "consumer_id": k_consumer_id}
response = requests.get(f"{base_url}/size", json=payload)
print(json.dumps(response.json(), indent=4))

payload = {"topic": "Kagenou", "consumer_id": k_consumer_id}
response = requests.get(f"{base_url}/consumer/consume", json=payload)
print(json.dumps(response.json(), indent=4))


payload = {"topic": "Minoru", "consumer_id": m_consumer_id}
response = requests.get(f"{base_url}/consumer/consume", json=payload)
print(json.dumps(response.json(), indent=4))


payload = {"topic": "Kagenou", "consumer_id": k_consumer_id}
response = requests.get(f"{base_url}/consumer/consume", json=payload)
print(json.dumps(response.json(), indent=4))


payload = {"topic": "Minoru", "consumer_id": m_consumer_id}
response = requests.get(f"{base_url}/consumer/consume", json=payload)
print(json.dumps(response.json(), indent=4))


payload = {"topic": "Minoru", "consumer_id": m_consumer_id}
response = requests.get(f"{base_url}/size", json=payload)
print(json.dumps(response.json(), indent=4))


payload = {"topic": "Kagenou", "consumer_id": k_consumer_id}
response = requests.get(f"{base_url}/size", json=payload)
print(json.dumps(response.json(), indent=4))
