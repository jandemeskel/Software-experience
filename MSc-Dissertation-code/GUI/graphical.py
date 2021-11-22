import pydot
import os

class graph:

    def __init__(self, automata, img_number):
        self.automata = automata
        self.img_number = img_number

    def construct_graph(self):

        graph = pydot.Dot("Output", graph_type="digraph", strict=True,  rankdir = 'LR')

        
        for state in self.automata[0]:
            if (state in self.automata[4]) and (state in self.automata[1]):
            
                node = pydot.Node(str(state), shape="square", color = "green")
                graph.add_node(node)
            
            elif (state in self.automata[4]):
                node = pydot.Node(str(state), color = "green")
                graph.add_node(node)
        
            elif (state in self.automata[1]):
                node = pydot.Node(str(state), shape = "square")
                graph.add_node(node)

            else:
                node = pydot.Node(str(state), shape="circle")
                graph.add_node(node)

        for each_t in self.automata[3]:
            for i in range(len(each_t[1])):
                my_edge = pydot.Edge(str(each_t[0]), str(each_t[2][i]), label = each_t[1][i])
                graph.add_edge(my_edge)


        
        path = "GUI\static"
        graph.write_png(os.path.join(path, "A" + str(self.img_number) + ".png" ))


