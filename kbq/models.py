from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import datetime
from bson.objectid import ObjectId
from kbq import mongo
from kbq.sparql.queries import query_dbpedia_entityCount, query_graph, query_className, query_property_count , query_entity_count


def add_experiment(endpoint,graph,className,propertyList):
    """Add a new experiment in the mongo db and return the saved results"""

    experiment = mongo.db.experiment
    
    stat = mongo.db.stat
    
    """Experiment collection Keys:
       sparql: <uri: sparql endpoint>
       graph: <uri: graph name>
       class: <uri: class name>
       enabled: <boolean: True/False>
       status: <str: active/inactive>          
    """
    experiment_id = experiment.insert({'sparql': endpoint,'graph': graph,'className': className,'enabled': 'False', 'status':'active'})
    new_experiment = experiment.find_one({'_id': experiment_id})
    new_experiment['_id'] = str(experiment_id)
    
    """Stat collection keys:
       experiment_id: <str: experiment id>
       entity_stats:{<datetime:date>,<int:count>}
       property_stats:{<datetime:date>,
                        list:[<property,count>]
                      }    
    """
    if new_experiment:

        timestamp = datetime.datetime.now()
        entityCount = query_entity_count(endpoint,className,graph)

        entity_stats = []
        entity_stats.append({'timestamp': timestamp,'entityCount': entityCount})

        property_stats = []
        property_stats.append({'timestamp': timestamp,'property_freq':propertyList})
        stat_id = stat.insert({'experiment_id': str(experiment_id), 'entity_stats': entity_stats,'property_stats':property_stats})

        new_stat = stat.find_one({'_id': stat_id})
        new_stat['_id'] = str(stat_id)

        if new_stat:
            return str(stat_id) #jsonify({'experiment': new_experiment,'stat': new_stat})
        else:
            return {'result':'fail to add new experiment'}
    else:
        return jsonify({'result':'fail to add new experiment'})

def check_className(className):

    exp = mongo.db.experiment

    exp_check = exp.find_one({'className': className})
    
    if exp_check:
        return True
    else:
        return False
   

def new_stats_entity(endpoint,graph,className,propertyList):
    
    timestamp = datetime.datetime.now()
    entityCount = query_entity_count(endpoint,className,graph)

    entity_stats = []
    entity_stats.append({'timestamp': timestamp,'entityCount': entityCount})

    return entity_stats

def new_stats_property(endpoint,graph,className,propertyList):
    
    timestamp = datetime.datetime.now()
    #property_stats = {'timestamp': timestamp,'property_freq':propertyList}

    property_stats = []
    property_stats.append({'timestamp': timestamp,'property_freq':propertyList})

    return property_stats



def append_stats(expId,propertyList):
    """Search one experiment from mongo db"""

    exp = mongo.db.experiment
    stat = mongo.db.stat

    print(expId)

    exp_output = exp.find_one({'_id': expId})
    #exp_output['_id'] = expId

    if exp_output:

        timestamp = datetime.datetime.now()
        #entity_stats = []
        #entity_stats.append({'timestamp': timestamp,'entityCount': 1254})
        
        entity_stats = {'timestamp': timestamp,'entityCount': 1111}

        property_stats = {'timestamp': timestamp,'property_freq':propertyList}

        #print(property_stats)

        stat = stat.update({'experiment_id': str(expId)},{'$push':{'entity_stats':entity_stats,'property_stats':property_stats}})
        print(stat)

        output =  get_one_experiment(expId)

    else:
        output = jsonify({'results':'No result found'})

    return output

def update_experiment_enabled(expId,value):
    """update experiment enabled"""

    exp = mongo.db.experiment
    stat = mongo.db.stat

    print(expId)

    exp_output = exp.find_one({'_id': ObjectId(expId)})
    exp_output['_id'] = expId

    if exp_output:
        exp_output['enabled'] = value
        exp.save(exp_output)
        stat_output = stat.find_one({'experiment_id': str(expId)})
        stat_output['_id'] = str(stat_output['_id'])

        output = exp_output
    else:
        output = {'results':'No result found'}

    return output

def update_experiment_status(expId,value):
    """updated experiment status"""

    exp = mongo.db.experiment
    stat = mongo.db.stat

    print(expId)

    exp_output = exp.find_one({'_id': ObjectId(expId)})
    exp_output['_id'] = expId

    if exp_output:
        exp_output['status'] = value
        exp.save(exp_output)
        stat_output = stat.find_one({'experiment_id': str(expId)})
        stat_output['_id'] = str(stat_output['_id'])

        output =  exp_output
    else:
        output = jsonify({'results':'No result found'})

    return output



def get_one_experiment(expId):
    """Search one experiment from mongo db"""

    exp = mongo.db.experiment
    stat = mongo.db.stat

    print(expId)

    exp_output = exp.find_one({'_id': ObjectId(expId)})
    #print(exp_output)
    #exp_output['_id'] = expId

    if exp_output:
        
        stat_output = stat.find_one({'experiment_id': str(expId)})
        stat_output['_id'] = str(stat_output['_id'])
        
        output = stat_output #jsonify({'experiment': exp_output,'stat': stat_output})
    else:
        output = {'results':'No result found'}

    return output


def get_all_experiment():
    
    exp = mongo.db.experiment

    output = [] 

    for q in exp.find():
        output.append({'className':q['className'], 'graph': q['graph'],'sparql': q['sparql'],'enabled':q['enabled'],'status': q['status'],'expId':str(q['_id'])})

    return output


def stats_snapshots(expId):
    """Search one experiment from mongo db"""
    
    exp = mongo.db.experiment
    stat = mongo.db.stat

    print(expId)

    exp_output = exp.find_one({'_id': ObjectId(expId)})
    exp_output['_id'] = expId

    timestamp = datetime.datetime.now()

    if exp_output:

        entity_count = query_entity_count(exp_output['sparql'],exp_output['graph'],exp_output['className'])
        
        entity_stats = {'timestamp': timestamp,'entityCount': entity_count }

        propertyList = query_property_count(exp_output['sparql'],exp_output['graph'],exp_output['className'])

        property_stats = {'timestamp': timestamp,'property_freq':propertyList}

        #print(property_stats)

        stat = stat.update({'experiment_id': str(expId)},{'$push':{'entity_stats':entity_stats,'property_stats':property_stats}})
        #output =  get_one_experiment(expId)
        output = stat

    else:
        output = {'results':'No result found'}

    return output



def delete_all_records():
    """Clear records"""
    exp = mongo.db.experiment
    stats = mongo.db.stats

    ex = exp.remove({})
    st= stats.remove({})
    
    if ex and st:
        return 'success'
    else:
        return 'fail'








