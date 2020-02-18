from flask_restful import Resource
#from flask import request

from Model.Evento import Evento
from Dao.Evento_dao import EventoDao

class EventoController(Resource):
    def __init__(self):
        self.dao = EventoDao()

    def get(self):
        return self.dao.list_all()

