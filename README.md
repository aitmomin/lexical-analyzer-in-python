# lexical-analyzer-of-C-language

the realization of a lexical analyzer of the C language in Python.

For this, we identify the lexical units of the C language. We create a finite automaton accepting these lexical units. Then, we create an Automata class implementing a finite automaton. Consequently, in the main program, we create an object of type Automata implementing the automaton recognizing the lexical units of language C. Finally, apply this object to recognize the lexical units of language C appearing in a given text file.

Definition of a finite automaton

A finite state automaton A is defined as a 5-tuple A = <Q, , , q0, F> where:
  Q is the set of states,
   is an alphabet (a set of symbols),
  : Q    Q is the transition function of the automaton,
  q0 is the initial state of the automaton,
  F  Q is the set of final states (or acceptance states) of the automaton.
  
Example:
  Let A = <, Q, , q0, F> with
     = {0,1}
    Q = {q0, q1}
     = {(q0, 0, q0), (q0, 1, q1), (q1, 1, q1), (q1, 0, q0)}
    q0 is the initial state
    F = {q1}
