from flask import (render_template, url_for, flash,
                   redirect, request,jsonify, abort, Blueprint)
from kbq import mongo
from kbq.sparql.queries import query_dbpedia_entityCount, query_graph, query_className, query_property_count , query_entity_count

from kbq.models import (add_experiment,get_one_experiment, update_experiment_enabled,
                        update_experiment_status,append_stats,get_all_experiment,delete_all_records,stats_snapshots)
from kbq.metrics.completeness import Completeness
from kbq.metrics.consistency import Consistency

rest = Blueprint('rest',__name__)

@rest.route('/metrics/completeness/<expId>',methods=['GET'])
def completeness(expId):
    comp = Completeness()
    stat = comp.meaures(expId)
    return stat

@rest.route('/metrics/consistency/<expId>',methods=['GET'])
def consistency(expId):
    cons = Consistency()
    stat = cons.meaures(expId)
    return stat


@rest.route('/rest/queryTest',methods=['GET','POST'])
def queryTest():
    results = query_dbpedia_entityCount()
   
    output = []

    for result in results["results"]["bindings"]:
        output.append({'p':result['p']['value'],'freq':result['freq']['value']})
        
    return jsonify({'result':output})
    
# test api for extracting graph name    
@rest.route('/rest/graph',methods=['GET'])
def graphName():
    endpoint = 'http://dbpedia.org/sparql'
    results = query_graph(endpoint)

    output = []

    for result in results['results']['bindings']:
        output.append({'graph':result['g']['value']})

    return jsonify({'result': output})


# test api for extracting class name
@rest.route('/rest/class',methods = ['GET'])
def className():
    endpoint = 'http://dbpedia.org/sparql'
    graph = 'http://dbpedia.org'
    
    results = query_className(endpoint,graph)

    output = []

    for result in results['results']['bindings']:
        output.append({'className': result['class']['value']})

    return jsonify({'result': output})


# test api for extracting entityCount
@rest.route('/rest/entityCount',methods = ['GET'])
def entityCount():
    endpoint = 'http://dbpedia.org/sparql'
    graph = 'http://dbpedia.org'
    className = 'http://dbpedia.org/ontology/Place'
    
    results = query_entity_count(endpoint,graph,className)
    
    return jsonify(results)

    
@rest.route('/rest/property', methods = ['GET'])
def properties():
    endpoint = 'http://dbpedia.org/sparql'
    graph = 'http://dbpedia.org'
    className = 'http://dbpedia.org/ontology/Place'

    results = query_property_count(endpoint,graph,className)
    
    #for result in results['results']['bindings']:
    #    output.append({'Property': result['p']['value'],'Frequency': result['Freq']['value']})

    return jsonify({'result': results})


# Save experimental data in mongoDB

@rest.route('/rest/addexperiment',methods = ['GET'])
def save_experiment():

    endpoint = 'http://dbpedia.org/sparql'
    graph = 'http://dbpedia.org'
    className = 'http://dbpedia.org/ontology/Place'

    property_list = query_property_count(endpoint,graph,className)

    results = add_experiment(endpoint,graph,className,property_list)
         
    return jsonify(results)

@rest.route('/rest/getexperiment/<expId>',methods = ['GET'])
def get_experiment(expId):

    results = get_one_experiment(expId)

    return jsonify(results)


@rest.route('/rest/getallexperiment',methods = ['GET'])
def find_all_experiment():

    results = get_all_experiment()

    return jsonify(results)


@rest.route('/rest/append_exp/<expId>',methods = ['GET'])
def append_exp(expId):
    
    """
    Periodic snapshots checks
    Test Sparql Endpoint:
    endpoint = 'http://dbpedia.org/sparql'
    graph = 'http://dbpedia.org'
    className = 'http://dbpedia.org/ontology/Place'
    property_list = query_property_count(endpoint,graph,className)
    results = append_stats(expId,property_list)
    """
    results = stats_snapshots(expId)

    return jsonify(results)

@rest.route('/rest/update_enabled/<expId>/<value>',methods = ['GET'])
def update_enabled(expId,value):
    results = update_experiment_enabled(expId,value)
    return jsonify(results)

@rest.route('/rest/update_status/<expId>/<value>',methods = ['GET'])
def update_status(expId,value):

    results = update_experiment_status(expId,value)

    return jsonify(results)

@rest.route('/rest/delete_all')
def delete_all():

    output = delete_all_records()    

    return jsonify(output)


