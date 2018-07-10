from kbq.metrics.metrics import Metrics

from flask import (render_template, url_for, flash,
                   redirect, request,jsonify, abort, Blueprint)


class Consistency(Metrics):
    
    def meaures(self,expId):
        stats_obj = self.get_stats(expId)
        print(type(stats_obj))
        prop = []
        
        for prop in stats_obj:
            print(prop)

        return jsonify( stats_obj)

    def plot(self,expId):
       pass

