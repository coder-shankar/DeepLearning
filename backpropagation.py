from random import seed
from random import random
import math

#steps
#initialize network
#forward propagation
#back propagation for error
#Train network
#predict


#initialize network
def init_network(n_inputs,n_hidden,n_output):
    network = list()
    hidden_layer = [{'weights':[random() for i in range(n_inputs+1)]} for i in range(n_hidden)]
    network.append(hidden_layer)
    output_layer = [{'weights':[random() for i in range(n_hidden+1)]} for i in range(n_output)]
    network.append(output_layer)
    return network


#forward propagation
#activation function

def activation(weights,inputs):
    #last weight is for bias
    activation = weights[-1]
    for i in range(len(weights)-1):
        activation += weights[i]*inputs[i]
    return activation

#neuron output
def neuron_output (activation):
    return 1.0/(1.0 + math.exp(-activation))

#forward propagate through network

def forward_propagate(newtwork ,input_row):
    inputs = input_row
    for layers in newtwork:
        new_inputs = []
        for neuron in layers:
            activations = activation(neuron['weights'],inputs)
            neuron['output'] = neuron_output(activations)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs



#Backpropagation


    



# test forward propagation
network = init_network(2,4,2)
row = [1, 0, None]
output = forward_propagate(network, row)
print(output)
