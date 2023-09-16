from db.models.tasks import Tasks
from flask import request, Blueprint
import string
from utils.controllers import token_required

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['POST'])
@token_required
def post_task():
    return Tasks.create_new_task(request)

@tasks_bp.route('/tasks/all/<email>', methods=['GET'])
@token_required
def get_tasks(email):
    return Tasks.get_all_tasks_by_email(email)

@tasks_bp.route('/tasks/<id>', methods=['GET'])
@token_required
def get_task_by_id(id):
    return Tasks.get_task_by_id(id)

@tasks_bp.route('/tasks/<id>', methods=['PATCH'])
@token_required
def put_task_by_id(id):
    return Tasks.patch_task_by_id(id, request)

@tasks_bp.route('/tasks/<id>', methods=['DELETE'])
@token_required
def delete_task_by_id(id):
    return Tasks.delete_task_by_id(id)