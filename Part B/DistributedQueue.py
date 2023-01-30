# TODO: Implement the Distributed Queue using the Individual Topic Queues
import Models
import threading
import uuid
from typing import Dict, List, Tuple, Set
from concurrent.futures import ThreadPoolExecutor

from TopicQueue import TopicQueue

# TODO: define enum for success and failure codes   

class LoggingQueue:
    def __init__(self):
        print("Hello")
        self.ProducerDB, self.MessageDB, self.NameDB, self.OffsetsDB = Models.return_objects()
        print("Bye")

    def create_topic(self, topic_name: str) -> None:
        if not self.NameDB.CheckTopic(topic_name=topic_name):
            self.NameDB.CreateTopic(topic_name=topic_name)
            print(f"Topic {topic_name} created.")
            return 1 
        else:
            print(f"Topic {topic_name} already exists.")
            return -1

    def list_topics(self) -> List[str]:
        return list(self.NameDB.ListTopics())

    def register_consumer(self, topic_name: str) -> int:
        # offset --> 0
        if not self.NameDB.CheckTopic(topic_name=topic_name):
            print(f"Topic {topic_name} does not exist.")
            return -1
            
        consumer_id = uuid.uuid4()
        self.OffsetsDB.registerConsumer(consumer_id=consumer_id,topic_name=topic_name)
        print(f"Consumer {consumer_id} registered for topic {topic_name}.")
        return consumer_id

    def register_producer(self, topic_name: str) -> int:        
        # with self.create_topic:
        if not self.NameDB.CheckTopic(topic_name=topic_name):
            self.NameDB.CreateTopic(topic_name=topic_name)

        producer_id = uuid.uuid4()
        self.ProducerDB.registerProducer(producer_id=producer_id,topic_name=topic_name)
        print(f"Producer {producer_id} registered for topic {topic_name}.")
        return producer_id

    def enqueue(self, topic_name:str, producer_id: int, message: str) -> None:
        
        if not self.NameDB.CheckTopic(topic_name=topic_name):
            print(f"Topic {topic_name} does not exist.")
            return -1

        if not self.ProducerDB.checkProducer(producer_id):
            print(f"Producer {producer_id} is not registered for topic {topic_name}.")
            return -2
        
        # self.topics[topic_name].add_log(message,message_metadata=f"{producer_id}")
        self.MessageDB.addMessage(topic_name=topic_name, producer_id=producer_id, message=message)
        print(f"Producer {producer_id} enqueued message '{message}' to topic {topic_name}.")
        return 1

    def dequeue(self, consumer_id: str, topic_name: str) -> str:

        if not self.NameDB.CheckTopic(topic_name=topic_name):
            print(f"Topic {topic_name} does not exist.")
            return -1
            
        if not self.OffsetsDB.checkConsumer(consumer_id):
            print(f"Consumer {consumer_id} is not registered.")
            return -2
        
        offset = self.OffsetsDB.getOffset(consumer_id)
        message = self.MessageDB.retrieveMessage(topic_name=topic_name, offset=offset)
        if message == -1:
            print(f"No message in queue!!!")
            return -3
        else:
            print(f"Consumer {consumer_id} dequeued message '{message}' from topic {topic_name}.")
            return message

    def size(self, topic_name: str, consumer_id: int) -> int:

        if not self.NameDB.CheckTopic(topic_name=topic_name):
            print(f"Topic {topic_name} does not exist.")
            return -1
            
        if not self.OffsetsDB.checkConsumer(consumer_id):
            print(f"Consumer {consumer_id} is not registered.")
            return -2

        offset = self.OffsetsDB.getOffset(consumer_id)
        return self.MessageDB.getSizeforTopic(topic_name=topic_name, offset=offset)
        