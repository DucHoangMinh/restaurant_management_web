from db.models.subject_result import Subject_Result
from flask import request, Blueprint
import random
import string
from utils.controllers import token_required

subject_result_bp = Blueprint('subject_result', __name__)

@subject_result_bp.route('/subject_result', methods=['POST'])
@token_required
def create_subject_result():
    return Subject_Result.input_result(request)