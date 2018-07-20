from SPARQLWrapper import SPARQLWrapper, JSON
from flask import render_template,flash, url_for, redirect,jsonify, request, Blueprint

def query_dbpedia_entityCount():
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    propertName = 'Person'

    sparql.setQuery("""
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX quepy: <http://www.machinalis.com/quepy#>
        PREFIX dbpedia: <http://dbpedia.org/ontology/>
        PREFIX dbpprop: <http://dbpedia.org/property/>
        PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
        select ?p (COUNT( ?p) as ?freq)
        where {
            ?s ?p ?o.
            ?s a dbpedia:%s.
        }LIMIT 100 
        """%(propertName))

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    return results

def query_with_endpoint(endpoint):
    sparql = SPARQLWrapper(endpoint)
    propertName = 'Person'

    sparql.setQuery("""
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX quepy: <http://www.machinalis.com/quepy#>
        PREFIX dbpedia: <http://dbpedia.org/ontology/>
        PREFIX dbpprop: <http://dbpedia.org/property/>
        PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
        select ?p (COUNT( ?p) as ?freq)
        where {
            ?s ?p ?o.
            ?s a dbpedia:%s.
        }LIMIT 100 
        """%(propertName))

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    return results

# Get all graph names
def query_graph(endpoint):
     sparql = SPARQLWrapper(endpoint)
     sparql.setQuery("""
        select ?g (count(?s) as ?entityCount) 
        where { graph ?g{?s a ?o}} 
        group by ?g
     """)
     sparql.setReturnFormat(JSON)
     results = sparql.query().convert()

     return results



# Get all Class Names
# Example
# select count(*)
# where {
#   graph<http://3cixty.com/nice/places> {?s a dul:Place.}
# }

def query_className(endpoint,graph):
     print(graph)
     sparql = SPARQLWrapper(endpoint)
     sparql.setQuery("""
     select distinct  ?class 
      where  {
         graph<%s>{ ?s a ?class. }
        }
       
     """%(graph))
     sparql.setReturnFormat(JSON)
     results = sparql.query().convert()

     return results


# select ?p (COUNT(?p) as ?pCount)
# where {
#   graph<http://3cixty.com/nice/places> {?s a dul:Place}
#   ?s ?p ?o.
# }

def query_property_count(endpoint,graph,className):
    print(className)
    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery("""
      select ?p  (COUNT(?p) as ?Freq) 
      where  {
         graph<%s>{ ?s a <%s>. }
         ?s ?p ?o.
        } 
     """%(graph,className))
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    output = []
    for result in results['results']['bindings']:
        output.append({'Property': result['p']['value'],'Frequency': result['Freq']['value']})

    return output

   
def query_entity_count(endpoint,graph,className):

    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery("""
     select (COUNT(distinct ?s) as ?entityCount) 
      where  {
         graph<%s>{ ?s a <%s>. }
      }
     """%(graph,className))
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    print(results)

    output = int(results['results']['bindings'][0]['entityCount']['value'])
    print(output)

    return output





