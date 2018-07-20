from abc import ABC, abstractmethod

from flask import (render_template, url_for, flash,
                   redirect, request,jsonify, abort, Blueprint)
from kbq import mongo
from kbq.sparql.queries import query_dbpedia_entityCount, query_graph, query_className, query_property_count , query_entity_count
from kbq.models import add_experiment,get_one_experiment, update_experiment_enabled,update_experiment_status,append_stats, get_all_experiment
import datetime,json

metrics = Blueprint('metrics',__name__)

class Metrics(ABC): 
  
    @staticmethod
    def get_stats(expId):
        """Get stats based on experiment id"""
        stat_json_object = get_one_experiment(expId)
        return stat_json_object

    @staticmethod
    def myconverter(o):
        """JSON data time converter"""
        if isinstance(o, datetime.datetime):
            return o.__str__()

    @abstractmethod
    def meaures(self,expId):
        pass

    @abstractmethod
    def plot(self,expId):
        pass





    

    

    
