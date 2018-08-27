from kbq.metrics.metrics import Metrics

from flask import (render_template, url_for, flash,
                   redirect, request,jsonify, abort, Blueprint)

from bson.objectid import ObjectId
import time,json
from datetime import datetime

from kbq import mongo

import numpy as np
import pandas as pd


class Hpersistency(Metrics):
    
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


    def H_persistencyValue(self,expId):
        stats_obj = self.get_stats(expId)

        r = json.dumps(stats_obj,default=self.myconverter) 
        stats_obj_json = json.loads(r)

        data_time = []
        entity_count = []  

        for entity in stats_obj_json['entity_stats']:
            
            date_timestamp = str(entity['timestamp']).split(' ')
            
            data_time.append(date_timestamp[0])

            entity_count.append(int(entity['entityCount']))

        per_value = 1*100

        #if entity_count[-1] < entity_count[-2]:
        #    per_value = 0        

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
