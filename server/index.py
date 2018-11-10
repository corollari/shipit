from flask import Flask, send_from_directory
import json, requests, collections
from keras.models import model_from_json
import numpy

app = Flask(__name__)

#headers = {'Authorization': 'token TOKEN'}
#headerTopic = {'Authorization': 'token TOKEN', 'Accept': 'application/vnd.github.mercy-preview+json'}
langs = ['CoffeeScript', 'Lex', 'Forth', 'Assembly', 'Agda', 'Yacc', 'CSS', 'Parrot', 'prolog', 'OCaml', 'ColdFusion', 'M4', 'RenderScript', 'JSON', 'C', 'Isabelle', 'Smalltalk', 'Roff', 'Java', 'Haskell', 'HTML', 'Python', 'Groovy', 'JavaScript', 'Shell', None, 'Others']

@app.route('/<path:path>')
def h(path):
    return send_from_directory('frontend', path)

@app.route('/')
def files():
    return send_from_directory('frontend', "index.html")

@app.route('/api/<username>/<repo>')
def hello_world(username, repo):
    json_data = requests.get('https://api.github.com/repos/'+username+'/'+repo) #, headers=headers)

    data = json.loads(json_data.content)
    project = data['full_name']
    language=data['language']
    description=data['description']

    json_data = requests.get('https://api.github.com/repos/'+username+'/'+repo+'/topics') #, headers=headerTopic)
    topics = json.loads(json_data.content)

    json_data = requests.get('https://api.github.com/users/'+username+'/repos', params={'per_page':100}) #, headers=headers)
    data = json.loads(json_data.content)
    print(data)
    userlgs=dict(zip(langs, [0]*len(langs)))
    for d in data:
        if d.get('language') in userlgs:
            userlgs[d.get('language')] += 1
        else:
            userlgs['Others'] += 1
    data={}
    data={'input':{'language':language, 'description':description, 'topics':topics, 'experiencelgs':userlgs}}

    final=[]
    data = [data]
    #print(ascii(distros_dict[0]['input']))
    a=[]
    for k in data:
        a+=ascii(k['input']['description']).split()
    #print(a)
    common=list(map( lambda x:x[0], collections.Counter(a).most_common(100)))
    for j in range(len( data)):
        f=[0]*100
        for i, k in enumerate(common):
            if k in (ascii(data[j]['input']['description'])).split():
                f[i]=1
        data[j]['input']['description']=f

    a=[]
    for k in data:
        a+=ascii(k['input']['language'])

    #print(a)
    common=a#list(map( lambda x:x[0], collections.Counter(a).most_common(100)))
    for j in range(len( data)):
        f=[0]*len(langs)
        l=data[j]['input']['language']
        if l in langs:
            f[langs.index(l)]=1
        else:
            f[len(langs)-1]=1
        data[j]['input']['language']=f

    a=[]
    for k in data:
        a+=(k['input']['topics'])

    common=list(map( lambda x:x[0], collections.Counter(a).most_common(50)))
    for j in range(len( data)):
        f=[0]*100
        for i, k in enumerate(common):
            if k in (data[j]['input']['topics']):
                f[i]=1
        data[j]['input']['topics']=f

    a=[]
    for k in data:
        a+=(k['input']['topics'])

    common=list(map( lambda x:x[0], collections.Counter(a).most_common(50)))
    for j in range(len( data)):
        f=[0]*100
        for i, k in enumerate(common):
            if k in (data[j]['input']['topics']):
                f[i]=1
        data[j]['input']['topics']=f

    for j in range(len( data)):
        f=[0]*len(langs)
        v = data[j]['input']['experiencelgs']
        for w in v:
            if w in langs:
                f[langs.index(w)] = v[w]

        data[j]['input']['experiencelgs']=f

    matlav=[]
    y=len(data)
    for i in range(len(data)):
        matlav.append(data[i]['input']['language']+data[i]['input']['description']+data[i]['input']['topics']+data[i]['input']['experiencelgs'])
    print(matlav)
    


    return str(model.predict(numpy.array(matlav))[0][0])

model = model_from_json(open("../ai/model.json", "r").read())
model.load_weights("../ai/weights.hdf5", by_name=False)
model._make_predict_function() # Fix Keras bug
