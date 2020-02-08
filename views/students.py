from flask import request
from flask_restful import Resource
from psycopg2.extras import Json
from models import Student, Teacher, Module, Course, serialize_multiple
from utils.viewsvalidator import ViewsValidator
from settings import db


class Students(Resource):

    def get(self):
        return serialize_multiple(Student.query.all())

    def post(self):
        data = request.get_json()
        return ViewsValidator(Student).post(data)


class SingleStudent(Resource):

    def get(self, student_id):
        return ViewsValidator(Student).get_by_id(student_id)

    def patch(self, student_id):
        data = request.get_json()
        student = Student.query.filter_by(id=student_id)
        student.update(data)
        db.session.commit()
        return {}, 204

    def delete(self, student_id):
        db.session.query(Student).filter_by(id=student_id).delete()
        db.session.commit()
        return {}, 200


class StudentTeacher(Resource):

    def get(self, student_id):
        return str(ViewsValidator(Student).get_by_id(student_id)["teacher"])

    def post(self, student_id):
        data = request.get_json()["teacher"]
        teacher = Teacher.query.filter_by(id=data)
        student = Student.query.filter_by(student_id)
        student.teacher.append(teacher)
        db.session.commit()
        return {}, 204


class StudentModule(Resource):

    def get(self, student_id):
        return str(ViewsValidator(Student).get_by_id(student_id)["modules"])

    def post(self, student_id):
        data = request.get_json()["module"]
        module = Module.query.get(data)
        student = Student.query.filter_by(student_id)
        student.module.append(module)
        db.session.commit()
        return {}, 204


class StudentCourse(Resource):

    def get(self, student_id):
        return str(ViewsValidator(Student).get_by_id(student_id)["course"])

    def post(self, student_id):
        data = request.get_json()["course"]
        course = Course.query.get(data)
        student = Student.query.filter_by(student_id)
        student.course.append(course)
        db.session.commit()
        return {}, 204



