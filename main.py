# Georgescu Ioana 331CB
import sys
from antlr4 import *
from RegexLexer import RegexLexer
from RegexParser import RegexParser
from RegexToNFAVisitor import RegexToNFAVisitor
from NFAandDFA import *


if __name__ == '__main__':

	input = FileStream(sys.argv[1])
	lexer = RegexLexer(input)
	stream = CommonTokenStream(lexer)
	parser = RegexParser(stream)

	tree = parser.regex() # arborele de parsare

	regexToNFA = RegexToNFAVisitor()

	regexToNFA.nfa_final_states.add(regexToNFA.visit(tree))

	# starea initiala = 0
	nfa = NFA(regexToNFA.nfa_states, regexToNFA.nfa_final_states,
		regexToNFA.nfa_transitions, 0, regexToNFA.nfa_alphabet)

	nfa.printNFA(sys.argv[2])

	dfa = convert(nfa)

	dfa.printDFA(sys.argv[3])
