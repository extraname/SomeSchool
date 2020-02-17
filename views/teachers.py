from flask import request
from flask_restful import Resource

from models import Teacher, serialize_multiple
from settings import db
from utils.modelsvalidator import ModelsValidator


class Teachers(Resource):

    @staticmethod
    def get():
        return serialize_multiple(Teacher.query.all())

    @staticmethod
    def post():
        data = request.get_json()
        return ModelsValidator(Teacher).post(data)


class SingleTeacher(Resource):

    @staticmethod
    def get(teacher_id):
        return ModelsValidator(Teacher).get_by_id(teacher_id)

    @staticmethod
    def patch(teacher_id):
        data = request.get_json()
        return ModelsValidator(Teacher).patch_by_id(teacher_id, data)

    @staticmethod
    def delete(teacher_id):
        db.session.query(Teacher).filter_by(id=teacher_id).delete()
        db.session.commit()
        return {}, 200


class TeacherCourse(Resource):

    @staticmethod
    def get(teacher_id):
        return ModelsValidator(Teacher).get_by_id(teacher_id)["course"]


class TeacherStudents(Resource):

    @staticmethod
    def get(teacher_id):
        return str(db.session.query(Teacher).get(teacher_id).students)
