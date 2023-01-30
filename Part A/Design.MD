# Distributed Logging Queue
# Design Choices Documentation 

## Part A
### Implementation
Our design for the Distributed Logging Queue (aka Connectify) includes two packages:  multiple lower level queues which are maintained for every topic and which stores all the data corresponding to the topic, namely the messages which are stored as a list and a self lock for synchronization; and a top level package named Distributed Queue which helps us interact with the lower level topic queues and also stores the user data such as the consumer and producer IDs corresponding to every topic as a dictionary mapped from topic names to the IDs which are in a set. The distributed queue package is an umbrella module which helps us interact with the system while the Topic Queues store the topic data which is accessed via the Distributed Queue package. A topic dictionary is maintained with each topic name mapped to their self locks. We have also created 3 locks for the Distributed queue: one lock for the consumer ID dictionary access, another for the producer ID dictionary access and a third lock for the topic dictionary access. The API wrapper used to interact with the endpoints was implemented using Flask. Postman was integrated into the Flask interface to send and recieve prompts in the JSON format.

### Challenges
Our initial design was centered around maintaining Queues for every topic, but this method had a lot of shortcomings ( for eg.: the popping of messages from any topic queue would make it inaccessible for every other consumer, and this would have created an extra burden of maintaining a seperate queue for every consumer ). Finally, we decided upon maintaining a list of strings for the topic messages instead of a queue and maintaining an offset for every consumer which would inform us the next message that the specific consumer has to read and also if the consumer has reached the end of the message queue. 

Another challenge in the implementation was ensuring concurrency, which was done using locks; but we also had to optimize the locking process to optimize the running time of various retrieval and add methods, and hence we used multiple locks for different data structures, to increase the granularity of the program. With a large number of locks each independently locking small amounts of data, the lock contention is reduced, which decreases the waiting time of the program compared to the case where a smaller number of locks is used to protect larger amounts of data, because this increases the likelihood of the lock stopping an unrelated process from running concurrently.   

The generation of unique and random consumer and producer IDs across concurrently executing threads was also a difficulty that we came across, but it was solved by the usage of the inbuilt module called uuid (universally unique identifier), which can generate random 128-bit unique IDs which consist of hexadecimal digits. 

### Hyperparameters
Some of the hyperparameters that we assumed during the implementation included the number of servers running the script, the maximum number of logs that can be inserted per second, and the maximum number of logs that can be stored in the database. Additionally, We also needed to consider the maximum size of a log and the maximum number of columns required in the database table to store all the required information.

### Testing 
To test the implementation, we conducted a series of functional and performance tests. 
The functioncal tests included:
- Checking that the queue is able to handle multiple log messages at the same time.
- Verifying that the queue is able to handle different types of log messages (e.g. info, warning, error) correctly.
- Ensuring that the queue is able to handle high concurrency without data corruption or race conditions.

The performance tests included:
- Measuring the time it takes for log messages to be added and processed from the queue under different concurrency levels.
- Testing the queue's behavior when it is under heavy load.


## Part B
Adding Persistence

## For each topic 

### Topic_Names
    One Field -> topic_name {Supports CreateTopic, ListTopic}
### TopicMessages
	Three fields -> message_id, topic_name, producer_id, message {supports enqueue, dequeue, size}

### TopicOffsets
	Three fields -> consumer_id, topic_name, offset {supports RegisterConsumer, used in deqeue, size}

### TopicProducer
	Two fields -> topic_name, producer_id {used for checking if producer exists for given topic}
