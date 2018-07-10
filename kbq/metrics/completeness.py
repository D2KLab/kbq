from kbq.metrics.metrics import Metrics

from flask import (render_template, url_for, flash,
                   redirect, request,jsonify, abort, Blueprint)


class Completeness(Metrics):


    
    def meaures(self,expId):
        stats_obj = self.get_stats(expId)
        """Property Completeness"""

        for prop in stats_obj:
            time = prop['property_stats']['timestamp']
            print(time)

        return jsonify(stats_obj)



    def plot(self,expId):
       pass

