import copy as c


class NBA():
    def __init__(self, NGAs):
        
        self.NGAs = NGAs
    
    def flatten(self,arr):
        arr = [i for j in arr for i in j]
        return arr    
    
    def rename_states(self, arr, used_char):
        rename_dict = {}

        letters = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        available_chars = sorted(list(set(letters) - set(used_char)))

        for char in range(len(used_char)):
            rename_dict[used_char[char]] = available_chars[char]
        
        for state in range(len(arr)):
            for key, value in rename_dict.items():
                if arr[state][0] == key[0]:
                    arr[state] = (value, arr[state][1])
        return arr, rename_dict
    
    def rename_initial(self, arr, rename_dict):

        for initial in range(len(arr)):
            for key, value in rename_dict.items():
                if arr[initial][0] == key[0]:
                    arr[initial] =  (value, arr[initial][1])
        return arr
    
    def rename_transitions (self, states, rename_dict):

        for key,value in rename_dict.items():
            if states[0] == key[0]:
                states = (value, states[1])
        return states
    
    def individual_transitions(self, t):
        collect = []
        for i in range(len(t[1])):
            collect.append([t[0], t[1][i], t[2][i]])
        return collect 
    
    def reset_dict(self, rename_dict):

        copy_rename = c.deepcopy(rename_dict)
        for key in copy_rename.keys():
            for value in copy_rename.values():
       
                if value == key[0]:
                    rename_dict.pop(key)
        return rename_dict
    
    #################### rename all NBA copies #################

    def rename(self, NGA_per_ac):

        #################### creating arrays to track the state names already in use #################
        used_char_states =[]
   
        for elem in NGA_per_ac[0][0]:
            used_char_states.append(elem)
        
        used_char_initial = []
        
        for elem in NGA_per_ac[0][1]:
            used_char_initial.append(elem)

        individual_t = []
        used_char_t = []

        for automata in range(len(NGA_per_ac)):
        
            for transition in NGA_per_ac[automata][3]:
                x = self.individual_transitions(transition)
                individual_t.append(x)
            individual_t = self.flatten(individual_t)
            NGA_per_ac[automata][3] = individual_t
            individual_t = []

        for elem in NGA_per_ac[0][3]:
            used_char_t.append(elem[0][0])
            used_char_t.append(elem[2])
        
        used_char_ac = []
        for automata in range(len(NGA_per_ac)):
            for elem in NGA_per_ac[automata][4]:
                used_char_ac.append(elem)

        rename_dict = 0

        for automata in range(1, len(NGA_per_ac)):
            
            #################### rename all the states of NBA copies #################

            for state in NGA_per_ac[automata][0]:
                if state in used_char_states:
                    NGA_per_ac[automata][0], rename_dict = self.rename_states(NGA_per_ac[automata][0], used_char_states)
            
            #################### rename all the initial states of NBA copies ##################    

            for initial in NGA_per_ac[automata][1]:        
                    if initial in used_char_initial:
                        NGA_per_ac[automata][1] = self.rename_initial(NGA_per_ac[automata][1], rename_dict)
                    
            #################### rename all the states in transitions of NBA copies #################

            for transition in range(len(NGA_per_ac[automata][3])):
                    
                    if NGA_per_ac[automata][3][transition][0] in used_char_t:
                        NGA_per_ac[automata][3][transition][0] = self.rename_transitions(NGA_per_ac[automata][3][transition][0], rename_dict)
                        
                    if NGA_per_ac[automata][3][transition][2]  in used_char_t:
                        NGA_per_ac[automata][3][transition][2] = self.rename_transitions(NGA_per_ac[automata][3][transition][2] , rename_dict)  
            
            #################### rename all the states in acceptance conditions of NBA copies #################
                
            for ac in NGA_per_ac[automata][4]:
           
                if ac in used_char_ac:
                    NGA_per_ac[automata][4] = self.rename_initial(NGA_per_ac[automata][4], rename_dict)
       

            for elem in NGA_per_ac[automata][0]:
                if elem not in used_char_states:
                    used_char_states.append(elem)

        return NGA_per_ac

    #################### combining two NBA copies to satisfy their individual acceptance conditions #################

    def join_NBAs(self, nba1, nba2):

        buchi = []

        buchi_states = nba1[0] + nba2[0]
        buchi_initial = nba1[1]
        buchi_alphabet = nba1[2]
        buchi_transitions = []
        
        nba1_transitions = nba1[3]
        nba2_transitions = nba2[3]
        all_transitions = []

        nba1_ac = nba1[4]
        nba2_ac = nba2[4]


      
        for transitions in range(len(nba1_transitions)):
            if  nba1_transitions[transitions][0] == nba1_ac[0]:
               

                  # redirect the accepting states transitions which are not loops to the other copies ac

                if nba1_transitions[transitions][2] != nba1_ac[0]:
                    nba1_transitions[transitions][2] = nba2[4]
                
                 # redirect the accepting state's loop to the other copies non-accepting state which is in the same position as the state its leaving
                else:
                    nba1_transitions[transitions][2] = nba2_transitions[transitions][0]
        
        for transitions in range(len(nba2_transitions)):
            
            if  nba2_transitions[transitions][0] == nba2_ac[0]:
                if nba2_transitions[transitions][2] != nba2_ac[0]:
                    nba2_transitions[transitions][2] = nba1[4]
                else:
                    nba2_transitions[transitions][2] = nba1_transitions[transitions][0]


        all_transitions = nba1_transitions + nba2_transitions
        buchi_transitions.append(all_transitions)


        buchi.append(buchi_states)
        buchi.append(buchi_initial)
        buchi.append(buchi_alphabet)
        buchi.append(buchi_transitions)
        buchi.append(nba1_ac)
        return buchi

    ### Splits a NGA input into NBA copies equal to the NGA's number of acceptance conditions & combines the copies for a single NBA ###

    # input -> Array of NGAs
    # Output -> Array of NBAs
    def convert_NGA(self, NGA):

        accepting_conditions = []
        NGA_per_ac = []
        joint_NBA = []

        for elem in NGA[4]:
            accepting_conditions.append(elem)
        
        for i in range(len(accepting_conditions)):
            NGA_per_ac.append(c.deepcopy(NGA))
        
        for i in range(len(accepting_conditions)):
            NGA_per_ac[i][4] = accepting_conditions[i]

        # NGA_per_ac should here return copies of the input NGA, one per acceptance condition.
        # each copy posses a unique ac from the set of ac's and each copy has states, initials, transitions and ac's renamed to distinquish between them.

        
        NGA_per_ac = self.rename(NGA_per_ac)
        
        # This loop should now build a single NBA as a joint construction of the NGA copies, the single NBA has an ac which satisfies all NGAs which its build from.
        recursive_count = 1

        while recursive_count < len(NGA_per_ac):
            additional_NBA = self.join_NBAs(NGA_per_ac[0], NGA_per_ac[recursive_count])

            if recursive_count == 1:
                joint_NBA = c.deepcopy(additional_NBA)
            
            else:
                for fd in range(len(joint_NBA)):
                    joint_NBA[fd] = joint_NBA[fd] + additional_NBA[fd]
                    
            recursive_count += 1
        
        joint_NBA[0] = list(set(joint_NBA[0]))
        joint_NBA[1] = list(set(joint_NBA[1]))
        joint_NBA[2] = list(set(joint_NBA[2]))
        joint_NBA[4] = list(set(joint_NBA[4]))
        joint_NBA[3] = self.flatten(joint_NBA[3])

        for each_t in range(len(joint_NBA[3])):
            if type(joint_NBA[3][each_t][2]) != type([]):
                joint_NBA[3][each_t][2] = [joint_NBA[3][each_t][2]]
        
        return joint_NBA


    ### repeats the NGA -> NBA process for a collection of NGAs. ###
    ## collection of NGAs with each NGA differing in set of acceptance conditions is a Muller automaton ##


    # input -> Array of NGAs           (This is the output of a muller -> NGA conversion) 
    # output -> Array of NBAs          (This array is the complete conversion of muller -> NBA)
    # The output is in the form for LTL conversion 

    
    def index_states(self,input):
            
        no_index = c.deepcopy(input[0][0])


        for elem in range(len(input[0][0])):
            if input[0][0][elem] in no_index:
                input[0][0][elem] = (input[0][0][elem],0)

        for elem in range(len(input[0][1])):
            if input[0][1][elem] in no_index:
                input[0][1][elem] = (input[0][1][elem],0)
        
        for elem in range(len(input[0][4])):
            for j in range(len(input[0][4][elem])):
                if input[0][4][elem][j] in no_index:
                    input[0][4][elem][j] = (input[0][4][elem][j],0)
        
        for elem in range(len(input[0][3])):
            for j in range(len(input[0][3][elem])):
                if input[0][3][elem][j] in no_index:
                    input[0][3][elem][j] = (input[0][3][elem][j],0)
        
            
        for elem in range(len(input[0][3])):
            for j in range(len(input[0][3][elem])):
                for k in range(len(input[0][3][elem][2])):
                    if input[0][3][elem][2][k] in no_index:
                        input[0][3][elem][2][k] = (input[0][3][elem][2][k],0)
        

        return input

    def construct_NBAs(self):

        NBAs = []


        #check if indexed, if yes then continue, if no then add 0 indexes to all states
        for automaton in self.NGAs:
            if len(automaton[0][0]) < 2:
                
       
                self.NGAs = self.index_states(self.NGAs)
                
                if len(automaton[4]) > 1:
                    NBAs.append(self.convert_NGA(automaton))
                else:
                    NBAs.append(automaton)

            else:
                
                
                if len(automaton[4]) > 1:
        
                    NBAs.append(self.convert_NGA(automaton))
                else:
                    NBAs.append(automaton)
        
        return NBAs



