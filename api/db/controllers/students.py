from db.models.students import Students
from main import app


@app.route('/students', methods=['GET'])
def get_all_students():
    return Students.get_all_students()
