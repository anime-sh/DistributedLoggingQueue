import requests

# TODO: When broker is down: block hoke baith jao
class MyConsumer:
	def __init__(self, topics, broker):
		self.topics = topics
		self.url = broker
		self.topics_to_consumer_ids = dict{}

		for topic_name in topics:
			self.subscribe_to_topic(topic_name)
	
	def get_next(self, topic_name):
		
		if topic_name not in self.topics_to_consumer_ids:
			print(f"Please register to {topic_name}")
			return

		send_url = self.base_url + "/consumer/dequeue"
		data = {
			"topic" : topic_name,
			"consumer_id": self.topics_to_consumer_ids[topic_name],
		}
		try:
			r = requests.post(send_url, json = data)
			r.raise_for_status()
		except requests.exceptions.HTTPError as errh:
			print ("Http Error:",errh)
		except requests.exceptions.ConnectionError as errc:
			print ("Error Connecting:",errc)
		
		response = r.json()

		if response["status"] == "Success":
			print("Sent successfully")
		else:
			print(f"Failed, {response['message']}")
		
		return response
		
if __name__ == "__main__":
	pass