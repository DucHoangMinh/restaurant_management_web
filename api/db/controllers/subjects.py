from db.models.subjects import Subject
from flask import request, Blueprint
import random
import string
from utils.controllers import token_required

subjects_bp = Blueprint('subjects', __name__)

@subjects_bp.route('/subjects/<id>', methods=['GET'])
@token_required
def get_subject(id):
    return Subject.get_subject_by_id(id)