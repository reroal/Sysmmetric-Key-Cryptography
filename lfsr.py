import numpy

connection_polynomial = [1,1,0,0]

initial_state  = [0,1,1,0]

def lfsr(state, cp, n):
	list_output = []
	for i in range(n):
		feedback = 0
		for s, c, in zip(state, cp):
			feedback += s*c
		feedback = feedback % 2
		list_output.append( state.pop(0))
		state.append(feedback)
	return list_output

print(lfsr(initial_state, connection_polynomial, 15))
