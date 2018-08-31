from flask import render_template,flash, url_for, redirect,jsonify, request, Blueprint
from kbq.webapp.forms import experimentForm
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from kbq.sparql.queries import query_with_endpoint,query_graph,query_className,query_property_count
from kbq.rest.routes import find_all_experiment
from kbq.models import get_all_experiment,add_experiment,check_className
import pygal
import pandas as pd
import numpy as np

from kbq.metrics.completeness import Completeness
from kbq.metrics.consistency import Consistency
from kbq.metrics.persistency import Persistency
from kbq.metrics.hpersistency import Hpersistency

webapp = Blueprint('webapp',__name__)

@webapp.route('/')
@webapp.route('/home')
def home():
    return render_template('home.html')

@webapp.route('/experiment2')
def experiment2():
    """Test Experiment Layout"""
    return render_template('experiment2.html')    

@webapp.route('/experiment3')
def experiment3():
    """Test Experiment Layout"""
    return render_template('experiment3.html')

@webapp.route('/active')
def active_experiment():
    """Active experiment details"""
    results = get_all_experiment()

    res_active=[]
    sparql_list = []

    for result in results:
        if str(result['enabled']) == "True":
            res_active.append(result)
    
    for sparql in res_active:
        sparql_list.append(sparql['sparql'])

    unique_sparql_list = list(set(sparql_list))

    print(type(unique_sparql_list))

    return render_template('active.html', results = res_active, unique_sparql_list = unique_sparql_list)


#@webapp.route('/results')
#def resultsView():
#    """Test results layout"""
#    graph = pygal.Line()
#    graph.title = '% Change Coolness of programming languages over time.'
#    graph.x_labels = ['2011','2012','2013','2014','2015','2016']
#    graph.add('Python',  [15, 31, 89, 200, 356, 900])
#    graph.add('Java',    [15, 45, 76, 80,  91,  95])
#    graph.add('C++',     [5,  51, 54, 102, 150, 201])
#    graph.add('All others combined!',  [5, 15, 21, 55, 92, 105])
#    graph_data = graph.render_data_uri()
#    return render_template('results.html', graph_data = graph_data)

@webapp.route('/results/<expId>')
def resultView(expId):

    cons = Consistency()
    comp = Completeness()
    per = Persistency()
    hper = Hpersistency()

    statPersistency = per.meaures(expId)
    perValue = per.persistencyValue(expId) 

    df = per.table_values(expId) 
    entity = per.name_entity(expId)

    statHpersistency = hper.meaures(expId)
    
    HperValue = hper.H_persistencyValue(expId)

    statCompleteness = comp.meaures(expId)
    comValue = comp.comp_value(expId)
    print(comValue)    
    statConsistency = cons.meaures(expId)
    conValue = cons.consistency_value(expId)
    
    #print(stat)
    return render_template('results.html', resultsConsistency = statConsistency,conValue=conValue, comValue = comValue, HperValue = HperValue, df = df, entity = entity, resultsCompleteness = statCompleteness[1:10],resultsPersistency = statPersistency,resultsHpersistency = statHpersistency, perValue = perValue)

@webapp.route('/experiment',methods = ['GET','POST'])
def experiment():  
    if request.method == 'POST':
        form = request.form['form']
        print(form)
   
        if form == "endpoint":
            endpoint = request.form['endpoint']
            print(endpoint)
            results = query_graph(endpoint)
            #print(results)
            output = []
            for result in results['results']['bindings']:
                output.append(result['g']['value'])
            return jsonify({'endpoint' : output})

        if form == "graph":
            graph = request.form['graph']
            endpoint = request.form['endpoint']
            print(graph)
            results = query_className(endpoint,graph)

            #print(results)            
            className = []
            for result in results['results']['bindings']:
                className.append(result['class']['value'])

            return jsonify({'className' : className})

        if form == "runexpriment":
            graph = request.form['graph']
            endpoint = request.form['endpoint']
            className =  request.form['className']

            if check_className(className):
                return jsonify({'status':'Already Exists','Flag':False})
            else:
                # property list
                propertyList = query_property_count(endpoint,graph,className)
                expId = add_experiment(endpoint,graph,className,propertyList)
                return jsonify({'status':'Experiment Created','expId':expId,'Flag':True})

            #redirect(url_for('webapp.results', results = results))
        #else:
        #    return jsonify({'error':'error'})

    return render_template('experiment.html', title='Configuration')

@webapp.route('/shape')
def shape():
    return  render_template('shape.html', title='SHACL')

@webapp.route('/about')
def about():
    return render_template('about.html', title='About Us')

#@webapp.route('/results/<results>')
#def results(results):
#   return render_template('results.html', results = results) 
    
    


