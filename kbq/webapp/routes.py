from flask import render_template,flash, url_for, redirect,jsonify, request, Blueprint
from kbq.webapp.forms import experimentForm
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from kbq.sparql.queries import query_with_endpoint,query_graph,query_className,query_property_count
from kbq.rest.routes import find_all_experiment
from kbq.models import get_all_experiment,add_experiment,check_className
import pygal

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

    return render_template('active.html', results = results)


@webapp.route('/results')
def resultsView():
    """Test results layout"""
    graph = pygal.Line()
    graph.title = '% Change Coolness of programming languages over time.'
    graph.x_labels = ['2011','2012','2013','2014','2015','2016']
    graph.add('Python',  [15, 31, 89, 200, 356, 900])
    graph.add('Java',    [15, 45, 76, 80,  91,  95])
    graph.add('C++',     [5,  51, 54, 102, 150, 201])
    graph.add('All others combined!',  [5, 15, 21, 55, 92, 105])
    graph_data = graph.render_data_uri()
    return render_template('results.html', graph_data = graph_data)


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


@webapp.route('/results/<results>')
def results(results):
    
    return render_template('results.html', results = results) 
    
    


