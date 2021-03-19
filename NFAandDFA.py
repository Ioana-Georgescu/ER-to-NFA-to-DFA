# Georgescu Ioana 331CB
import sys

# NFA, DFA si conversia de la NFA la DFA din Tema 2

class NFA:
	def __init__(self, states, final_states, transitions, initial_state, alphabet):
		self.states = states # {0, 1, 2, ...}
		self.initial_state = initial_state
		self.current_state = initial_state
		self.final_states = final_states # {2, 3, ...}
		self.transitions = transitions # { (0, 'a'): [1, 2], ...}
		self.alphabet = alphabet
		self.epsilonClosures = dict()
		# le calculez pe toate la inceput pentru a nu le recalcula mai tarziu
		for x in states:
			self.epsilonClosures[x] = self.epsilonClosure(x)

	def epsilonClosure(self, state):
		eps_cl = {state}
		eps_cl.update(self.checkDown(state, eps_cl))
		return eps_cl

	def checkDown(self, state, eps_cl):
		if (state, 'eps') in self.transitions:
			for x in self.transitions.get( (state, 'eps') ):
				if x not in eps_cl: # ca sa evit bucle pe tranzitii epsilon
					eps_cl.add(x)
					nextStates = self.checkDown(x, eps_cl)
					eps_cl.update(nextStates)
		return eps_cl

	def reachableOnSymbol(self, state, c):
		states = set()
		# poate parcurge oricate tranzitii epsilon pana ajunge intr-o stare
		# in care poate consuma simbolul c
		start_points = self.epsilonClosures.get(state)

		for x in start_points:
			if (x, c) in self.transitions: # poate consuma c
				next_points = self.transitions.get( (x, c) )

				# poate continua cu oricate tranzitii epsilon
				for s in next_points:
					if (s, 'eps') in self.transitions:
						states.update(self.epsilonClosures.get(s))

				states.update(next_points)

		return states

	def printNFA(self, fileName):
		f_out = open(fileName, "w")
		f_out.write(f'{len(self.states)}\n')

		not_first = 0
		for x in self.final_states:
			if not_first == 0:
				not_first = 1
			else:
				f_out.write(' ')

			f_out.write( str(x) )

		f_out.write('\n')

		for d in self.transitions:
			f_out.write(f'{str(d[0])} {d[1]}')

			next_states = self.transitions.get(d)
			for state in next_states:
				f_out.write(f' {str(state)}')

			f_out.write('\n')

		f_out.close()


class DFA:
	def __init__(self, states, final_states, transitions, initial_state, alphabet):
		self.states = list(states) # Set(Tuple) -> List(Tuple)
		st_init = tuple(initial_state)
		# ma asigur ca starea initiala == 0
		if self.states.index(st_init) != 0:
			self.states.remove(st_init)
			self.states.insert(0, st_init)
		self.initial_state = self.states.index(st_init) # int
		self.current_state = self.states.index(st_init) # int
		self.final_states = final_states # Set(Tuple)
		self.transitions = transitions # { (Tuple, char): Tuple, ...}
		self.alphabet = alphabet

	def printDFA(self, fileName):
		f_out = open(fileName, "w")
		f_out.write(f'{len(self.states)}\n')

		not_first = 0
		for x in self.final_states:
			if not_first == 0:
				not_first = 1
			else:
				f_out.write(' ')

			f_out.write( str(self.states.index(x)) )
		f_out.write('\n')

		for d in self.transitions:
			f_out.write(f'{str(self.states.index(d[0]))} {d[1]} ')
			f_out.write(f'{str(self.states.index(self.transitions.get(d)))}\n')
		f_out.close()

def convert(nfa: NFA):
	dfa_states = set()
	st_init = nfa.epsilonClosure(nfa.initial_state)

	# daca nu are nevoie de sink state nu il mai adug la lista de stari
	# si nu-i mai definesc tranzitiile
	sink_state = {len(nfa.states)}
	needs_sink = 0

	dfa_final_states = set() # ca sa evit adaugarea de dubplicate
	dfa_transitions = dict() # pentru o cautare mai usoara
	alphabet = nfa.alphabet

	# 0 = nu am definit toate tranzitiile care duc din st_init in alte stari
	# cast la tuplui pentru ca sunt hashable (pot fi introdusi in dictionare)
	dfa_states.add((tuple(st_init), 0))

	# 1 pt ca din sink_state nu se poate ajunge in nicio alta stare
	dfa_states.add((tuple(sink_state), 1))

	nextOn = dict()
	for c in alphabet:
		for x in nfa.states:
			nextOn[(x, c)] = nfa.reachableOnSymbol(x, c)

	not_finished = list( filter(lambda x: x[1] == 0, dfa_states) )
	while len(not_finished) != 0:

		current_state = not_finished[0][0]
		# starea initiala ar putea fi si finala
		if len(set(current_state).intersection(nfa.final_states)) != 0:
			dfa_final_states.add(current_state)

		for c in alphabet:
			next_state = set() # ca sa evit dubplicatele
			for x in current_state:
				reachable = nextOn.get((x, c))
				if len(reachable) != 0:
					next_state.update(nextOn.get((x, c)))

			if len(next_state) == 0:
				needs_sink = 1
				dfa_transitions[(current_state, c)] = tuple(sink_state)
			else:
				dfa_transitions[(current_state, c)] = tuple(next_state)

				if (tuple(next_state), 1) not in dfa_states:
					dfa_states.add((tuple(next_state), 0))

		dfa_states.remove((current_state, 0))
		dfa_states.add((current_state, 1))
		not_finished = list( filter(lambda x: x[1] == 0, dfa_states) )

	if needs_sink == 0:
		dfa_states.remove((tuple(sink_state), 1))
	else:
		for c in alphabet:
			dfa_transitions[(tuple(sink_state), c)] = tuple(sink_state)

	dfa_states = [(x[0]) for x in dfa_states]
	return DFA(dfa_states, dfa_final_states, dfa_transitions, st_init, alphabet)