from flask import request
from flask_restful import Resource

from models import School, serialize_multiple
from utils.viewsvalidator import ViewsValidator
from settings import db


class MySchool(Resource):
    def get(self):
        return ViewsValidator(School).get()

