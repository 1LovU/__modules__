# Module which takes json or xml string , parse it to python Dict object.
# returns empty dict, if its invalid data type or invalid xml or json format.
# Make sure you have all the modules installed.
# Author :: Amit Yadav


import json
import xmltodict


def xml_json_parse(string):
    simple_dict = dict()
    if type(string) != str:
        print('ERROR :: "Not A valid data type, please pass a string." ')
        print(f'Object type :: "{type(string)}" ')
        return simple_dict

    try:
        simple_dict = json.loads(string)
        # Need to change to dict if its just one value. ( maybe string or integer )
        if type(simple_dict) != dict:
            value = simple_dict
            simple_dict = dict()
            simple_dict[value] = value


    except:
        # comes here if the string is not a valid json string.
        try:
            simple_dict = xmltodict.parse(string)
            # Need to change to dict if its just one value. ( maybe string or integer )
            
            if type(simple_dict) != dict:
                value = simple_dict
                simple_dict = dict()
                simple_dict[value] = value
        except:
            # if neither json or xml string.
            print('ERROR :: "Not a valid xml or json string." ')

    return simple_dict






