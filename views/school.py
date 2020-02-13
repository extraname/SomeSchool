from flask_restful import Resource

from models import School
from utils.modelsvalidator import ModelsValidator


class MySchool(Resource):
    def get(self):
        return ModelsValidator(School).get()
