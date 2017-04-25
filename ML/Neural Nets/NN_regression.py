from enum import *
from math import *
import matplotlib.pyplot as plt
from numpy import *
from random import *
import pdb
import sys


def info(type, value, tb):
   if hasattr(sys, 'ps1') or not sys.stderr.isatty():
      # we are in interactive mode or we don't have a tty-like
      # device, so we call the default hook
      sys.__excepthook__(type, value, tb)
   else:
      import traceback, pdb
      # we are NOT in interactive mode, print the exception...
      traceback.print_exception(type, value, tb)
      print
      # ...then start the debugger in post-mortem mode.
      pdb.pm()

sys.excepthook = info

class ActivationType(Enum):
    linear = 1
    logistic = 2
    tanh = 3

class NeuronType(Enum):
    bias = 1
    input = 2
    regular = 3
    output = 4
    
class Neuron:
    def __init__(self, neuron_type, weights = None, activation_type = None):
        self.neuron_type = neuron_type
        if self.neuron_type == NeuronType.input:
            self.weights = [1]
            self.activation_type = ActivationType.linear
        elif self.neuron_type == NeuronType.regular or self.neuron_type == NeuronType.output:
            self.weights = weights
            self.activation_type = activation_type
            
        self.derivative = 0
        self.output = 0
        
    def Sigmoid(self,x):
        return 1/(1+exp(-x))

    def Tanh(self,x):
        return math.tanh(x)
        
    def Output(self,inputs=None):
        if self.neuron_type == NeuronType.bias:
            self.output = 1
            self.derivative = 0
        elif self.neuron_type == NeuronType.input or self.neuron_type == NeuronType.regular:
            if self.activation_type == ActivationType.linear:
                self.output = dot(self.weights,inputs)
                self.derivative = 1
            elif self.activation_type == ActivationType.logistic:
                self.output = self.Sigmoid(dot(self.weights,inputs))
                self.derivative = self.output * (1 - self.output)
        else:
            if self.activation_type == ActivationType.linear:
                self.output = dot(self.weights,inputs)
                self.derivative = 1
            else:
                self.s = self.Sigmoid(dot(self.weights,inputs))
                self.output = round(self.s)
                self.derivative = self.s * (1-self.s)

        return self.output
    
    def UpdateWeights(self, dw):
        for i, w in enumerate(self.weights):
            self.weights[i] += dw[i]

class LayerType(Enum):
    input_layer = 1
    output_layer = 2
    
class NeuronLayer:
    def __init__(self, num_neurons, num_inputs, layer_type, activation_type=None):
        self.layer_type = layer_type
        
        if layer_type == LayerType.input_layer:
            self.neurons = [Neuron(NeuronType.bias)]
            self.neurons += [Neuron(NeuronType.input) for i in range(1,num_neurons)]
        elif layer_type == LayerType.hidden_layer:
            self.neurons = [Neuron(NeuronType.bias)]
            self.neurons += [Neuron(NeuronType.regular, [uniform(-.1,.1) for j in range(0,num_inputs)], activation_type) for i in range(1,num_neurons)]
        else:
            self.neurons = [Neuron(NeuronType.output, [uniform(-.1,.1) for j in range(0,num_inputs)], activation_type) for i in range(num_neurons)]
    
    def Outputs(self, inputs):
        if self.layer_type == LayerType.input_layer:
            return [self.neurons[0].Output()] + [n.Output([inputs[i]]) for i,n in enumerate(self.neurons[1:])]
        else:
            return [n.Output(inputs) for n in self.neurons]


class ProblemType(Enum):
    regression = 1
    classification = 2

class NeuralNet:
    def __init__(self, num_inputs, num_hidden_layers, num_hidden_neurons,num_output_neurons,alpha,problem_type):
        self.problem_type = problem_type
        if problem_type == ProblemType.regression:
            self.activation_type = ActivationType.linear
        else:
            self.activation_type = ActivationType.logistic
        self.layers = [NeuronLayer(num_inputs+1, 1, LayerType.input_layer)]
        self.layers += [NeuronLayer(num_hidden_neurons+1, num_inputs + 1 if i == 0 else num_hidden_neurons + 1, LayerType.hidden_layer, self.activation_type) for i in range(0,num_hidden_layers)]
        self.layers += [NeuronLayer(num_output_neurons, num_hidden_neurons+1, LayerType.output_layer, self.activation_type)]
        
        self.outputs = [[0]*(num_inputs+1)]
        self.outputs += [[0]*(num_hidden_neurons+1) for i in range(0,num_hidden_layers)]
        self.outputs += [[0]*num_output_neurons]
        
        self.alpha = alpha

    def FeedForward(self, inputs):
##        print(inputs)
        self.outputs[0] = self.layers[0].Outputs(inputs)
##        pdb.set_trace()
        for i,layer in enumerate(self.layers[1:],1):
            self.outputs[i] = layer.Outputs(self.outputs[i-1])
            
        return self.outputs[-1]

    def GradientDescent(self,predicted_output,target_output):
		
    def TrainExample(self, example, target_output):
##        pdb.set_trace()
        try:
            example = list(example)
        except TypeError:
            example = [example]

        try:
            target_output = list(target_output)
        except TypeError:
            target_output = [target_output]
##            
        predicted_output = self.FeedForward(example)
        self.GradientDescent(predicted_output, target_output)
        return predicted_output

    def NormalizeInputs(self,inputs):
        sums = [sum([abs(inputs[i][j]) for i in range(len(inputs))]) for j in range(len(inputs[0]))]
        return [[inputs[i][j]/sums[j] for j in range(len(inputs[0]))] for i in range(len(inputs))]

    def Train(self, training_examples, actual_outputs):
        i = 0

        normalized_training_examples = self.NormalizeInputs(training_examples)

        rmse = float('inf')
        prev_rmse = -float('inf')
        self.errors = []
        self.vals = []
        while i == 0 or abs(rmse - prev_rmse) > 0.000001:
            errors = []
            for j in range(0,len(normalized_training_examples)):
                example = normalized_training_examples[j]
                actual_output = actual_outputs[j]
##                print(i,j,actual_output)
                predicted_output = self.TrainExample(example, actual_output)
##                print(i,j,actual_output, predicted_output)
                errors.append(sum([(predicted_output[i] - actual_output[i])**2 for i in range(len(predicted_output))]))
                #print('\t',example,actual_output, predicted_output)
            prev_rmse = rmse
            rmse = sqrt(sum(errors)/len(errors))
            print(i, rmse)
            self.errors.append(rmse)
            i += 1

    def Test(self,test_examples,outputs):
        n_correct = 0
        for i in range(len(test_examples)):
            predicted_output = self.FeedForward(test_examples[i])
            n_correct += predicted_output == outputs[i]

        return n_correct/len(test_examples)


def Test():
    global N,x,S
    x = [[x] for x in list(arange(-1,1,0.1))]
    S = sin(x).tolist()
    alpha = .1
    N = NeuralNet(len(x[0]),1,100,len(S[0]),alpha)
    N.Train(x,S)


import atexit
@atexit.register
def goodbye():
    y = N.errors
    plt.plot(arange(len(y)),y)
    plt.show()
    plt.plot(x,S)
    plt.plot(x,[N.FeedForward(i) for i in x])
    plt.show()

    input()

if __name__ == "__main__":
    Test()