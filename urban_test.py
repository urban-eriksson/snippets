import pandas as pd
from cerberus import Validator
import json

config = {
    'metadata' : {
        'name': 'Urban test',
        'type': 'filter',
        'version': '0.0.2',
        'gui_version': '4',
        'permanent': False,
        'author': 'Validio'
        },
    'requirements': ['pandas==0.24.1'],
    'outputs': [{ 
            'key': 'multiplieddata',
            'name': 'Multiplied data points',
            'alertable': True
            },],
    'wizard': {
        'steps' : [
            {   'label': 'Define data input',
                'elements': [ {
                        'type': 'heading2',
                        'label': 'Datainput'
                        },
                           {
                        'type': 'datainput',
                        'key' : 'production_data',
                        },
                             ]},
            {   'label': 'Define multiplier',
                'elements': [ {
                        'type': 'heading2',
                        'label': 'Input multiplier'
                        },
                           {
                        'type': 'input',
                        'key' : 'multiplier',
                        'label': 'Input multiplier'
                        },
                             ]},
        ]},
    'visualizations': []
    }

def get_schemas(input_schemas, args):
    output_schema = [{'name': 'multipliedvalue', 'type': 'number'}]
    return {'multiplieddata': output_schema}

def execute(inputdata, localdata, args):

    if not 'production_data' in inputdata:
        return {}

    multiplier = args['multiplier'] 
    df = inputdata['production_data']
    df = pd.DataFrame( [[float(multiplier) * df['VolatileAcidity'].values[0]]], columns=['multipliedvalue'])

    outputdata = {'multiplieddata': df}

    return outputdata

