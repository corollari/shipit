# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
import json

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

import collections



with open('data/n2', 'r') as f:
    distros_dict = json.load(f)

data=distros_dict
final=[]

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
#print(common)
print( data[0]['input']['description'])
#________________________________________________________________________________________
langs = ['CoffeeScript', 'Lex', 'Forth', 'Assembly', 'Agda', 'Yacc', 'CSS', 'Parrot', 'prolog', 'OCaml', 'ColdFusion', 'M4', 'RenderScript', 'JSON', 'C', 'Isabelle', 'Smalltalk', 'Roff', 'Java', 'Haskell', 'HTML', 'Python', 'Groovy', 'JavaScript', 'Shell', None, 'Others']

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

#print(common)
print( data[0]['input']['language'])

print(len(langs))
#________________________________________________________________________________________
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
#print(common)
print(data[0]['input']['topics'])

#________________________________________________________________________________________

for j in range(len( data)):
    f=[0]*len(langs)
    v = data[j]['input']['experiencelgs']
    for w in v:
        if w in langs:
            f[langs.index(w)] = v[w]

    data[j]['input']['experiencelgs']=f

#print(common)
print(data[0]['input']['experiencelgs'])

matlav=[]
y=len(data)
for i in range(len(data)):
    matlav.append(data[i]['input']['language']+data[i]['input']['description']+data[i]['input']['topics']+data[i]['input']['experiencelgs'])

print(len(matlav[0]))
matlov=[ ]
for out in range(len(data)):
    matlov.append(data[out]['output'])

print(matlov[0])

open('matlav', 'w+').write(json.dumps(matlav))
open('matlov', 'w+').write(json.dumps(matlov))
