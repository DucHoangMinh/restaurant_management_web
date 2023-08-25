from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
import db.controllers.students

@app.route('/', methods=['GET','POST'])
def test():
        return 'students'