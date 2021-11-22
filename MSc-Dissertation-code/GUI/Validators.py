
class Validator():

    def __init__(self, Automata):
        self.states = Automata[0]
        self.initials = Automata[1]
        self.alphabet = Automata[2]
        self.transitions = Automata[3]
        self.accepting = Automata[4]

############## states input validator ##############

    def validate_states(self, states):

        valid_input = True
        response = 'Successful input'

        if len(states) < 1:
            valid_input = False
            response = 'No input detected, try again'
        
        for state in states:
            if any((not i.isalpha()) for i in state[0]):
                valid_input = False
                response = ' Please label states using Alphabetic character(s) only, for instance " [A, B, C]"  or "[One, Two, Three]" corresponds to the first, second & third states '
            
        if (len(states) != len(set(states))):
            valid_input = False
            response = 'Please ensure states do not have duplicate labels '

        return valid_input, response

############## initial states input validator ##############

    def validate_initials(self, initials):
        
        valid_input = True
        response = 0

        if len(initials) < 1:
            valid_input = False
            response = 'No input detected, try again'
            
        elif len(initials) > len(self.states):
            valid_input = False
            response = 'Number of initial states cannot exceed number of total states entered, try again'

        elif not all(elem in self.states for elem in initials):
            valid_input = False
            response = 'Please choose an existing state from the set of states entered above.'

        return valid_input, response

############## alphabet input validator ##############

    def validate_alphabet(self, alphabet):
        valid_input = True
        response = 0

        if len(alphabet) < 1:
            valid_input = False
            response = 'No input detected, try again'

        elif (any( not i.isdecimal() for i in alphabet)):
            valid_input = False
            response = 'Please follow the numerical labelling convention, for instance " 0 1" or "10 20" would correspond to two characters within the alphabet'

        return valid_input, response

############## transitions input validator ##############

    def validate_transitions(self, transitions):
        valid_input = True
        response = 0

        if len(transitions) < 1:
            valid_input = False
            response = 'No input detected, try again'
        
        for each_transition in transitions:
            if (each_transition[0] not in self.states):
                valid_input = False
                response = 'Transition entered contains a start state not from the set of existing states, try again'
            
            elif [z for z in each_transition[2] if z not in self.states] != []:
                valid_input = False
                response = 'Transition entered contains an end state not from the set of existing states, try again'
            
            elif [z for z in each_transition[1] if z not in self.alphabet] != [] :
                valid_input = False
                response = 'Transition entered contains letters not from the existing computational alphabet, try again'

            elif len(each_transition[2]) != len(each_transition[1]):
                valid_input = False
                response = 'Number of computed letters does not match the number of end states, try again'
        
        return valid_input, response
############## accepting conditions input validator ##############

    def validate_accepting(self, accepting):

        valid_input = True
        response = 0
        states_count = []

        if len(accepting) < 1:
            valid_input = False
            response = 'No input detected, try again'
        
        for collection in accepting:
                for each_set in collection:
                    states_count.append(each_set)
        states_count = list(set(states_count))

        if type(self.states[0]) != type(()):
            if type(collection) != type([]):
                valid_input = False
                response = 'Please enter accepting sets in the array format shown in the example above'
            
        if len(states_count) > len(self.states):
            valid_input = False
            response = 'Number of accepting states cannot exceed number of total states entered, try again'

        if type(self.states[0]) == type(()):

            state_char = []
            for state in self.states:
                state_char.append(state[0])

            for each_set in collection:
                if each_set not in state_char:
                    valid_input = False
                    response = 'Please choose an existing state from the set of states previously entered'
                    break
                break

        else:
            for each_set in collection:
                if each_set not in self.states:
                    valid_input = False
                    response = 'Please choose an existing state from the set of states previously entered'
                    break
                break
        
        return valid_input, response


############## main validator loop ##############

    def validate_form(self):

        response = []
        valid_input = True

    
        valid_input, response = self.validate_states(self.states)
        if valid_input:
            valid_input, response = self.validate_initials(self.initials)

        if valid_input:
            valid_input, response = self.validate_alphabet(self.alphabet)

        if valid_input:
            valid_input, response = self.validate_transitions(self.transitions)

        if valid_input:
            valid_input, response = self.validate_accepting(self.accepting)

        if valid_input:
            return [True, response]
        else:
            return [False, response]

