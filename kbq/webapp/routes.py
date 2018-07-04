from flask import render_template,flash, url_for, redirect,jsonify, request, Blueprint
from kbq.webapp.forms import experimentForm
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from kbq.sparql.queries import query_with_endpoint,query_graph,query_className,query_property_count
webapp = Blueprint('webapp',__name__)

@webapp.route('/')
@webapp.route('/home')
def home():
    return render_template('home.html')


@webapp.route('/experiment',methods = ['GET','POST'])
def experiment():  
    if request.method == 'POST':
        form = request.form['form']
        #graph = request.form['graph']
        
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
       # else:
       #     return jsonify({'error':'error'})

        if form == "graph":
            graph = request.form['graph']
            endpoint = request.form['endpoint']
            print(graph)
            results = query_className(endpoint,graph)

            #print(results)            
            className = []
            for result in results['results']['bindings']:
                className.append(result['class']['value'])

            print(className)

            return jsonify({'className' : className})

        if form == "runexpriment":
            graph = request.form['graph']
            endpoint = request.form['endpoint']
            className =  request.form['className']
            print(className)
            
            

            # property list
            results = query_property_count(endpoint,graph,className)

                        

            expId = '58275'
            return jsonify({'expId': expId})
            
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
    
    


