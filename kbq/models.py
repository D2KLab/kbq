from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import kbq.sparql.queries as queries 
import datetime
from bson.objectid import ObjectId

from kbq import mongo


# Save experiment and stat in mongo db collections: Experiment , Stat
def add_experiment(endpoint,graph,className,propertyList):

    experiment = mongo.db.experiment

    stat = mongo.db.stat
    
    experiment_id = experiment.insert({'sparql': endpoint,'className': className,'graph': graph,'enabled':'False'})

    timestamp = datetime.datetime.now()

    new_experiment = experiment.find_one({'_id': experiment_id})
    new_experiment['_id'] = str(experiment_id)

    entityCount = queries.query_entity_count(endpoint,className,graph)

    stat_id = stat.insert({'timestamp': timestamp,'entity_count':entityCount['entityCount'],'property_stat':propertyList,'experiment_id': str(experiment_id)})

    new_stat = stat.find_one({'_id': stat_id})
    new_stat['_id'] = str(stat_id)

    return jsonify({'experiment': new_experiment,'stat': new_stat})
   


def get_one_experiment(expId):

    exp = mongo.db.experiment
    stat = mongo.db.stat

    print(expId)

    exp_output = exp.find_one({'_id': ObjectId(expId)})
    exp_output['_id'] = expId

    if exp_output:
        stat_output = stat.find_one({'experiment_id': str(expId)})
        stat_output['_id'] = str(stat_output['_id'])

        output = jsonify({'experiment': exp_output,'stat': stat_output})
    else:
        output = jsonify({'results':'No result found'})

    return output


def get_all_experiment(expId):

    return 'all'





