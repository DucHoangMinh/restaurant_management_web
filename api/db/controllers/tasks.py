from db.models.tasks import Tasks
from flask import request, Blueprint
import string
from utils.controllers import token_required

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['POST'])
@token_required
def post_task():
    return Tasks.create_new_task(request)

@tasks_bp.route('/tasks/<email>', methods=['GET'])
@token_required
def get_tasks(email):
    return Tasks.get_all_tasks_by_email(email)