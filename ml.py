

# Create your first MLP in Keras
from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
numpy.random.seed(7)




# load pima indians dataset
#dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
dataset=[range(9)] #TODO
dataset=numpy.array(dataset)
X = dataset[:,0:8]
Y = dataset[:,8]




# create model
model = Sequential()
model.add(Dense(128, input_dim=254, activation='relu')) #TODO
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='tanh'))
# Compile model
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, epochs=150, batch_size=10)

predictions = model.predict(X)

# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
