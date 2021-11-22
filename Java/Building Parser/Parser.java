import computation.contextfreegrammar.*;
import computation.parser.*;
import computation.parsetree.*;
import computation.derivation.*;
import java.util.ArrayList;
import java.util.List;


public class Parser implements IParser {
  
  public boolean isInLanguage(ContextFreeGrammar cfg, Word w){

    // Default return variable

    boolean output = false;

    // Pull all rules & start variable from Mygrammar.java

    List<Rule> rules = cfg.getRules();
    Variable startV = cfg.getStartVariable();

    // Procedure to check whether last output of derivation is a word in the isInLanguage
    // Where firstDerivation is the derivation of all one step rules from start variable

    ArrayList<Derivation> toCheck = getDerivation(rules, startV, w);

    for(Derivation d: toCheck){
      Word currentWord = d.getLatestWord();

      // test print to see all one step derivation outputs
      //System.out.println(currentWord);

      // coniditon comparing arbriary input word and all end state variables after 1 step
      if (currentWord.equals(w)){
        output = true;
      }
    }
    return output;
  }


 // ---------------------------------------------------------------------------------------------------------------


  // Function which finds all one step derivaitons from the start variable 

  private ArrayList<Derivation> getDerivation(List<Rule> rules, Variable startV, Word w){
    
    // list to hold all derivations, list of lists, with the nested list holding two elements, 
    //null step to the start variable and second element is the any one step from the start variable. 

    ArrayList<Derivation> firstD = new ArrayList();
    Word startV_word = new Word(startV.toString());
    int n = w.length();
    int constraint = (2*n)-2;

    // loop through all rules and compare whether the variable which the rule applies to is equivalent to the start variable
    // i.e. procedure to see whether the rule can be applied to the start variable

    for (Rule r: rules)
    {
      if (r.getVariable() == startV)
      {
        Derivation d = new Derivation(startV_word);
        d.addStep(r.getExpansion(), r, 0);
        firstD.add(d);
      }
    }
  //return firstD;


  // Derivation of pervious derivaiton, to change every loop

  ArrayList<ArrayList<Derivation>> loopD = new ArrayList();
  loopD.add(firstD);

  // for each derivation of previous lists of derivations

  // Empty array list to hold all derivations
  for( int i = 1; i <= constraint; i++)
  {
    ArrayList<Derivation> allD = new ArrayList();

    for (Derivation d: loopD.get(loopD.size()-1))
    { 
      // find the last derivation within the list of lists

      Word lastWord = d.getLatestWord();

      // for each symbol of the last derivation within the list of lists

      for (int index = 0; index<lastWord.length(); index++)
      {
        // for each rule within the grammars set of rules

        for (Rule r: rules)
        {
          // if the symbol is equivalent to a rule's symbol

          if (r.getVariable() == lastWord.get(index))
          {
            // find the derivation of the symbol, given that rule. i.e. if the rule is applied what is the RHS
            // add the derivation to a temporarily list

            Word newWord = lastWord.replace(index, r.getExpansion());

            Derivation currentD = new Derivation(d);
            currentD.addStep(newWord, r, index);

            // add derivation to the loop derivation list

            allD.add(currentD);
          }
        }
      }
    }
    loopD.add(allD);
  }
  
  // once all derivations of the loop are complete add that as one set of derivations for that step

  return loopD.get(loopD.size() - 1);
  }


 // ---------------------------------------------------------------------------------------------------------------


  public ParseTreeNode generateParseTree(ContextFreeGrammar cfg, Word w) {
    return null;
  }
}