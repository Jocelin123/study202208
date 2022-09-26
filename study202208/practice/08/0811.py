import json

# data={
#     'a1':1,
#     'b1':'哈哈',
#     'c1':True,
#     'd1':False,
#     'e1':None
# }
# print(json.dumps(data,ensure_ascii=False,indent=4))
# with open('data.json','w') as f:
#     json.dump(data,f)

# j2 = '''{"a": 1, "b": ["2", "3"], "c": true, "d": false, "e": null}'''
# json.loads(j2)
# with open('data.json','r') as f:
#     print(json.load(f))
import sys

print(sys.version_info>(3,6))