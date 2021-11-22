
# Framework guidance

## Preliminary

Firstly, before attempting to use the framework, please ensure all packages and dependecies are correctly installed as instructed in the documentation.
<br>
Source:  https://github.com/jandemeskel/MSc-Dissertation-Submission/blob/main/User%20Documentation.pdf 


## Functionality

To access the modules, ensure the framework is correctly imported by using the following test:

<div align="center">
    <img src ="PathTest.png" width = 50% height = auto>
</div>

***If the test fails:***

- Revert back to the documentation to ensure installation was completed correctly.
- Ensure the with file structure resembles the recommended structure within the documentation to ensure pathing issues do not occur.


***If successful, the framework's features are ready to be used***

The following information contains the name of the module, the main class contained and the corresponding functionality.

<div align="center">

<strong>Module Name</strong>: Muller_input()
<br>
<strong>Class</strong>: NMA

| Function      | Description |                            
| ----------- | ----------- |                                                     
| construct_FD()| Construct the formal description of a Muller automata via prompts from the terminal.|                            
| FD_print()| Display well formatted print statement of the Muller automata formal description in the terminal|
</div>

<br>
<div align="center">

<strong>Module Name</strong>: NGA_conversion
<br>
<strong>Class</strong>: NGA(states, initial, alphabet, transitions, acceptance)

| Function      | Description |                            
| ----------- | ----------- |                           
|construct_NGAs()|Costruct an NGA from the class inputs corresponding to NMA components|                            
|NGA_print() |Display well formatted print statement of the NGA formal description in the terminal|                            


</div>
<br>
<div align="center">

<strong>Module Name</strong>: NBA_conversion
<br>
<strong>Class</strong>: NBA()

| Function      | Description |                            
| ----------- | ----------- |                           
|convert_NGA(NGA)|Convert a singular NGA to an equivalent NBA|                            
|construct_NBAs()|Convert a collection of NGAs to their equivalent NBAs|                            


</div>
<br>
<div align="center">

<strong>Module Name</strong>: Regular_operations
<br>
<br>
<strong>Class</strong>: Union([Automata1, Automata2])

| Function      | Description |                            
| ----------- | ----------- |                           
|Union_of_two(Automata1, Automata2)| The Union of two Finite or Stream automata|                            
|Union_of()|The union of multiple finite or stream automata|                            
|Union_print()|Display well formatted print statement of the Union formal description in the terminal|

<strong>Class</strong>: Intersection([Automata1, Automata2])

| Function      | Description |                            
| ----------- | ----------- |                           
|Intersect_two(Automata1, Automata2) | The Union of two Stream automata|                          
|Intersection_of()|The union of multiple Stream automata|                            
|Intersection_print()|Display well formatted print statement of the Intersection formal description in the terminal|


</div>



## Data Structure

Every automata is stored within a nested array with the following structure:

```
Automata = [ [States], [Initial(s)], [Alphabet], [Transitions], [Accepting] ] 
```

Where the transitions array takes the form of:

``` 
Transition = [T1, T2, ..., Tn]
T1 = [Start, [computed chars], [End state]]
etc...
```


For instance, the following automata and the corresponding data struct used in the framework to model it.

<div align="center">
    <img src ="ExampleDataStruct.png" width = 35% height = auto>
</div>


```
A = [ [Q], [Q0], [E], [T], [AC]]

Q = [q0, q1]

Q0 = [q0]

E = [a]

T = [ [[q0], [a], [q1]], [[q1], [a], [q0]] ]

AC = [q1]
```

## Framework Application - Union 

The regular operation for the union of stream automata was implemented using the models provided within the framework & algorithm Pseudocode provided by a standard textbook written by Esparzsa.


<div align="center">
    <img src ="UnionPseudo.png" width = 49% height = auto>
</div>

Below is the full source code produced to implement the above algorithm which is an explicity demonstration of the type of open-ended application possible using this framework.

<div align="center">
    <img src ="UnionSC1.png" width = 100% height = auto>
</div>

The addition of a well-formed print statement was included to provide a convinent method of inspecting the algorithms outputs within the terminal.

<div align="center">
    <img src ="UnionSC2.png" width = 49% height = auto>
</div>

## Suggested Application

Similar to the implementation of the union and intersection, a user may desire to implement the complement of an NGA. The user could do so by utilizing the framework and any standard algorithm as such:


<div align="center">
    <img src ="ExampleUse.png" width = 49% height = auto>
    <img src ="Complement.png" width = 45% height = auto>
</div>
                                                    
                                                


# GUI development server

Alternatively, one can use run the graphical user interface on a Flask development server and use the framework's features on face-value as a calculator for stream automata conversions and regular operations. To set up a development server complete the following steps.

- Download the GUI package from the project GitHub page at : https://github.com/jandemeskel/MSc-Dissertation-Submission


<div align="center">
    <img src ="GitHubRepo.png" width = 49% height = auto>
</div>

- Ensure all external dependencies are installed as guided by the framework documentation.

- Open & run the init.py folder 



<div align="center">
    <img src ="GUIDirectory.png" width = 49% height = auto>   
  
</div>

- View the terminal response and open the development server URL provided within an up to date web browser.




<div align="center">
    <img src ="developmentURL.png" width = 49% height = auto>
  
</div>