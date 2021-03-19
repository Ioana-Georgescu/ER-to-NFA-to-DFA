import sys
from antlr4 import *
from RegexParser import RegexParser
from RegexVisitor import RegexVisitor

class RegexToNFAVisitor(RegexVisitor):

	def __init__(self):
		self.nfa_alphabet = set()
		self.nfa_states = set()
		self.nfa_final_states = set()
		self.nfa_transitions = dict()

		# porneste de la starea initiala = 0; folosita pentru construire NFA
		# va deveni starea finala a NFA
		self.current_state = 0


	# adauga o tranzitie noua sau adauga o stare noua la o tranzitie existenta
	def addToTransition(self, key, new_state):
		if key in self.nfa_transitions:
			auxList = self.nfa_transitions[key]

			if new_state not in auxList:
				auxList.append(new_state)
				self.nfa_transitions[key] = auxList
		else:
			self.nfa_transitions[key] = [new_state]


	# regex1 sau (regex1 U regex2)
	def visitRegex(self, ctx:RegexParser.RegexContext):
		regex1 = ctx.concat_regex()
		regex2 = ctx.regex()

		# ma asigur ca starea curenta este inregistrata
		# necesar daca este starea initiala
		self.nfa_states.add(self.current_state)

		if regex2:
			# starea initiala a secventei care accepta reunuinea
			reunion_start = self.current_state

			# prima stare a secventei care accepta regex1
			self.current_state = self.current_state + 1
			regex1_start = self.current_state
			self.nfa_states.add(regex1_start)

			# construieste secventa care accepta regex1 pornind de la starea curenta
			# returneaza starea ei finala
			regex1_end = self.visit(regex1)

			# prima stare a secventei care accepta regex2
			self.current_state = self.current_state + 1
			regex2_start = self.current_state
			self.nfa_states.add(regex2_start)

			# construieste secventa care accepta regex1 pornind de la starea curenta
			# returneaza starea ei finala
			regex2_end = self.visit(regex2)

			# starea finala a secventei care accepta reunuinea
			self.current_state = self.current_state + 1
			reunion_end = self.current_state
			self.nfa_states.add(reunion_end)

			# conecteaza sarile initiale
			self.addToTransition((reunion_start, 'eps'), regex1_start)
			self.addToTransition((reunion_start, 'eps'), regex2_start)

			# conecteaza starile finale
			self.addToTransition((regex1_end, 'eps'), reunion_end)
			self.addToTransition((regex2_end, 'eps'), reunion_end)

			return self.current_state

		else:
			# construieste secventa care accepta regex1
			# starea ei finala = noua stare curenta
			return self.visit(regex1)


	# kleene_regex sau (kleene_regex concat_regex)
	def visitConcat_regex(self, ctx:RegexParser.Concat_regexContext):
		kleene_regex = ctx.kleene_regex()
		concat_regex = ctx.concat_regex()

		# ma asigur ca starea curenta este inregistrata
		# necesar daca este starea initiala
		self.nfa_states.add(self.current_state)

		if concat_regex:
			# construieste secventa care accepta kleene_regex pornind de la starea curenta
			# returneaza starea ei finala
			first_half_end = self.visit(kleene_regex)

			# prima stare a secventei care accepta concat_regex
			self.current_state = self.current_state + 1
			self.nfa_states.add(self.current_state)

			# leaga secventele
			self.addToTransition((first_half_end, 'eps'), self.current_state)

			# construieste secventa care accepta concat_regex
			# starea ei finala = noua stare curenta
			return self.visit(concat_regex)

		else:
			# construieste secventa care accepta concat_regex
			# starea ei finala = noua stare curenta
			return self.visit(kleene_regex)


	# atom_regex sau (atom_regex)*
	def visitKleene_regex(self, ctx:RegexParser.Kleene_regexContext):
		atom_regex = ctx.atom()
		kleene_regex = ctx.KLEENE()

		# ma asigur ca starea curenta este inregistrata
		# necesar daca este starea initiala
		self.nfa_states.add(self.current_state)

		if kleene_regex:
			# noua stare initiala pt secventa care accepta (conc_regex)*
			start_state_kleene_encaps = self.current_state

			# fac o stare noua
			self.current_state = self.current_state + 1
			self.nfa_states.add(self.current_state)

			# prima stare din secventa care accepta conc_regex
			start_state = self.current_state
			self.addToTransition((start_state_kleene_encaps, 'eps'), start_state)

			# ultima stare din secventa care accepta conc_regex
			end_state = self.visit(atom_regex)

			self.addToTransition((end_state, 'eps'), start_state)

			# noua stare finala pt secventa care accepta (conc_regex)*
			self.current_state = end_state + 1
			self.nfa_states.add(self.current_state)
			self.addToTransition((end_state, 'eps'), self.current_state)

			self.addToTransition((start_state_kleene_encaps, 'eps'), self.current_state)

			# starea finala a secventei care accepta kleene_regex = noua stare curenta
			return self.current_state

		else:
			return self.visit(atom_regex)


	# simbol din alfabet sau (regex)
	def visitAtom(self, ctx:RegexParser.AtomContext):
		symbol = ctx.symbol()
		regex = ctx.inner_regex()

		if symbol:
			return self.visit(symbol)

		if regex:
			return self.visit(regex)


	# frunza a arborelui
	def visitSymbol(self, ctx:RegexParser.SymbolContext):
		# adauga simbolul in alfabet
		self.nfa_alphabet.add(str(ctx.SYMBOL()))

		# adauga starea curenta daca nu exista deja
		self.nfa_states.add(self.current_state)

		# adauga o tranzitie pe simbol din alfabet catre o noua stare
		self.addToTransition((self.current_state, str(ctx.SYMBOL())), self.current_state + 1)

		# creaza + adauga noua stare
		self.current_state = self.current_state + 1
		self.nfa_states.add(self.current_state)

		return self.current_state


	# (regex)
	def visitInner_regex(self, ctx:RegexParser.Inner_regexContext):
		unpacked_regex = ctx.regex()

		return self.visit(unpacked_regex)