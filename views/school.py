from flask import request
from flask_restful import Resource

from models import School, serialize_multiple
from utils.modelsvalidator import ModelsValidator
from settings import db


class MySchool(Resource):
    def get(self):
        return ModelsValidator(School).get()

