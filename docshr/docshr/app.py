from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://localhost:5432/flask_docshr'
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    """Print 'Hello, world!' as the respjytonse body."""
    return 'Hello, ASFDSworld!'


from .app import db
from datetime import datetime

class Task(db.Model):
    """Tasks for the To Do list."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, nullable=False)
    note = db.Column(db.Unicode)
    creation_date = db.Column(db.DateTime, nullable=False)
    due_date = db.Column(db.DateTime)
    completed = db.Column(db.Boolean, default=False)

    def __init__(self, *args, **kwargs):
        """On construction, set date of creation."""
        super().__init__(*args, **kwargs)
        self.creation_date = datetime.now()
