
import queue
import threading

class TopicQueue(object):
	def __init__(self):
		# self.queue = queue.Queue()
		self.messages = []
		self.offsets = dict()
		self.lock = threading.Lock()

		# TODO: Should we limit number of active threads accessing a single topic??
		# self.max_threads = max_threads
		# self.active_threads = 0

	def add_log(self, log_message, message_metadata=""):
		# Acquire the lock to add a log message to the queue
		self.lock.acquire()
		try:
			# self.queue.put((log_message,message_metadata))
			self.messages.append((log_message, message_metadata))
		finally:
			self.lock.release()


	def retrieve_log(self, consumer_id):
		# Acquire the lock to retrieve a log message from the queue
		# if empty the thread will wait UNTIL it has something to return
		self.lock.acquire()
		try:
			if len(self.messages) > self.offsets[consumer_id]:
				# log_message, message_metadata = self.queue.get()
				log_message, message_metadata = self.messages[self.offsets[consumer_id]]
				self.offsets[consumer_id] += 1
			else:
				log_message=""
				message_metadata="No Message"
		finally:
			self.lock.release()
			return log_message, message_metadata

	def size(self, consumer_id):
		with self.lock:
			return len(self.messages) - self.offsets[consumer_id]
			

# Testing :
if __name__=='__main__':
	topic_queue = TopicQueue()
	topic_queue.add_log("This is an error message")
	topic_queue.add_log("This is a warning message")
	topic_queue.add_log("This is an info message")
	print(topic_queue.retrieve_log())
	print(topic_queue.retrieve_log())
	print(topic_queue.retrieve_log())
	print(topic_queue.retrieve_log())
