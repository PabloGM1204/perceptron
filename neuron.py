import math
import numpy as np

class Neuron:
    def __init__(self, weights, bias, fun):
        self.weights = weights
        self.bias = bias
        self.fun = fun
    
    def run(self, input_data):
        weighted_sum = np.sum(np.array(self.weights) * np.array(input_data)) + self.bias
        if self.fun == "ReLU":
            return max(0, weighted_sum)
        elif self.fun == "Sigmoide":
            return 1 / (1 + math.exp(-weighted_sum))
        elif self.fun == "Tangente hiperbólica":
            return math.tanh(weighted_sum)
        elif self.fun == "Linear":
            return weighted_sum
        else:
            raise ValueError("Invalid activation function")

    def changeBias(self, new_bias):
        self.bias = new_bias