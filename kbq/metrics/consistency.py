from kbq.metrics.metrics import Metrics

from flask import (render_template, url_for, flash,
                   redirect, request,jsonify, abort, Blueprint)
from bson.objectid import ObjectId
import time,json
from datetime import datetime

from kbq import mongo

import numpy as np
import pandas as pd

class Consistency(Metrics):

    time_list_date = []
    property_list = []
    
    def meaures(self,expId):

        stats_obj = self.get_stats(expId)

        r = json.dumps(stats_obj,default=self.myconverter) 
        stats_obj_json = json.loads(r)
                
        #for prop in stats_obj_json['entity_stats']:
        #    print(prop['timestamp'])
            #pass
        data_time = []
        dict_data_items = {}
            
        for prop in stats_obj_json['property_stats']:
            #print(prop['property_freq'])
            #print(type(prop['property_freq']))

            print(prop['timestamp'])
            #print(datetime.strptime(prop['timestamp'],'%Y %M %d'))

            date_timestamp = str(prop['timestamp']).split(' ')
            
            #print(date_timestamp[0])

            data_time.append(date_timestamp[0])

            
            self.time_list_date.append(date_timestamp[0])  
            
            for property in prop['property_freq']:
                #print(property['Property']+'-'+ property['Frequency'])
                #if property['Property'] not in dict_data_items:
                #    dict_data_items[property['Property']] = []

                if int(property['Frequency'])<=100:
                    if property['Property'] not in dict_data_items:
                        dict_data_items[property['Property']] = []

                    dict_data_items[property['Property']].append(int(property['Frequency']))
                
       
        data_plot = []    
        for property in dict_data_items:
            trace = {}
            trace['x'] = data_time
            trace['y'] = dict_data_items[property]
            trace['name'] = property
            trace['Consistency'] = 1
            data_plot.append(trace)
            
            #print(dict_data_items)               
            #print(prop['timestamp'])
        #print(self.time_list_date) 



        return data_plot

    def consistency_value(self,expId):

        stats_obj = self.get_stats(expId)

        r = json.dumps(stats_obj,default=self.myconverter) 
        stats_obj_json = json.loads(r)
                
        #for prop in stats_obj_json['entity_stats']:
        #    print(prop['timestamp'])
            #pass
        data_time = []
        dict_data_items = {}
        consistency_total=0 
        con_total=0   
        for prop in stats_obj_json['property_stats']:
            #print(prop['property_freq'])
            #print(type(prop['property_freq']))

            print(prop['timestamp'])
            #print(datetime.strptime(prop['timestamp'],'%Y %M %d'))

            date_timestamp = str(prop['timestamp']).split(' ')
            
            #print(date_timestamp[0])

            data_time.append(date_timestamp[0])

            
            self.time_list_date.append(date_timestamp[0])  
            
            for property in prop['property_freq']:
                #print(property['Property']+'-'+ property['Frequency'])
                #if property['Property'] not in dict_data_items:
                #    dict_data_items[property['Property']] = []

                if int(property['Frequency'])<=100:
                    if property['Property'] not in dict_data_items:
                        dict_data_items[property['Property']] = []

                    consistency_total+=1

                    dict_data_items[property['Property']].append(int(property['Frequency']))
                else:
                    con_total+=1


        data_plot = []    
        for property in dict_data_items:
            trace = {}
            trace['x'] = data_time
            trace['y'] = dict_data_items[property]
            trace['name'] = property
            data_plot.append(trace)
            
            #print(dict_data_items)               
            #print(prop['timestamp'])
        #print(self.time_list_date) 
        # 
        count_total = consistency_total/(con_total+consistency_total)   

        return count_total*100

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

