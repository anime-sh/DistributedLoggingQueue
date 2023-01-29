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
    

