
import copy as c


##########################################################################  Union  ########################################################################## 

class Union():
    def __init__(self, all_automaton):
        self.all_automaton = all_automaton

    def flatten(self,arr):
        arr = [i for j in arr for i in j]
        return arr

    def union_of_two(self, Automaton1, Automaton2):

        joint_automaton = []

        for i in range(len(Automaton1)):
            joint_automaton.append(list(zip(Automaton1[i], Automaton2[i])))
       
        for k in range(len(joint_automaton)):
            for elem in joint_automaton[k]:
                elem = list(elem)
            joint_automaton[k] = self.flatten(joint_automaton[k])
        

        for k in range(len(joint_automaton)) :
            if k != 3:

                joint_automaton[k] = set(joint_automaton[k])
                joint_automaton[k] = sorted(list(joint_automaton[k]))
        
        joint_automaton[3] = [i for j, i in enumerate(joint_automaton[3]) if i not in joint_automaton[3][:j]]


        return joint_automaton
    
    def union_of(self):

        complete_automaton = []

        complete_automaton = self.all_automaton[0]
        recursive_count = 1

        while recursive_count < len(self.all_automaton):
            complete_automaton = self.union_of_two(complete_automaton, self.all_automaton[recursive_count])
            recursive_count += 1

        complete_automaton = self.new_initial(complete_automaton)

        return complete_automaton
    
    def new_initial(self,automata):
        automata[0].append('initial')

        for state in automata[1]:
            automata[3].append([automata[0][-1], ['e'], [state]])

        automata[1] = [automata[0][-1]]

        return automata

    def union_print(self):
        
        x = self.union_of()
        joint_construction = self.new_initial(x)
      

        print("\n ...............................................................................................") 
        print("\n  Joint construction describing the language defined by the union of two w-regular languages ")
        print("...............................................................................,,,,,,,,,.......") 

        print (" \n ............ Set of states ............")

        print("\n", joint_construction[0])


        print (" \n ............ Set of initial states ............")

        
        print("\n", sorted(joint_construction[1]))
        
        
        print (" \n ............ Computational alphabet ............")
        
        print("\n", sorted(joint_construction[2]))


        print (" \n ............ State transitions ............ \n")

        sub = joint_construction[3]
        for i in range(len(sub)): 
            for k in range(len(sub[i][1])):
                print(str(sub[i][0]) + " -------- " + str(sub[i][1][k]) + " --------> " + str(sub[i][2][k]))
            

        print (" \n ............ State satisfying acceptence condition ............ \n ")
            
        print("\n", joint_construction[4])
        

        print("\n...................................................................................... \n")
    
        return joint_construction




##########################################################################  Intersection  ########################################################################## 



class Intersection():
    def __init__(self, all_automaton):
        self.all_automaton = all_automaton


# E.g. flatten nested arrays / cross product appending two nested arrays elementwise.

    def flatten(self,arr):
        arr = [i for j in arr for i in j]
        return arr    

    def cross_prod(self, x, y):
        cross_product = []
        for elem_x in x:
            for elem_y in y:
                cross_product.append((elem_x,elem_y))
        return cross_product

    def individual_transitions(self, t):
        collect = []
        for i in range(len(t[1])):
            collect.append([t[0], t[1][i], t[2][i]])
        return collect 
 
    def unpack(self, a):
            c = []
            if len(a) > 1:
                for i in range(len(a[0])):
                    c.append([a[0][i], a[1][i]])
            else: 
                c.append(a)
            return c

    def transition_remove_alpha(self,myList):
        for transition in myList:
            if not(all(x==(transition[1])[0] for x in transition[1])):
                myList.remove(transition)
                self.transition_remove_alpha(myList)
        return myList
    
    def transition_remove_beta(self,myList, states):
        for transition in myList:
            if transition[0] not in states:
                myList.remove(transition)
                self.transition_remove_beta(myList, states)
        return myList
    
    def rename_states(self, arr, used_char):

        rename_dict = {}

        letters = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        available_chars = sorted(list(set(letters) - set(used_char)))

        for char in range(len(used_char)):
            rename_dict[used_char[char]] = available_chars[char]
        
        for state in range(len(arr)):
            for key, value in rename_dict.items():
                if arr[state][0] == key:
                    arr[state] = (value, arr[state][1])
        return arr, rename_dict
    
    def rename_initial(self, arr, rename_dict):

        for initial in range(len(arr)):
            for key, value in rename_dict.items():
                if arr[initial][0] == key:
                    arr[initial] =  (value, arr[initial][1])
        return arr
    
    def rename_transitions (self, states, rename_dict):

        for key,value in rename_dict.items():
            if states[0] == key:
                states = (value, states[1])
        return states




# Intersection of two automata

    def intersect_two(self, Automaton1, AutomatonTwo):

        Automaton2 = c.deepcopy(AutomatonTwo)
        used_char_states = []
        used_char_initial = []
        used_char_t = []
        rename_dict = 0


####################### states rename ###########################

        for elem in Automaton1[0]:
            used_char_states.append(elem[0])
        used_char_states = list(set(used_char_states))

        for elem in Automaton2[0]:
            if elem[0] in used_char_states:
                Automaton2[0], rename_dict = self.rename_states(Automaton2[0], used_char_states)

####################### initial states rename ###########################

        for elem in Automaton1[1]:
            used_char_initial.append(elem[0])
        used_char_initial = list(set(used_char_initial))

        for elem in Automaton2[1]:
            if elem[0] in used_char_initial:
                Automaton2[1] = self.rename_initial(Automaton2[1], rename_dict)
    
        cross_states = self.cross_prod(Automaton1[0], Automaton2[0])
        cross_initial = self.cross_prod(Automaton1[1], Automaton2[1])
        cross_accepting = [self.cross_prod(Automaton1[0], Automaton2[4]), self.cross_prod(Automaton2[0], Automaton1[4])]
        cross_alphabet = list(set(Automaton1[2] + Automaton2[2]))
        
        for elem in range(len(cross_accepting)):
            cross_accepting[elem] = list(cross_accepting[elem])

        automaton1_individual_t = []
        automaton2_individual_t = []

        for transitions in Automaton1[3]:
            x = self.individual_transitions(transitions)
            automaton1_individual_t.append(x)

        for transitions in Automaton2[3]:
            x = self.individual_transitions(transitions)
            automaton2_individual_t.append(x)
        
        automaton1_individual_t = self.flatten(automaton1_individual_t)
        automaton2_individual_t = self.flatten(automaton2_individual_t)

        ####################### states in transitions rename ###########################

        for elem in automaton1_individual_t:
            used_char_t.append(elem[0])
            used_char_t.append(elem[2])
        used_char_t = list(set(used_char_t))
        
        for elem in range(len(automaton2_individual_t)):

            if automaton2_individual_t[elem][0] in used_char_t:
                automaton2_individual_t[elem][0] = self.rename_transitions(automaton2_individual_t[elem][0], rename_dict)
            
            if automaton2_individual_t[elem][2] in used_char_t:
                automaton2_individual_t[elem][2] = self.rename_transitions(automaton2_individual_t[elem][2], rename_dict)
  

        cross_prod_t = self.cross_prod(automaton1_individual_t, automaton2_individual_t)
        collect_transitions = []

        for elem in cross_prod_t:
            collect_transitions.append(self.unpack(elem))

        reduced_trans_alpha = self.transition_remove_alpha(collect_transitions)

        for elem in range(len(cross_states)):
            cross_states[elem] = list(cross_states[elem])
        
        cross_transitions = self.transition_remove_beta(reduced_trans_alpha, cross_states)

        for elem in range(len(cross_transitions)):
            cross_transitions[elem][1].pop()
        
            
        intersected_automaton = [cross_states, cross_initial, cross_alphabet, cross_transitions, cross_accepting]

        return intersected_automaton
    
# intersection of arbitrary many automata

    def intersection_of(self):

        resultant_automaton = []

        resultant_automaton = self.all_automaton[0]
        recursive_count = 1

        while recursive_count < len(self.all_automaton):
            resultant_automaton = self.intersect_two( resultant_automaton, self.all_automaton[recursive_count])
            recursive_count += 1
        
        resultant_automaton = self.GNBAtoNBA(resultant_automaton)

        return resultant_automaton
    
    def GNBAtoNBA(self,automata):

        reachable = []
        for initial in range(len(automata[1])):
            automata[1][initial] = list(automata[1][initial])

        for transition in range(len(automata[3])):
            if automata[3][transition][0] in automata[1] or automata[3][transition][2] in automata[1]:
                reachable.append(automata[3][transition])

        automata[3] = reachable


        y = NBA_i(automata).NBA_convert()

        return y


# Print formal definition of automata intersection

    def intersection_print(self):
        
        intersect_construction = self.intersection_of()

        print("\n ...............................................................................................") 
        print("  Construction describing the language defined by the intersection of two w-regular languages ")
        print(" ...............................................................................,,,,,,,,,.......") 

        print (" \n ............ Set of states ............")

        print("\n", sorted(intersect_construction[0]))


        print (" \n ............ Set of initial states ............")

        
        print("\n", sorted(intersect_construction[1]))
        
        
        print (" \n ............ Computational alphabet ............")
        
        print("\n", sorted(intersect_construction[2]))


        print (" \n ............ State transitions ............ \n")

        sub = intersect_construction[3]
        for i in range(len(sub)):
            print(str(sub[i][0]) + " -------- " + str(sub[i][1][0]) + " --------> " + str(sub[i][2]))
            

        print (" \n ............ State satisfying acceptence condition ............ \n ")
            
        print("\n", intersect_construction[4])
        

        print("\n...................................................................................... \n")

    
        return intersect_construction




##########################################################################  Complement  ########################################################################## 




class NBA_i():


    def __init__(self, NGAs):
        
        self.NGAs = NGAs
    


############## Auxiliary functions ###############

    def flatten(self,arr):
        arr = [i for j in arr for i in j]
        return arr    
    



    def rename_states(self, arr, used_char):
        rename_dict = {}

        x = []
        for tuple in self.flatten(used_char):
            x.append(tuple[0])

        used_char = x
        
        letters = [chr(x) for x in range(ord('A'), ord('Z') + 1)] + [chr(x) for x in range(ord('a'), ord('z') + 1)]
        available_chars = sorted(list(set(letters) - set(used_char)))

        for char in range(len(used_char)):
            rename_dict[used_char[char]] = available_chars[char]
        
        for state in range(len(arr)):
            for tuple in range(len(arr[state])):
                for key, value in rename_dict.items():
                    if arr[state][tuple][0] == key[0]:
                        arr[state][tuple] = (value, arr[state][tuple][1])
        return arr, rename_dict
    


    def rename_initial(self, arr, rename_dict):

        for initial in range(len(arr)):
            arr[initial] = list(arr[initial])
            for tup in range(len(arr[initial])):
                for key, value in rename_dict.items():
                    if arr[initial][tup][0] == key[0]:
                        arr[initial][tup] =  (value, arr[initial][tup][1])
            arr[initial] = tuple(arr[initial])

        return arr
    



    def rename_transitions (self, states, rename_dict):
      
        for tup in range(len(states)):
            for key,value in rename_dict.items():
            
                if states[tup][0] == key[0]:
                    states[tup]= (value, states[tup][1])

        return states

    
    #################### rename all NBA copies #################

    def rename(self, NGA_per_ac):

        #################### creating arrays to track the state names already in use #################
        used_char_states =[]
   
        for elem in NGA_per_ac[0][0]:
            used_char_states.append(elem)
        
        used_char_initial = []
        
        for elem in NGA_per_ac[0][1]:
            used_char_initial.append(elem)


        used_char_t = []

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
        buchi_states = []
        buchi_initial = []
        buchi_alphabet =  list(set (nba1[2] + nba2[2]))
        buchi_transitions = []
        buchi_accepting = []
        
        nba1_transitions = nba1[3]
        nba2_transitions = nba2[3]
        outgoing_char = []
        incoming_char = []
        all_states = []
        t_start = 0
        t_end = 0

        nba1_ac = nba1[4]
        for elem in range(len(nba1_ac)):
            nba1_ac[elem] = list(nba1_ac[elem])
        nba2_ac = nba2[4]
        for elem in range(len(nba2_ac)):
            nba2_ac[elem] = list(nba2_ac[elem])
        
        for elem in range(len(nba1[1])):
            nba1[1][elem] = list(nba1[1][elem])
        for elem in range(len(nba2[1])):
            nba2[1][elem] = list(nba2[1][elem])

        
        for transitions in range(len(nba1_transitions)):
            for ac in nba1_ac:
                if  sorted(nba1_transitions[transitions][0]) == sorted(ac):
                    if nba1_transitions[transitions][2] != ac:
                        buchi_accepting = ac
                        t_start = ac
                        outgoing_char.append(nba1_transitions[transitions][1])
        
        for transitions in range(len(nba2_transitions)):
            for ac in nba2_ac:
                if sorted(nba2_transitions[transitions][2]) == sorted(ac):
                    if nba2_transitions[transitions][0] != ac:
                        t_end = ac
                        incoming_char.append(nba2_transitions[transitions][1])

        t_char = list(set(self.flatten(outgoing_char + incoming_char)))
        if len(t_char) > 1:
            t_char = t_char[0]
        t = [t_start, t_char, [t_end]]
        buchi_transitions.append(t)
        incoming_char = []
        outgoing_char = []
        t_char = []

        for transitions in buchi_transitions:
            all_states.append(transitions[0])

        for transitions in range(len(nba2_transitions)):
            for ac in nba2_ac:
                if  sorted(nba2_transitions[transitions][0]) == sorted(ac):
                    if nba2_transitions[transitions][2] != ac:
                        t_start = ac
                        outgoing_char.append(nba2_transitions[transitions][1])
        
        for transitions in range(len(nba1_transitions)):
            for ac in nba1_ac:
                if sorted(nba1_transitions[transitions][2]) == sorted(ac):
                    if nba1_transitions[transitions][0] != ac:
                        t_end = ac
                        incoming_char.append(nba1_transitions[transitions][1])
        
        t_char = list(set(self.flatten(outgoing_char + incoming_char)))
        if len(t_char) > 1:
            t_char = t_char[0]

        t = [t_start, t_char, [t_end]]
        buchi_transitions.append(t)
        
        for transitions in buchi_transitions:
            all_states.append(transitions[0])

            if sorted(transitions[0]) in sorted(nba1[1]):
                if transitions[0] in nba1[4]:
                    buchi_initial.append(transitions[0])
            elif sorted(transitions[0]) in sorted(nba2[1]):
                 if transitions[0] in nba2[4]:
                    buchi_initial.append(transitions[0])
        
        if buchi_initial == []:
            buchi_initial = nba1[1]

        for states in all_states:
            if states not in buchi_states:
                buchi_states.append(states)

        buchi.append(buchi_states)
        buchi.append(buchi_initial)
        buchi.append(buchi_alphabet)
        buchi.append(buchi_transitions)
        buchi.append([buchi_accepting])


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
            if recursive_count == 1:
                joint_NBA = self.join_NBAs( NGA_per_ac[recursive_count], NGA_per_ac[0])
            
            else:
                joint_NBA = self.join_NBAs(NGA_per_ac[recursive_count], joint_NBA)
                    
            recursive_count += 1

 
        return joint_NBA


    def NBA_convert(self):
    
       
        NBAs = self.convert_NGA(self.NGAs)


        return NBAs