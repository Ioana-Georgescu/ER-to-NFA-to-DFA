// Georgescu Ioana 331CB
// antlr4 -Dlanguage=Python3 -no-listener -visitor Regex.g4
grammar Regex;

SYMBOL : [a-z] ; // o literamica din alfabet
OPEN : '(' ;
CLOSE : ')' ;
REUNION : '|' ;
KLEENE : '*'('*'*) ; // mai multe * consective vor fi ignorate

WHITESPACE : [ \t\n]+ -> skip ;

// ordinea de precedenta: *, concatenare, U

regex : concat_regex | concat_regex REUNION regex ;
concat_regex : kleene_regex | kleene_regex concat_regex ;
kleene_regex : atom | atom KLEENE ;
atom : symbol | inner_regex ;
symbol : SYMBOL ;
inner_regex : OPEN regex CLOSE ;