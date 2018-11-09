from SPARQLWrapper import SPARQLWrapper, JSON

def cardinality_extraction(endpoint, class_name):
    """
    Cardinality value extraction.
    1. Extract all the properties based on the given class.
    2. Based on each properties extract raw cardinality values.
    Parm: 
    endpoint- KB SPARQL endpoint
    class_name- Input class_name from UI
    Return:
    Dict-  dictory constains - Proporties, Card, Instance Count
    """

    
    pass


# query for object value prediction
def object_prediction():
    return 'object'


def LiteralValues():
    return 'literal values'
