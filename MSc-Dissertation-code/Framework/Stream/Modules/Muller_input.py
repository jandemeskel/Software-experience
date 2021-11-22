
import numpy as np

class NMA:

    def __init__(self):
        pass

    @staticmethod
    def take_states():
        states = list(input("\n Enter all states, leaving a space between each and labelling them with Alphabetic characters only: ").strip().split())
        return states

    @staticmethod
    def take_initial():
             initial = list(input("\n Which of these are initial? : ").strip().split())
             return initial
    
    @staticmethod
    def take_accepting():
            accepting = input("\n Enter the collection of accepting sets as a nested array, Where each array is a seperate set, and each state within a set is seperated by the boolean operator or, '|'.  e.g. [[A|B], [C]] ").strip().split()
            return accepting

    @staticmethod
    def take_alphabet():
             alphabet = list(input("\n Numerically label and leaving a space between each letter , Enter all distinct letters within the alphabet : ").strip().split())
             return alphabet

    def FD_input(self):

       ################################################################ State inputs Error Handling ################################################################
        
        def all_states():

                states_temp = self.take_states()

                if len( states_temp) < 1:
                    print('No input detected, try again')
                    states_temp = all_states()
                    
                if  any((not i.isalpha()) for i in states_temp):
                    print("\n Entered input:", i,  "is invalid")
                    print (' Please label states using Alphabetic character(s) only, for instance " A B C"  or "One Two Three" corresponds to the first, second & third states ')
                    states_temp = all_states()
                    
                elif (len(states_temp) != len(set(states_temp))):
                    print("\n Entered input:", states_temp, " is invalid")
                    print (' Please ensure states do not have duplicate labels and  have a space between them, or instance " A B C"  or "One Two Three" corresponds to the first, second & third states ')
                    states_temp = all_states()
            
                return states_temp

        print("\n Type 'End' into the terminal at any stage to stop the programme")

        error_flag_all_states = True
        while error_flag_all_states:
            try: 
                states = all_states()
                error_flag_all_states = False
            except:
                print('invalid input, try again')
                states = 0

            if 'End' in states:
                    exit()
                
      ################################################################  Initial states Error Handling #################################################################

        def initial_states():

            get_initial = self.take_initial()

            if len(get_initial) < 1:
                print('No input detected, try again')
                get_initial = initial_states()

            if len(get_initial) > len(states):
                print("\n Entered input:", get_initial, " is invalid")
                print (' Number of initial states cannot exceed number of total states entered, try again')
                get_initial = initial_states()

            elif not all(elem in states for elem in get_initial):
                if (get_initial[0] == 'End'):
                    return get_initial
                else:
                    print("\n Entered input:", get_initial, " is invalid")
                    print (' Please choose an existing state from the set of states previously entered')
                    get_initial = initial_states()
            
            return get_initial

        error_flag_initial = True
        while error_flag_initial:
            try:
                initial = initial_states()
                error_flag_initial = False
            except:
                print('invalid input, try again')

        if 'End' in initial:
                exit()
                        
    ################################################################ accepting states Error Handling ################################################################

        def accepting_states():

            get_accepting = self.take_accepting()
            states_count = []

            if len(get_accepting) < 1:
                print('No input detected, try again')
                get_accepting = accepting_states()
            
            y = ''
            for elem in get_accepting:
                y = y + elem

            get_accepting = self.split_accepting_string(y)

            for elem in get_accepting:
                for state in elem:
                        if state == 'End':
                            return get_accepting
   
            for collection in get_accepting:
                for each_set in collection:
                    states_count.append(each_set)
            states_count = list(set(states_count))

            if type(collection) != type([]):
                print("\n Entered input:" , collection, ' is invalid')
                print(' Please enter accepting sets in the array format shown in the example above')
                get_accepting = accepting_states()
    
            if len(states_count) > len(states):
                print("\n Entered input:" , each_set, ' is invalid')
                print (' Number of accepting states cannot exceed number of total states entered, try again')
                get_accepting = accepting_states()

            for each_set in collection:
                if each_set not in states:
                    print("\n Entered input:", each_set, ' is invalid')
                    print (' Please choose an existing state from the set of states previously entered')
                    get_accepting = accepting_states()
                    break
                break

            return get_accepting

        error_flag_accepting = True
        while error_flag_accepting:
             try:
                accepting = accepting_states()
                error_flag_accepting = False
             except:
                 print('invalid input, try again')
                 accepting = 0

        for elem in accepting:
            if 'End' in elem: 
                exit()

        ################################################################ Alphabet input Error Handling ################################################################

        def compAlphabet():
        
            get_alphabet = self.take_alphabet()

            if len(get_alphabet) < 1:
                print('No input detected, try again')
                get_alphabet = compAlphabet()

            for elem in get_alphabet:
                if elem == 'End':
                    return get_alphabet
            if (any( not i.isdecimal() for i in get_alphabet)):
                print("\n Entered input:" , i, ' is invalid')
                print( ' Please follow the numerical labelling convention, for instance " 0 1" or "10 20" would correspond to two characters within the alphabet')
                get_alphabet = compAlphabet()
            return get_alphabet
        
        error_flag_alphabet = True 
        while error_flag_alphabet:
            try:
                alphabet = compAlphabet()
                error_flag_alphabet = False
            except: 
                print('invalid input, try again following Please follow the numerical labelling convention')
                alphabet = 0
        
        if 'End' in alphabet:
                 exit()
    
        ################################################################ transition input error handling ################################################################

        print(" \n Enter the transitions between states using the format [start state, [input characters], [end states]]. Type 'Stop' to continue")
        print(" For instance [A, [0|1], [A|B]] corresponds to state transitions from state A to B and C via computing 0 and 1 respectively : ")

        transition = []

        def take_transition():
            flag = True        
            while flag:

                x = input()

                if len(x) < 1:
                    print('No input detected, try again')
                    x = input()

                if x == 'End':
                    transition.append(x)

                elif x == 'Stop' and len(transition) == 0:
                    print('Please enter at least one valid transition of the format: [A, [0|1], [B|C]] corresponding to state transitions from state A to B and C via computing 0 and 1 respectively')
                    take_transition()

                elif x == 'Stop':
                    transition.append(x)
                
                else:
                    y = self.split_transition_string(x)

                    if (y[0] not in states):
                        print('Transition entered contains a start state not from the set of existing states, try again')
                        take_transition()
                        
                    elif [z for z in y[2] if z not in states] != []:
                        print('Transition entered contains an end state not from the set of existing states, try again')
                        take_transition()
                        
                    elif [z for z in y[1] if z not in alphabet] != [] :
                        print('Transition entered contains letters not from the existing computational alphabet, try again')
                        take_transition()
                        
                    elif len(y[2]) != len(y[1]):
                        print('Number of computed letters does not match the number of end states, try again')
                        take_transition()
                        
                    else:
                        transition.append(y)

                return transition
       
        error_flag_transition = True 
        while error_flag_transition:
            try:
                all_transitions = take_transition()

                if 'End' in all_transitions:
                    error_flag_transition = False

                elif 'Stop' in all_transitions:

                    all_transitions.pop()
                    reachable_states = []
                    for i in range(len(all_transitions) ):
                        reachable_states.append(all_transitions[i][0])

                        for k in range(len(all_transitions[i][2])):
                            reachable_states.append(all_transitions[i][2][k])
                        reachable_set = set(reachable_states)

                    error_flag_transition = False
      
            except: 
                print('invalid input, try again following Please follow the input array labelling convention')
        
        return states , initial, accepting, alphabet, all_transitions, reachable_set
    
        ################################################################ Print Formal Description to Terminal ################################################################

    def FD_print(self):
        
        states, initial, accepting, alphabet, transition, reachable = self.FD_input()
        subscript = 0

        print("........................................") 
        print(" Muller automaton Formal Description ")
        print("........................................") 
        
        print (" \n ............ Set of states ............")

        print("\n", sorted(states))
            
        print (" \n ............ Set of initial states ............")

        
        print("\n", sorted(initial))
        

        print (" \n ............ collection of sets satisfying acceptence condition ............ \n ")

        
        for elem in accepting:
            print('Accepting set F',subscript,':', elem)
            subscript += 1


        print (" \n ............ Computational alphabet ............")
        
        print("\n", sorted(alphabet))

        print (" \n ............ State transitions ............ \n")

        if len(transition) == 0:
            print('No valid transitions were entered')
        for i in range(len(transition)): 
             for k in range(len(transition[i][1])):
                 print(str(transition[i][0]) + " -------- " + str(transition[i][1][k]) + " --------> " + str(transition[i][2][k]))

        return states, initial, accepting, alphabet, transition

        ################################################################ Compute Formal description without any terminal printing ################################################################

    def construct_FD(self):

        states, initial, accepting, alphabet, transition = self.FD_print()

        return states, initial, accepting, alphabet, transition

        ################################################################ Handling Transition Array input ################################################################

    def split_transition_string(self, input):
        output = []
        split_commas = []
        remove_commas = input.replace(']','').replace('[','').split(',')

        for i in range(len(remove_commas)):
            spaces = remove_commas[i].strip()
            split_commas.append(spaces)
        
        output.append(split_commas[0])
        second_list = [] 
 
        for item in split_commas[1].split('|'):
            second_list.append(item)
 
        output.append(second_list)
 
        third_list = [] 
 
        for item in split_commas[2].split('|'):
            third_list.append(item)
 
        output.append(third_list)
 
        return output

    def split_accepting_string(self, input):
        collection_of_sets = []
        
        split_commas = []
        remove_commas = input.replace(']','').replace('[','').split(',')

        for i in range(len(remove_commas)):
            spaces = remove_commas[i].strip()
            split_commas.append(spaces)
        
        for elem in range(len(split_commas)):
                
                split_commas[elem] = split_commas[elem].split('|')
                collection_of_sets.append(split_commas[elem])

        return collection_of_sets




