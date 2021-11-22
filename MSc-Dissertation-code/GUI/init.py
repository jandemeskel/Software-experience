
from GUI_parser import parser
from flask import Flask, render_template, request
from Algorithms.NGA_con import NGA_construct
import Terminal_programme.NBA_conversion as NBA_c
import Terminal_programme.Regular_operations as regops_c
import Validators as V
from graphical import graph

app = Flask(__name__)

formatter = HtmlFormatter(style="emacs",full=True,cssclass="codehilite")
css_string = formatter.get_style_defs()

def flatten(arr):
    arr = [i for j in arr for i in j]
    return arr    
    
@app.route("/")
def Home():
    return render_template('Home.html')



@app.route("/NGA", methods = ["GET", "POST"])
def NGA():

    data = []
    NGAs = []
    if request.method == 'POST':

        data.append(request.form.get('states'))
        data.append(request.form.get('initial'))
        data.append(request.form.get('alphabet'))
        data.append(request.form.get('accepting'))
        data.append(request.form.get('transitions'))
        try:
            if request.form.get('submit'):
                

                automata = parser(data[0],data[1],data[2],data[3],data[4]).parse_input()
                valid_input, response = V.Validator(automata).validate_form()

            if valid_input:
                    NGAs = NGA_construct().muller_to_NGA(automata)
                    img_number = 0
                    for automata in NGAs:
                        
                        graph(automata, img_number).construct_graph()
                        img_number += 1
                    return render_template('NGA.html', NGAs=NGAs)
            
            else:
                invalid = response
                return render_template('NGA.html', invalid=invalid)

        except:
                invalid = 'Error within input, go through the input stipulations example on the home page and try again'
                return render_template('NGA.html', invalid=invalid)
    return render_template('NGA.html')




@app.route("/NBA", methods = ["GET", "POST"])
def NBA():

    data = []
    if request.method == 'POST':

        data.append(request.form.get('states'))
        data.append(request.form.get('initial'))
        data.append(request.form.get('alphabet'))
        data.append(request.form.get('accepting'))
        data.append(request.form.get('transitions'))

        try:

            if request.form.get('submit'):
                
                NGAs = []
                automata = parser(data[0],data[1],data[2],data[3],data[4]).parse_input()
                valid_input, response = V.Validator(automata).validate_form()

            if valid_input:

                NGAs.append(automata)
                NBAs = flatten(NBA_c.NBA(NGAs).construct_NBAs())

                img_number = 0
                graph(NBAs, img_number).construct_graph()
                   
                return render_template('NBA.html', NBAs=NBAs)

            else:
                invalid = response
                return render_template('NBA.html', invalid=invalid)

        except:
                invalid = 'Error within input, go through the input stipulations example on the home page and try again'
                return render_template('NBA.html', invalid=invalid)

    return render_template('NBA.html')



@app.route("/regops", methods = ["GET", "POST"])
def Regops():
    data = []
    NGAs = []
    if request.method == 'POST':

        data.append(request.form.get('states_one'))
        data.append(request.form.get('initial_one'))
        data.append(request.form.get('alphabet_one'))
        data.append(request.form.get('accepting_one'))
        data.append(request.form.get('transitions_one'))
    
        try:

            automata1 = parser(data[0],data[1],data[2],data[3],data[4]).parse_input()
            automata1[4] = flatten(automata1[4])
            NGAs.append(automata1)
            data = []
        
        except:

            invalid = 'Error within input, go through the input stipulations example on the home page and try again'
            return render_template('Regops.html')


        data.append(request.form.get('states_two'))
        data.append(request.form.get('initial_two'))
        data.append(request.form.get('alphabet_two'))
        data.append(request.form.get('accepting_two'))
        data.append(request.form.get('transitions_two'))

        try:

            automata2 = parser(data[0],data[1],data[2],data[3],data[4]).parse_input()
            automata2[4] = flatten(automata2[4])
            NGAs.append(automata2)
            data = []
        
        except:

            invalid = 'Error within input, go through the input stipulations example on the home page and try again'
            return render_template('Regops.html')
    
        if request.form.get('union'):

            valid_input,response = V.Validator(NGAs[0]).validate_form()

            if valid_input:

                valid_input,response = V.Validator(NGAs[1]).validate_form()

                if valid_input:


                    joint_construction = regops_c.Union(NGAs).union_of()
                    img_number = 0
                    graph(joint_construction, img_number).construct_graph()
                    return render_template('Regops.html', joint_construction=joint_construction)
                
                else:
                    invalid = response
                    return render_template('Regops.html', invalid=invalid)

            else:
                invalid = response
                return render_template('Regops.html', invalid=invalid)
            


        if request.form.get('intersection'):

            valid_input,response = V.Validator(NGAs[0]).validate_form()

            if valid_input:

                valid_input,response = V.Validator(NGAs[1]).validate_form()

                if valid_input:
                    intersect = regops_c.Intersection(NGAs).intersection_of()
                    for elem in intersect:
                        print(elem)
                    img_number = 0
                    graph(intersect, img_number).construct_graph()
                    return render_template('Regops.html', intersect=intersect)

                else:
                    invalid = response
                    return render_template('Regops.html', invalid=invalid)
            
            else:
                invalid = response
                return render_template('Regops.html', invalid=invalid)


    return render_template('Regops.html')


if __name__ == '__main__':
    app.run(debug=True)