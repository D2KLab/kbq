from kbq.metrics.metrics import Metrics

from flask import (render_template, url_for, flash,
                   redirect, request,jsonify, abort, Blueprint)
#from kbq import mongo
#from kbq.sparql.queries import query_dbpedia_entityCount, query_graph, query_className, query_property_count , query_entity_count
#from kbq.models import add_experiment,get_one_experiment, update_experiment_enabled,update_experiment_status,append_stats, get_all_experiment
#completeness = Blueprint('completeness',__name__)

class Persistency(Metrics):
    
    def meaures(self,expId):
        stats_obj = self.get_stats(expId)
        return jsonify(stats_obj)

    def plot(self,expId):
       pass

