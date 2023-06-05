from datetime import datetime

def create_models(db):
    class Data_message(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        email = db.Column(db.String(200), nullable=False)
        subject = db.Column(db.String(200), nullable=False)
        message = db.Column(db.String(10000), unique=True, nullable=False)
        created_at = db.Column(db.DateTime, default=datetime.utcnow)

        def __repr__(self):
            return f"<Message(id={self.id}, name='{self.name}', email='{self.email}', subject='{self.subject}')>"
    
    return Data_message
