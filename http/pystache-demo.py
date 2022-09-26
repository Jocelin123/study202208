import pystache

t = open("t.txt", "rb")
f = pystache.render(
    t.read(),
    {'name':'zj'}
)
print(f)
print('DONE!')

c={
    "header":"Colors",
    "items":[
        {"name":"red","first":True,"url":"#Red"},
        {"name":"green","link":True,"url":"#Green"},
        {"name":"blue","link":True,"url":"#Blue"}
    ],
    "empty":False
}

c2 = {
  "header": "Colors2222",
  "items": [
      {"name": "red2222", "first": True, "url": "#Red"},
      {"name": "green2222", "link": True, "url": "#Green"},
      {"name": "blue2222", "link": True, "url": "#Blue"}
  ],
  "empty": False
}
r=pystache.Renderer()
f=r.render_name("ttt",c)
print(f)
print("DONE!")
t=open("ttt.txt","rb")
f=pystache.render(t.read(),c2)
print(f)
print("DONE!")
