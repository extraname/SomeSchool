from flask import request
from flask_restful import Resource

from models import Module, serialize_multiple
from settings import db
from utils.modelsvalidator import ModelsValidator


class Modules(Resource):

    @staticmethod
    def get():
        return serialize_multiple(Module.query.all())

    @staticmethod
    def post():
        data = request.get_json()
        return ModelsValidator(Module).post(data)


class SingleModule(Resource):

    @staticmethod
    def get(module_id):
        return ModelsValidator(Module).get_by_id(module_id)

    @staticmethod
    def patch(module_id):
        data = request.get_json()
        return ModelsValidator(Module).patch_by_id(module_id, data)

    @staticmethod
    def delete(module_id):
        db.session.query(Module).filter_by(id=module_id).delete()
        db.session.commit()
        return {}, 200


class ModuleCourse(Resource):

    @staticmethod
    def get(module_id):
        return str(Module.query.get(module_id).course)
