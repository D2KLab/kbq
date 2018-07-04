from flask import (render_template, url_for, flash,
                   redirect, request,jsonify, abort, Blueprint)
from kbq import mongo
from kbq.sparql.queries import query_dbpedia_entityCount, query_graph, query_className, query_property_count , query_entity_count

from kbq.models import add_experiment,get_one_experiment

rest = Blueprint('rest',__name__)

@rest.route('/rest/<name>',methods=['GET','POST'])
def test(name):
    return name 

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





# testing adding users
#@rest.route('/add')
#def add():
 #   user = mongo.db.kbq
  #  user.insert({'name':'Anthony','language':'Python'})
   # user.insert({'name':'Kelly','language':'C'})
    #user.insert({'name':'John','language':'Java'})
   # user.insert({'name':'Cedric','language':'Haskell'})
   # return 'Added User!'

# Save experimental data in mongoDB

@rest.route('/rest/addexperiment',methods = ['GET'])
def save_experiment():

    endpoint = 'http://dbpedia.org/sparql'
    graph = 'http://dbpedia.org'
    className = 'http://dbpedia.org/ontology/Place'

    property_list = query_property_count(endpoint,graph,className)

    results = add_experiment(endpoint,graph,className,property_list)
         
    return results

@rest.route('/rest/getexperiment/<expId>',methods = ['GET'])
def get_experiment(expId):

    results = get_one_experiment(expId)

    return results