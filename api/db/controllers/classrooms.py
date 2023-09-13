from db.models.classrooms import Classroom
from flask import request, Blueprint
import random
import string
from utils.controllers import token_required

classroom_bp = Blueprint('classroom',__name__)

@classroom_bp.route('/classrooms/<id>',methods=['GET'])
@token_required
def get_classrooms(id):
    return Classroom.get_classroom_by_id(id)

@classroom_bp.route('/classrooms/all/<teacher_id>',methods=['GET'])
@token_required
def get_classrooms_list(teacher_id):
    return Classroom.get_classroom_by_teacher_id(teacher_id)