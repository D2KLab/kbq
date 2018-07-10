from flask import (render_template, url_for, flash,
                   redirect, request,jsonify, abort, Blueprint)
from kbq import mongo
from kbq.sparql.queries import query_dbpedia_entityCount, query_graph, query_className, query_property_count , query_entity_count

from kbq.models import stats_snapshots,add_experiment,get_one_experiment, update_experiment_enabled,update_experiment_status,append_stats,get_all_experiment,delete_all_records
from kbq.metrics.completeness import Completeness
from kbq.metrics.consistency import Consistency
import datetime
import time

schedule = Blueprint('schedule',__name__)

from kbq import mongo
from kbq.models import get_all_experiment

start_time = time.time()

def scheduler_module():
    with mongo.app.app_context():
        experiments = get_all_experiment()
        for exp in experiments:
            if exp['status'] == 'active':
                exp_id = exp['expId']
                stats = get_one_experiment(exp_id)
                print(stats)
                stats_snapshots(exp_id)
            else:
                pass    
