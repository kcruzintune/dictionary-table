# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pylab as plt

def build_dictionary(list1):
    
    '''Function that takes as input a list of 
    strings. This will return a dictionary whose keys are 
    every word that occurs in the list, and whose values are the frequency of 
    each word in the list.'''
    
    dict1 = {}
    
    for keys in list1:    
        if keys in dict1:
            dict1[keys] = dict1[keys] + 1
        else:
            dict1[keys] = 1
            
    return dict1
   

def frequency_table(string):
    
    '''Function that takes as input a string, and returns the word frequencies 
    in that string, sorted by words.''' 
    
    contain = ''
    
    string = string.split()
    string = sorted(string)
    string_dict = build_dictionary(string)
    
    for name, value in string_dict.items():
        contain += name + ": " + str(value) + '\n'
        
    return contain

def table(string2):
    
    '''similar to build_dictionary()'''
    
    string2 = sorted(string2.split())
    
    dict1 = build_dictionary(string2)
    
    return (dict1)
    
    
def plot_frequency_graph(string2):
    
    '''Function plot_frequency_graph() that takes the same input 
    (string of words) and prints a bar chart of the word frequencies.'''
    
    dict1 = table(string2)
    
    x = list(dict1.keys())
   
    y = list(dict1.values())
    
    plt.title("Plot Frequency Graph By Kevin Cruz")
    plt.bar(range(len(dict1)), y, tick_label=x)
    plt.show()

    