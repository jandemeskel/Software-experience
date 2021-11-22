import re
class parser():

    def __init__(self, states, initial, alphabet, accepting, transitions):
        self.states = states
        self.initial = initial
        self.alphabet = alphabet
        self.accepting = accepting
        self.transitions = transitions

    @staticmethod
    def get_states(app_input):
        states = state_initial_alphabet_parser(app_input)
        return states

    @staticmethod
    def get_initial(app_input):
        initial = state_initial_alphabet_parser(app_input)
        return initial

    @staticmethod
    def get_alphabet(app_input):
        alphabet = state_initial_alphabet_parser(app_input)
        return alphabet

    @staticmethod
    def get_accepting(app_input):
        accepting = []

        split_commas = []
        remove_commas = app_input.replace(']','').replace('[','').split('.')

        for i in range(len(remove_commas)):
            spaces = remove_commas[i].strip()
            split_commas.append(spaces)

        for elem in range(len(split_commas)):
            
            split_commas[elem] = split_commas[elem].split('|')
            accepting.append(split_commas[elem])

        return accepting

    @staticmethod
    def get_transition(app_input):

        app_input = app_input.split('-')
        for elem in range(len(app_input)):
            app_input[elem] = parse_transition(app_input[elem])
        
        return app_input


    def parse_input(self):

        states = self.get_states(self.states)
        initial = self.get_initial(self.initial)
        alphabet= self.get_alphabet(self.alphabet)
        transitions = self.get_transition(self.transitions)
        accepting = self.get_accepting(self.accepting)

        # if '(' is in a state then they're in a tuple and indexed
        # so inputs must be parsed via the tuples functions

        open = '('
        if open in states[0]:

            states = get_tuples(states)
            initial = get_tuples(initial)
            accepting[0] = get_tuples(accepting[0])
            transitions = parse_index_transitions(transitions)




        automata = []
        automata.append(states)
        automata.append(initial)
        automata.append(alphabet)
        automata.append(transitions)
        automata.append(accepting)

        return automata



################# axuiliary functions ###################

def flatten(arr):
    arr = [i for j in arr for i in j]
    return arr    

def state_initial_alphabet_parser(app_input):
    collection_of_sets = []
    
    split_commas = []
    remove_commas = app_input.replace(']','').replace('[','').split('.')

    for i in range(len(remove_commas)):
        spaces = remove_commas[i].strip()
        split_commas.append(spaces)
    
    for elem in range(len(split_commas)):
            
            split_commas[elem] = split_commas[elem].split('|')
            collection_of_sets.append(split_commas[elem])
    collection_of_sets = flatten(collection_of_sets)

    return collection_of_sets

def parse_transition(input):
    output = []
    split_commas = []
    remove_commas = input.replace('[','').replace(']','').split('.')

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

def get_tuples(input):

# Turns string tuples (string,int) into actual tuples (string,int) 
    output = []

    for item in input:
        try:
            text = re.search(r'\((.*?)\)',item).group(1)
        
            l,r = text.split(',')
            l,r = l.strip(' '),r.strip(' ') 
            try:
        
                wanted = (str(l),int(r))
                output.append(wanted)
            
            except Exception as e:
                pass

        except Exception as e :
            pass
    
    return output

def parse_index_transitions(transitions):

    for each_transition in range(len(transitions)):
        transitions[each_transition][0] = get_tuples([transitions[each_transition][0]]).pop()
        transitions[each_transition][2] = get_tuples(transitions[each_transition][2])

    return transitions
