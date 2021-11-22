import Muller_input as input
import NGA_conversion as convertNGA
import NBA_conversion as convertNBA
import Regular_operations as regops
import copy as c



Example_Input = input.NMA().FD_print()

# Example_NGA = convertNGA.NGA().construct_NGAs()



# def comp(NGA):

#     complement = []

#     # manipulate NGA array to perform the complement algorithm

#     return complement


# NGA_complement = comp(Example_NGA)









# def flatten(arr):
#     arr = [i for j in arr for i in j]
#     return arr    

# states = ['A','B','C']
# initial = ['A']
# accepting = [['A','B']]
# alphabet = ['0', '1']
# transition = [['A', ['0', '1'], ['A', 'B']], ['B', ['0', '1'], ['A', 'B']]]


# states_copy = c.deepcopy(states)
# initial_copy = c.deepcopy(initial)
# accepting_copy = c.deepcopy(alphabet)
# transition_copy = c.deepcopy(transition)

# NGAs = []

# for set_ac in accepting:

#     automaton = convertNGA.NGA(states, initial, set_ac, alphabet, transition).NGA_print()
#     NGAs.append(automaton)
#     automaton = []
#     states, initial, alphabet, transition = states_copy, initial_copy, accepting_copy, transition_copy



























# Example_Input = input.NMA().construct_FD()

# Example_NGA = convertNGA.NGA().construct_NGAs()



# def comp(NGA):

#     complement = []

#     # manipulate NGA array to perform the complement algorithm

#     return complement


# NGA_complement = comp(Example_NGA)

# Muller_input = input.NMA().FD_print()

# states = Muller_input[0]
# initial = Muller_input[1]
# alphabet = Muller_input[2]
# transitions = Muller_input[3]
# accepting = Muller_input[4]

# generalised_Buchi = convertNGA.NGA(states,initial,alphabet,transitions,accepting).construct_NGAs()
# # Example call on NGA conversion algorithm




# #Input with different dimensions to test NBA conversion and regular operations
# Example_NGA = [[  [('q', 0), ('r', 0), ('p',0) ],   [('q', 0)],   [0, 1],  
# [ [('q', 0),[1, 0], [('q', 0), ('r', 0)]], 
# [('r', 0),[0, 1], [('r', 0), ('q', 0)]]],   
# [[('q', 0)],[('r', 0)],]]]





# def flatten(arr):
#     arr = [i for j in arr for i in j]
#     return arr    

# states = ['A','B','C']
# initial = ['A']
# accepting = [['A','B']]
# alphabet = ['0', '1']
# transition = [['A', ['0', '1'], ['A', 'B']], ['B', ['0', '1'], ['A', 'B']]]


# states_copy = c.deepcopy(states)
# initial_copy = c.deepcopy(initial)
# accepting_copy = c.deepcopy(alphabet)
# transition_copy = c.deepcopy(transition)

# NGAs = []

# for set_ac in accepting:

#     automaton = NGA_c.NGA(states, initial, set_ac, alphabet, transition).construct_NGAs()
#     NGAs.append(automaton)
#     automaton = []
#     states, initial, alphabet, transition = states_copy, initial_copy, accepting_copy, transition_copy



# Example_union = regops.Union(NGAs).union_print()

    
# Example_intersection = regops.Intersection(NGAs).intersection_print()
    







# Example test for Muller -> NGA (from textbook):
# Q = A B
# I = A
# AC = [A|B]
# E = 0 1
# T1 = [A, [ 0 | 1], [A | B]]
# T2 = [B, [ 0 | 1], [A | B]]


# Example_NGAs an array holding the non-determinisitic buchi automatas for each set of acceptance conditions within the collection of acceptance.
# i.e.  F = {{F0}, {F1}, ... , {Fi}} Muller condition, collection of sets
# Each set has an equivalent NGA
# And each NGA a number of NBAs equivalent to the elements within that set





# E.g. F = {{F0}, {F1}} => This muller ac would have at least 2 NGAs as both sets are not empty hence the smallest number of AC containing states is 2
# if {F0} = {A,B} => 2 NBAs which are then turned into one by taking the disjoint union
# if {F1} = {C} => Singleton AC in the set hence this NGA is satisfies the condition of a NBA, no further conversion.
# 

