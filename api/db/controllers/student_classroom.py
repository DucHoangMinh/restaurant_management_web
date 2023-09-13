from db.models.student_classroom import Student_Classroom
from flask import request, Blueprint

from utils.controllers import token_required
std_clsr_bp = Blueprint('std_clsr_bp', __name__)

@std_clsr_bp.route('/student_classroom/<id>',methods=['GET'])
@token_required
def get_student_classroom(id):
    return Student_Classroom.get_student_in_classroom(id)