import numpy as np
import scipy.special as sci
import os
import sys



class neuralNetwork:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningRate) -> None:
        self.inodes = inputnodes
        self.onodes = outputnodes
        self.hnodes = hiddennodes
        self.lrate = learningRate

        self.AllC = 0.0
        self.CorC = 0.0

        self.wih = np.random.normal(0.0, pow(self.hnodes, -.5), (self.hnodes, self.inodes))
        self.who = np.random.normal(0.0, pow(self.onodes, -.5), (self.onodes, self.hnodes))
        #print(self.wih)
        #print(self.who)

        self.activation_function = lambda x: sci.expit(x)


    def train(self, inputs_list, targets_list):
        inputs = np.array(inputs_list, ndmin=2).T
        #print(inputs)

        targets = np.array(targets_list, ndmin=2).T 
        #print(targets)

        hidden_inputs = np.dot(self.wih, inputs)
        #print(hidden_inputs)

        hidden_outputs = self.activation_function(hidden_inputs)
        #print(hidden_outputs)

        final_inputs = np.dot(self.who, hidden_outputs)
        #print(final_inputs)

        final_outputs = self.activation_function(final_inputs)
        #print(final_outputs)

        self.AllC += 1.0
        if np.argmax(targets) == np.argmax(final_outputs):
            self.CorC += 1.0

        output_errors = targets - final_outputs
        #print(output_errors)

        hidden_errors = np.dot(self.who.T, output_errors)
        #print(hidden_errors)

        self.who += self.lrate * np.dot((output_errors * final_outputs *
                                        (1.0 - final_outputs)), np.transpose(hidden_outputs))

        self.wih += self.lrate * np.dot((hidden_errors * hidden_outputs * 
                                        (1.0 - hidden_outputs)), np.transpose(inputs))
        self.status()                                

    def status(self):
        os.system("clear")
        print("All : {0}        Correct : {1}           {2}".
                                format(self.AllC, self.CorC, self.CorC/self.AllC*100.0))

    def snapshot(self, filename):
        np.savez(filename, inn=self.inodes, outn=self.onodes, hidn=self.hnodes, wih=self.wih, who=self.who)
        


    def query(self, input_list):
        inputs = np.array(input_list, ndmin=2).T

        hidden_inputs = np.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = np.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        return final_outputs


input_nodes = 11
hidden_nodes = 8
output_nodes = 2
learning_rate = 0.1



n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
training_mnist_file = open("csgo.csv")
training_data_list = training_mnist_file.readlines()
training_mnist_file.close()
print(len(training_data_list))

# CT 0
# T 1


cron_list = [175, 33, 33, 500, 500, 500, 500, 5, 5, 5, 5]

allin = len(training_data_list)
prog = 0
for _ in range(1):
    for record in training_data_list:
        all_values = record.split(',')
        inputs = np.array([(float(all_values[x]) / cron_list[x] * 0.99 + 0.01) for x in range(11)])
        targets = np.zeros(output_nodes) + 0.01
        if all_values[11] == "CT":
            targets[0] = 0.99
        else:
            targets[1] = 0.99  
        n.train(inputs, targets)
        prog += 1
        per = prog / allin * 100
        print("Progress: {}".format(round(per))) 
    
n.snapshot("file")

# test_data_file = open("IRIS.csv", 'r')
# test_data_list = test_data_file.readlines()
# test_data_file.close()

# aans = len(test_data_list)
# cans = 0
# wans = []
# wan = []

# for strl in test_data_list:
#     all_val = strl.split(',')
#     can = all_val[4]
#     an = np.argmax(n.query((np.asfarray(all_val[:4]) / 10.0 * 0.99) + 0.01))
#     print("{0}   {1}".format(can, an))
#     if can==str(an):
#         cans += 1



# print("{}".format(round(cans/aans*100, 4)))

