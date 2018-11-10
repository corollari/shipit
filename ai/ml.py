# Create your first MLP in Keras
from keras.models import Sequential
from keras.layers import Dense
import numpy, json
# fix random seed for reproducibility
numpy.random.seed(7)


f = open("matlav", "r")
inp = json.loads(f.read())

f = open("matlov", "r")
outp = json.loads(f.read())

# load pima indians dataset
#dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
dataset=[range(9)] #TODO
dataset=numpy.array(dataset)
X = numpy.array(inp)#dataset[:,0:8]
Y = numpy.array(outp)#dataset[:,8]




# create model
model = Sequential()
model.add(Dense(128, input_dim=254, activation='relu')) #TODO
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='linear'))
# Compile model
model.compile(loss='mean_squared_error', optimizer='adam')
# Fit the model
model.fit(X, Y, epochs=1500, batch_size=10)

predictions = model.predict(X)

# evaluate the model
#scores = model.evaluate(X, Y)
#print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

print(model.predict(X))
