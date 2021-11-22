import copy as c

class NGA():
    
    def __init__(self, current_states, initial, accepting, alphabet, transition):

        self.current_states = current_states
        self.initial = initial
        self.accepting = accepting
        self.alphabet = alphabet
        self.transition = transition

# Add indexes to accepting, initial and all states variables and those within the transition arrays
    def state_index(self):

        states = []

        for element in self.current_states:
            states.append((element, 0))
            states.append((element, 1))

        return states
    
    def accepting_index(self):

        for i in range(len(self.accepting)):
            self.accepting[i] = (self.accepting[i],0)
        return self.accepting
    
    def initial_index(self):
        for elem in range(len(self.initial)):
            self.initial[elem] = (self.initial[elem], 0)
        
        return self.initial
    
    def transition_index(self):

        for each_transition in self.transition:
            
            each_transition[0] = (each_transition[0], 0)
            for i in range(len(each_transition[2])):

                each_transition[2][i] = (each_transition[2][i], 0)
                
        return self.transition
    
    
# Construct transitions representing infinite cycles for a given AC, and add to transition array
    def construct_loops(self):

        self.accepting = self.accepting_index()
        self.transition = self.transition_index()

        state_loops = []
        each_ac_transitions = []
        all_ac_transitions = []

        infinite_cycle = 0

        for each_transition in self.transition: 
            if each_transition[0] in self.accepting:   
                for i in range(len(each_transition[2])): 
                    if each_transition[0] == each_transition[2][i]: 

                        infinite_cycle = c.deepcopy(each_transition[0])
                        infinite_cycle = list(infinite_cycle)
                        infinite_cycle[1] = 1
                        infinite_cycle = tuple(infinite_cycle)

                        state_loops.append([each_transition[0], [each_transition[1][i]], [infinite_cycle]])
                        state_loops.append([infinite_cycle,[each_transition[1][i]], [infinite_cycle]])

                        for elem in self.transition:
                            each_ac_transitions.append(elem)
                        
                        for elem in state_loops:
                            each_ac_transitions.append(elem)
                        
                        all_ac_transitions.append(each_ac_transitions)
                        each_ac_transitions = []
                        state_loops = []
                        
        self.transition = all_ac_transitions
        return self.transition

    def construct_states(self,transitions):
        automaton_states = []

    
        for each_transition in transitions:
            automaton_states.append(each_transition[0])
    
        automaton_states = set(automaton_states)
        automaton_states = list(automaton_states)
        return automaton_states

    def construct_ac(self,transitions):
        automaton_ac = []

        for each_transition in transitions:
            if each_transition[0][1] == 1:
                automaton_ac.append(each_transition[0])
        
        automaton_ac = set(automaton_ac)
        automaton_ac = list(automaton_ac)
        return automaton_ac
    


    def construct_NGAs(self):
        
        self.transition = self.construct_loops()
        self.initial = self.initial_index()

        each_automaton = []
        all_automaton = []

        for automaton_transitions in self.transition:
            states = self.construct_states(automaton_transitions)
            accepting_condition = self.construct_ac(automaton_transitions)

            each_automaton = [states,  self.initial, self.alphabet, automaton_transitions, accepting_condition]
            all_automaton.append(each_automaton)
            each_automaton = []

        # all_automaton arry hold ==>  [[A1], [A2], etc] == [[[A1 states], [A1 initial], [alphabet], [A1 transitions], [A1 ac]],  [A2 DATA] , etc]]

    
        
        return all_automaton
    def NGA_print(self):
        
        NGAs = self.construct_NGAs()

        print("......................................................................................") 
        print("\n  Equivalent Non-determinisitc Generalized Buchi automaton Formal Descriptions ")
        print("......................................................................................") 

        print("\n ")


        prime_counter = 1
        for nga in NGAs:
            

            prime = "'" * prime_counter
            
            print("\n                     A", prime)
            print (" \n ............ Set of states ............")

            print("\n", sorted(nga[0]))


            print (" \n ............ Set of initial states ............")

            
            print("\n", sorted(nga[1]))
            
            
            print (" \n ............ Computational alphabet ............")
            
            print("\n", sorted(nga[2]))


            print (" \n ............ State transitions ............ \n")

            sub = nga[3]
            for i in range(len(sub)): 
                for k in range(len(sub[i][1])):
                    print(str(sub[i][0]) + " -------- " + str(sub[i][1][k]) + " --------> " + str(sub[i][2][k]))
                

            print (" \n ............ State satisfying acceptence condition ............ \n ")
                
            print("\n", nga[4])
            

            print("\n...................................................................................... \n")
            prime_counter += 1

        return NGAs

