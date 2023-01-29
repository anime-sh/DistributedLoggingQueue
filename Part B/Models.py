from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TopicName(db.Model):
    __tablename__ = 'TopicName'
    topic_name = db.Column(db.String(), primary_key=True)

    def __init__(self, topic_name):
        self.topic_name = topic_name

    def __repr__(self):
        return f"{self.topic_name}"

    def ListTopics(self):
        return TopicName.query.all()

    def CreateTopic(self, topic_name):
        topic = TopicName(topic_name)
        db.session.add(topic)
        db.session.commit()

    def CheckTopic(self, topic_name):
        topic = TopicName.query.filter_by(topic_name=topic_name).first()
        return True if topic else False


class TopicMessage(db.Model):
    __tablename = 'TopicMessage'
    id = db.Column(db.Integer, primary_key=True)
    topic_name = db.Column(db.String(), db.ForeignKey('TopicName.topic_name'))
    producer_id = db.Column(db.String())
    message = db.Column(db.String())

    def __init__(self, topic_name, producer_id, message):
        self.topic_name = topic_name
        self.producer_id = producer_id
        self.message = message

    def addMessage(self, topic_name, producer_id, message):
        # check if topic exists
        if not TopicName.CheckTopic(topic_name):
            raise Exception("Topic does not exist")

        topic = TopicMessage(topic_name, producer_id, message)
        db.session.add(topic)
        db.session.commit()

    def retrieveMessage(self, topic_name, offset):
        left_messages = self.getSizeforTopic(topic_name, offset)
        if (offset > left_messages):
            raise Exception("Offset is greater than the number of messages")
        data = TopicMessage.query.filter_by(
            topic_name=topic_name).sort_by(id).offset(offset).first()
        return data.message

    def getSizeforTopic(topic_name, offset):
        # offset is 0-indexed
        return TopicMessage.query.filter_by(topic_name=topic_name).count() - offset - 1

    def __repr__(self):
        return f"{self.topic_name} {self.producer_id} {self.message}"

