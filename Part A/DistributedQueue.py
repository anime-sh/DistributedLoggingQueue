# TODO: Implement the Distributed Queue using the Individual Topic Queues

import threading
import uuid
from typing import Dict, List, Tuple, Set
from concurrent.futures import ThreadPoolExecutor

from TopicQueue import TopicQueue

# TODO: define enum for success and failure codes   

class LoggingQueue:
    def _init_(self):
        self.topics: Dict[str, TopicQueue] = {}  # stores the available topics and their lock
        self.consumers_for_topic: Dict[str, Set[int] ] = {}  # stores the consumer_ids for a topic
        self.producers_for_topic: Dict[str, Set[int]] = {}  # stores the producer_ids for a topic
        # todo: check producer registers for exactly one topic
        self.topics_dict_lock = threading.Lock()  # lock for topics dictionary
        self.consumer_lock = threading.Lock()  # lock for consumers dictionary
        self.producer_lock = threading.Lock()  # lock for producers dictionary
        
    def create_topic(self, topic_name: str) -> None:
        with self.topics_dict_lock:
            if topic_name not in self.topics:
                self.topics[topic_name] = TopicQueue()  # create the topic queue
                with self.consumer_lock:
                    self.consumers_for_topic[topic_name] = set()  # create the set of consumer_ids for the topic
                with self.producer_lock:
                    self.producers_for_topic[topic_name] = set()  # create the set of producer_ids for the topic
                print(f"Topic {topic_name} created.")
                return 1 
            else:
                print(f"Topic {topic_name} already exists.")
                return -1

    def list_topics(self) -> List[str]:
        with self.topics_dict_lock:
            return list(self.topics.keys())
        

    def register_consumer(self, topic_name: str) -> int:
        with self.create_topic:
            if topic_name not in self.topics:
                print(f"Topic {topic_name} does not exist.")
                return -1
        consumer_id = uuid.uuid4()
        with self.consumer_lock:   
            self.consumers_for_topic[topic_name].add(consumer_id)
            print(f"Consumer {consumer_id} registered for topic {topic_name}.")
            return consumer_id

    def register_producer(self, topic_name: str) -> int:        
        with self.create_topic:
            if topic_name not in self.topics:
                self.create_topic(topic_name)

        producer_id = uuid.uuid4()
        
        with self.producer_lock:
            self.producers_for_topic[topic_name].add(producer_id)
            print(f"Producer {producer_id} registered for topic {topic_name}.")
            return producer_id

    def enqueue(self, topic_name:str, producer_id: int, message: str) -> None:
        
        with self.topics_dict_lock:
            if not topic_name in self.topics:
                print(f"Topic {topic_name} does not exist.")
                return -1
    
        with self.producer_lock:
            if not producer_id in self.producers_for_topic[topic_name]:
                print(f"Producer {producer_id} is not registered for topic {topic_name}.")
                return -1
        
        with self.topics_dict_lock: # TODO: is this even necessary? given we lock inside
            self.topics[topic_name].add_log(message,message_metadata=f"{producer_id}")
            print(f"Producer {producer_id} enqueued message '{message}' to topic {topic_name}.")
            return 1

    def dequeue(self, consumer_id: str, topic_name: str) -> str:
        with self.topics_dict_lock:
            if not topic_name in self.topics:
                print(f"Topic {topic_name} does not exist.")
                return -1
            
        with self.consumer_lock:
            if consumer_id not in self.consumers_for_topic[topic_name]:
                print(f"Consumer {consumer_id} is not registered.")
                return -1
        
        with self.topics_dict_lock:
            message, metadata = self.topics[topic_name].retrieve_log()
            print(f"Consumer {consumer_id} dequeued message '{message}' ({metadata}) from topic {topic_name}.")
            return message

    def size(self, topic_name: str, consumer_id: int) -> int:
        with self.topics_dict_lock:
            if topic_name not in self.topics:
                print(f"Topic {topic_name} does not exist.")
                return -1
            
        with self.consumer_lock:
            if consumer_id not in self.consumers_for_topic[topic_name]:
                print(f"Consumer {consumer_id} is not registered.")
                return -1
        with self.topics_dict_lock:
            return self.topics[topic_name].size()
        