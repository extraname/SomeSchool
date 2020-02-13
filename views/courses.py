from flask import request
from flask_restful import Resource

from models import Course, serialize_multiple
from settings import db
from utils.modelsvalidator import ModelsValidator


class Courses(Resource):

    def get(self):
        return serialize_multiple(Course.query.all())

    def post(self):
        data = request.get_json()
        return ModelsValidator(Course).post(data)


class SingleCourse(Resource):

    def get(self, course_id):
        return ModelsValidator(Course).get_by_id(course_id)

    def patch(self, course_id):
        data = request.get_json()
        return ModelsValidator(Course).patch_by_id(course_id, data)

    def delete(self, course_id):
        db.session.query(Course).filter_by(id=course_id).delete()
        db.session.commit()
        return {}, 200


class CourseModules(Resource):  # пересмотреть пост запрос

    def get(self, course_id):
        # return str(Course.query.get(course_id).module)
        return str(ModelsValidator(Course).get_by_id(course_id)["modules"])


class CourseTeacher(Resource):  # рассмотреть варинт патч

    def get(self, course_id):
        return ModelsValidator(Course).get_by_id(course_id)["teacher"]


class CourseStudents(Resource):  # рассмотреть варинт патч

    def get(self, course_id):
        return ModelsValidator(Course).get_by_id(course_id)["students"]
