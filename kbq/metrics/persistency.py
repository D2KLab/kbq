from kbq.metrics.metrics import Metrics

from flask import (render_template, url_for, flash,
                   redirect, request,jsonify, abort, Blueprint)
#from kbq import mongo
#from kbq.sparql.queries import query_dbpedia_entityCount, query_graph, query_className, query_property_count , query_entity_count
#from kbq.models import add_experiment,get_one_experiment, update_experiment_enabled,update_experiment_status,append_stats, get_all_experiment
#completeness = Blueprint('completeness',__name__)
from bson.objectid import ObjectId
import time,json
from datetime import datetime

from kbq import mongo

import numpy as np
import pandas as pd

class Persistency(Metrics):
    
    def meaures(self,expId):
        stats_obj = self.get_stats(expId)

        r = json.dumps(stats_obj,default=self.myconverter) 
        stats_obj_json = json.loads(r)

        data_time = []
        entity_count = []  

        for entity in stats_obj_json['entity_stats']:
            
            date_timestamp = str(entity['timestamp']).split(' ')
            
            data_time.append(date_timestamp[0])

            entity_count.append(int(entity['entityCount']))

        data_plot = []
        trace = {}
        trace['x'] = data_time
        trace['y'] = entity_count
        trace['name'] = self.name_entity(expId)
        data_plot.append(trace)

                               
        return data_plot

    def table_values(self,expId):
        stats_obj = self.get_stats(expId)

        r = json.dumps(stats_obj,default=self.myconverter) 
        stats_obj_json = json.loads(r)

        data_time = []
        entity_count = []  

        for entity in stats_obj_json['entity_stats']:
            
            date_timestamp = str(entity['timestamp']).split(' ')
            
            data_time.append(date_timestamp[0])

            entity_count.append(int(entity['entityCount']))

        data_plot = []
        trace = {}
        trace['x'] = data_time
        trace['y'] = entity_count
        trace['name'] = self.name_entity(expId)
        data_plot.append(trace)

        df = pd.DataFrame(list(zip(data_time, entity_count)), columns=['Date','Count'])
                               
        return df

    
    def persistencyValue(self,expId):
        stats_obj = self.get_stats(expId)

        r = json.dumps(stats_obj,default=self.myconverter) 
        stats_obj_json = json.loads(r)

        data_time = []
        entity_count = []  

        for entity in stats_obj_json['entity_stats']:
            
            date_timestamp = str(entity['timestamp']).split(' ')
            
            data_time.append(date_timestamp[0])

            entity_count.append(int(entity['entityCount']))

        per_value = 1

        if entity_count[-1] < entity_count[-2]:
            per_value = 0        

        return per_value


    def name_entity(self,expId):

        exp = mongo.db.experiment
        print(expId)
        exp_output = exp.find_one({'_id': ObjectId(expId)})

        if exp_output:
            return exp_output['className']
        else:
            return 'Not Found'
    
    
    def plot(self,expId):
       pass

