# Example of forward propagating input
from math import exp

# Calculate neuron activation for an input
def activate(weights, inputs):
	#print(inputs)
	activation = weights[-1]
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]
		#print(activation)
	return activation

# Transfer neuron activation
def transfer(activation):
    p= 1.0 / (1.0 + exp(-activation))
    #print(p)
    return 1.0 / (1.0 + exp(-activation))

# Forward propagate input to a network output
def forward_propagate(network, row):
    inputs = row
    for layer in network:

        new_inputs = []
        for neuron in layer:
            #print(neuron)
            activation = activate(neuron['weights'], inputs)
            neuron['output'] = transfer(activation)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs

# test forward propagation
network = [[{'weights': [0.13436424411240122, 0.8474337369372327, 0.32456985672351673, 0.763774618976614]},{'weights': [0.13436424411240122, 0.8474337369372327, 0.32456985672351673, 0.763774618976614]},{'weights': [0.2550690257394217, 0.49543508709194095, 0.4494910647887381, 0.651592972722763]}],
[{'weights': [0.13436424411240122, 0.8474337369372327, 0.32456985672351673, 0.763774618976614]},{'weights': [0.13436424411240122, 0.8474337369372327, 0.32456985672351673, 0.763774618976614]}],
		[{'weights': [0.2550690257394217, 0.49543508709194095, 0.651592972722763]},{'weights': [0.2550690257394217, 0.49543508709194095,0.651592972722763]}]]
row = [1, 0, 1, None]
output = forward_propagate(network, row)
print(output)
