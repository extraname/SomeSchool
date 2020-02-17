from flask_restful import Resource

from models import School
from utils.modelsvalidator import ModelsValidator


class MySchool(Resource):

    @staticmethod
    def get():
        return ModelsValidator(School).get()
