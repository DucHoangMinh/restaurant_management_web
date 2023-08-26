from flask import Flask
from flask_cors import CORS
from db.controllers.students import students_bp
app = Flask(__name__)
CORS(app)

app.register_blueprint(students_bp)
@app.route('/', methods=['GET'])
def test():
        return 'mya students'
print('This is a test')

import db.controllers.students
if __name__ == '__main__':
    app.run(host='0.0.0.0')