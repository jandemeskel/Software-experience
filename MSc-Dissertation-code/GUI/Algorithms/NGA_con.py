import copy as c
import Terminal_programme.NGA_conversion as NGA_c

class NGA_construct():
    def __init__(self):
        pass

    def flatten(self,arr):
        arr = [i for j in arr for i in j]
        return arr    

    def muller_to_NGA(self, muller):
        states = muller[0]
        initial = muller[1]
        alphabet = muller[2]
        transitions = muller[3]
        accepting = muller[4]

  

        states_copy = c.deepcopy(states)
        initial_copy = c.deepcopy(initial)
        accepting_copy = c.deepcopy(alphabet)
        transition_copy = c.deepcopy(transitions)
        
        NGAs = []

        for set_ac in accepting:
            
            automaton = NGA_c.NGA(states, initial, set_ac, alphabet, transitions).construct_NGAs()
            NGAs.append(automaton)
            automaton = []
            states, initial, alphabet, transitions = states_copy, initial_copy, accepting_copy, transition_copy

        NGAs = self.flatten(NGAs)

        return NGAs
        