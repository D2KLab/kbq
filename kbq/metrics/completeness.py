from kbq.metrics.metrics import Metrics

from flask import (render_template, url_for, flash,
                   redirect, request,jsonify, abort, Blueprint)

import json


class Completeness(Metrics):

    time_list_date = []
    property_list = []
    def meaures(self,expId):

        stats_obj = self.get_stats(expId)

        r = json.dumps(stats_obj,default=self.myconverter) 
        stats_obj_json = json.loads(r)
                
        data_time = []
        dict_data_items = {}
        count_total = 0

        for prop in stats_obj_json['property_stats']:

            date_timestamp = str(prop['timestamp']).split(' ')
            

            data_time.append(date_timestamp[0])

            
            self.time_list_date.append(date_timestamp[0])  
            
            for property in prop['property_freq']:
                if property['Property'] not in dict_data_items:
                    dict_data_items[property['Property']] = []

               
                count_total += 1
               
                dict_data_items[property['Property']].append(int(property['Frequency']))
               

        data_plot = []    
        for property in dict_data_items:
            trace = {}
            trace['x'] = data_time
            trace['y'] = dict_data_items[property]
            trace['name'] = property
            data_plot.append(trace)

        return data_plot

    def comp_value(self,expId):

        stats_obj = self.get_stats(expId)

        r = json.dumps(stats_obj,default=self.myconverter) 
        stats_obj_json = json.loads(r)
                
        data_time = []
        dict_data_items = {}
        count_total = 1
        count_incomplete = 0
          
        for prop in stats_obj_json['property_stats']:

            date_timestamp = str(prop['timestamp']).split(' ')
            
            data_time.append(date_timestamp[0])

            self.time_list_date.append(date_timestamp[0])  
            
            for property in prop['property_freq']:
                if property['Property'] not in dict_data_items:
                    dict_data_items[property['Property']] = []

                prop_freq = []
                count_total+= 1     
                dict_data_items[property['Property']].append(int(property['Frequency']))
                prop_freq.append(int(property['Frequency']))


        data_plot = []    
        for property in dict_data_items:
            trace = {}

            trace['x'] = data_time
            trace['y'] = dict_data_items[property]
            if dict_data_items[property][-1] < dict_data_items[property][-2]:
                count_incomplete+= 1 
            trace['name'] = property
            data_plot.append(trace)

        print(count_total)
 
        value=(count_total/count_total)*100

        value = 100

        return value

    def plot(self,expId):
       pass

