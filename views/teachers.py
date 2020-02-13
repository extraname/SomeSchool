from flask import request
from flask_restful import Resource

from models import Teacher, serialize_multiple
from settings import db
from utils.modelsvalidator import ModelsValidator


class Teachers(Resource):

    def get(self):
        return serialize_multiple(Teacher.query.all())

    def post(self):
        data = request.get_json()
        return ModelsValidator(Teacher).post(data)


class SingleTeacher(Resource):

    def get(self, teacher_id):
        return ModelsValidator(Teacher).get_by_id(teacher_id)

    def patch(self, teacher_id):
        data = request.get_json()
        return ModelsValidator(Teacher).patch_by_id(teacher_id, data)

    def delete(self, teacher_id):
        db.session.query(Teacher).filter_by(id=teacher_id).delete()
        db.session.commit()
        return {}, 200


class TeacherCourse(Resource):

    def get(self, teacher_id):
        return ModelsValidator(Teacher).get_by_id(teacher_id)["course"]


class TeacherStudents(Resource):

    def get(self, teacher_id):
        return str(db.session.query(Teacher).get(teacher_id).students)
