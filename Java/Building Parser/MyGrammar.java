import computation.contextfreegrammar.*;
import java.util.ArrayList;
import java.util.List;

public class MyGrammar {
	public static ContextFreeGrammar makeGrammar() {
		// You can write your code here to make the context-free grammar from the assignment

    // All variables in G0 constructured
    Variable q = new Variable("Q");
    Variable q1 = new Variable("Q1");
    Variable q2 = new Variable("Q2");
    Variable q3 = new Variable("Q3");
    Variable s = new Variable("S");
    Variable t = new Variable("T");
    Variable l = new Variable("L");
    Variable p = new Variable("P");
    Variable m = new Variable("M");
    Variable f = new Variable("F");
    Variable r = new Variable("R");

    // All terminals in G0 constructured
    Terminal one = new Terminal('1');
    Terminal zero = new Terminal('0');
    Terminal rightBracket = new Terminal(')');
    Terminal leftBracket = new Terminal('(');
    Terminal multiply = new Terminal('*');
    Terminal plus = new Terminal('+');
    Terminal x = new Terminal('x');
    
    // Start variable Q rules
    Rule r1 = new Rule(q, new Word(s,q1));
    Rule r2 = new Rule(q, new Word(t,q2));
    Rule r3 = new Rule(q, new Word(l,q3));
    Rule r4 = new Rule(q, new Word(one));
    Rule r5 = new Rule(q, new Word(zero));
    Rule r6 = new Rule(q, new Word(x));

    // Variable rules Q1, Q2, Q3
    Rule r7 = new Rule(q1, new Word(p,t));
    Rule r8 = new Rule(q2, new Word(m,f));
    Rule r9 = new Rule(q3, new Word(s,r));

    // Variable S rules
    Rule r10 = new Rule(s, new Word(s,q1));
    Rule r11 = new Rule(s, new Word(t,q2));
    Rule r12 = new Rule(s, new Word(l,q3));
    Rule r13 = new Rule(s, new Word(one));
    Rule r14 = new Rule(s, new Word(zero));
    Rule r15 = new Rule(s, new Word(x));
    
    // Variable T rules
    Rule r16 = new Rule(t, new Word(t,q2));
    Rule r17 = new Rule(t, new Word(l,q3));
    Rule r18 = new Rule(t, new Word(one));
    Rule r19 = new Rule(t, new Word(zero));
    Rule r20 = new Rule(t, new Word(x));

    // Variable f rules
    Rule r21 = new Rule(f, new Word(l,q3));
    Rule r22 = new Rule(f, new Word(one));
    Rule r23 = new Rule(f, new Word(zero));
    Rule r24 = new Rule(f, new Word(x));

    // Variable to terminal rules
    Rule r25 = new Rule(l, new Word(leftBracket));
    Rule r26 = new Rule(r, new Word(rightBracket));
    Rule r27 = new Rule(p, new Word(plus));
    Rule r28 = new Rule(m, new Word(multiply));

    // All variable rules stored into a a list
    List<Rule> rules = new ArrayList<Rule>();
    rules.add(r1);
    rules.add(r2);
    rules.add(r3);
    rules.add(r4);
    rules.add(r5);
    rules.add(r6);
    rules.add(r7);
    rules.add(r8);
    rules.add(r9);
    rules.add(r10);
    rules.add(r11);
    rules.add(r12);
    rules.add(r13);
    rules.add(r14);
    rules.add(r15);
    rules.add(r16);
    rules.add(r17);
    rules.add(r18);
    rules.add(r19);
    rules.add(r20);
    rules.add(r21);
    rules.add(r22);
    rules.add(r23);
    rules.add(r24);
    rules.add(r25);
    rules.add(r26);
    rules.add(r27);
    rules.add(r28);

    // Constructuring a CFG object defined by the rules of G0
    ContextFreeGrammar cfg = new ContextFreeGrammar(rules);

		return cfg;
	}
}
