from flask import request
from flask_restful import Resource

from models import Module, serialize_multiple
from utils.modelsvalidator import ModelsValidator
from settings import db


class Modules(Resource):

    def get(self):
        return serialize_multiple(Module.query.all())

    def post(self):
        data = request.get_json()
        return ModelsValidator(Module).post(data)


class SingleModule(Resource):

    def get(self, module_id):
        return ModelsValidator(Module).get_by_id(module_id)

    def patch(self, module_id):
        data = request.get_json()
        return ModelsValidator(Module).patch_by_id(module_id, data)

    def delete(self, module_id):
        db.session.query(Module).filter_by(id=module_id).delete()
        db.session.commit()
        return {}, 200


class ModuleCourse(Resource):

    def get(self, module_id):
        return str(Module.query.get(module_id).course)
