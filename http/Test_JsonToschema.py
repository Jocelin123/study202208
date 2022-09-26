import json
import logging
import jsonschema
import requests

class JsonToSchema:
    @classmethod
    def get_object_data(cls,dict_data):
        schema_data={}
        for dict_data_k in dict_data.keys():
            if type(dict_data[dict_data_k]) in (str,int,bool,float,list):
                if type(dict_data[dict_data_k]) is str:
                    schema_data[dict_data_k]={"type":"string"}
                    continue
                if type(dict_data[dict_data_k]) is int:
                    schema_data[dict_data_k] = {"type": "integer"}
                    continue
                if type(dict_data[dict_data_k]) is bool:
                    schema_data[dict_data_k] = {"type": "boolean"}
                    continue
                if type(dict_data[dict_data_k]) is float:
                    schema_data[dict_data_k] = {"type": "number"}
                    continue
                if type(dict_data[dict_data_k]) is list:
                    data={}
                    # j=0
                    # for i in dict_data[dict_data_k]:
                    #         data[j]=i
                    #         j=j+1
                    print(dict_data[dict_data_k])
                    for k,v in dict_data[dict_data_k]:
                        data[k]=v
                    # dict(dict_data)
                    print(data)
                    # schema_temp = {"type": "array", 'item': cls.get_schema(dict_data[dict_data_k])}
                    # schema_data[dict_data_k] = schema_temp
                    schema_data[dict_data_k] = {"type": "array"}
                    continue
            if dict_data[dict_data_k] is None:
                schema_data[dict_data_k] = {"type": "null"}
                continue
            elif type(dict_data[dict_data_k]) == dict:
                schema_temp={"type":"object",'properties':cls.get_object_data(dict_data[dict_data_k])}
                schema_data[dict_data_k]=schema_temp
            else:
                print(dict_data[dict_data_k]==None)
        return schema_data

    def get_schema(self,data):
        return {"type":"object","properties":JsonToSchema.get_object_data(data)}

if __name__ == '__main__':
    # url = "https://ceshiren.com/categories.json"
    url="https://testerhome.com/api/v3/topics.json"
    data = requests.get(url,params={'limit':'100'}).json()
    print(data)
    schema=JsonToSchema().get_schema(data)
    print(schema)
    jsonschema.validate(data,schema)
    print('end')