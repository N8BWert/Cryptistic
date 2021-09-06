from random import random

class cryptnet:
    #   Shape of neural network is 1 * 500 * 500 * 500 * 1
    #   Layer 0 : Input Layer, Layer 1 : Hidden Layer 1, Layer 2 : Hidden Layer 2, Layer 3 : Hidden Layer 3, Layer 4 : Output Layer
    #   All weights and biases, except 1 weight are considered free variables.  The final weight is determined based on the values of the free variables
    #   This network is meant to be randomly created upon instantiation.
    #   The decision bounds of this netowork are linear with a number on the order of 2^500 ish redirections to make cracking difficult

    #   biases[i] => bias at neuron i (0 : input, 1 : neuron 1 of hidden layer 1, 501 : neuron 1 of hidden layer 2, 1001 : neuron 1 of hidden layer 3, 1501 : output neuron)
    biases = []

    #   weights[i][j] => weight at neuron i coming from neuron j of the past layer
    #   weights[1][0] => weight at neuron 1 (1st layer neuron 1) coming from neuron 0 (input neuron)
    #   weights[501][25] => weight at neuron 501 (2nd layer neuron 1) coming from neuron 25 of previous layer (neuron 25)
    #   weights[1003][290] => weight at neuron 1003 (3rd layer neuron 3) coming from neuron 290 of previous layer (neuron 790)
    weights = []

    #   a => minvalue, b => maxvalue
    a = 505050505050505050505050505050505050505050505050505050505050505
    b = 9999999999999999999999999999999999999999999999999999999999999999

    #   max_yield => maximum value passed out of an activation function
    max_yield = 0

    def __init__(self):
        self.biases = self.populate_biases()
        self.weights = self.populate_weights()

        
    def populate_biases(self):
        #   1502 random biases are generated (the bias position 0 does not matter and would only be used if the input node was considered a hidden neuron with an activation function)
        biases = []
        for i in range(0, 1502):
            biases.append(random.uniform(float('-inf'), float('inf')))
        return biases

    def populate_weights(self):
        #   Random weights are generated for the 1502 nodes.  The weight associated with i = 0 can be ignored as it is for the input node, if it were considered a hidden neuron
        weights = [None] * (1502)
        for i in range(len(weights)):
            outgoing_weights = []
            if i == 0:
                #   Leaves the spot associated with i = 0 blank
                continue
            elif i > 0 and i < 501:
                #   Choose a weight 
                if self.biases[i] >= 0:
                    outgoing_weights[0] = random.uniform(float((1 - self.biases[i]) / self.b), float(10 ** 100 - self.biases[i] - self.b))
                else:
                    outgoing_weights[0] = random.uniform(float((1 - self.biases[i]) / self.a), float(10 ** 100 - self.biases[i] - self.a))
                if bool(random.getrandbits(1)):
                    outgoing_weights[0] = 0
            elif i > 500 and i < 1501:
                for i in range(0, 499):
                    outgoing_weights.append(random.uniform(float('-inf'), float('inf')))
                upper_bound = self.max_yield - self.biases[i]
                for weight in outgoing_weights:
                    upper_bound -= weight
                lower_bound = (1 - self.biases[i]) / self.max_yield
                for weight in outgoing_weights:
                    lower_bound -= weight
                outgoing_weights.append(random.uniform(lower_bound, upper_bound))
            else:
                for i in range(0, 499):
                    outgoing_weights.append(random.uniform(float('-inf'), float('inf')))
                upper_bound = self.b - self.biases[i]
                for weight in outgoing_weights:
                    upper_bound -= weight
                lower_bound = (self.a - self.biases[i]) / self.b
                for weight in outgoing_weights:
                    lower_bound -= weight
                outgoing_weights.append(random.uniform(lower_bound, upper_bound))
            weights[i] = outgoing_weights
        return weights