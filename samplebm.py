import numpy

connection_polynomial = [1,1,1,1,1, 1,0,0,0,0, 1,0,1,0,0]

initial_state  = [0,1,0,0,1, 0,0,1,1,1, 0,0,1,1,1]

message = "This message will be cracked by using Berlekmap-Massey algorithm. Muajajaja"

def to_binary(x):
    b = bin(x)[2:]
    r = [int(i) for i in b]
    while(len(r) < 8):
        r = [0] + r
    return r

def to_bin(string):
	intseq = []
	for x in string:
		intseq = intseq + to_binary(ord(x))
	return intseq
	

def encrypt(m, state, cp):
	m = to_bin(m)
	n = len(m)
	list_output = []
	for i in range(n):
		feedback = 0
		for s, c, in zip(state, cp):
			feedback += s*c
		feedback = feedback % 2
		list_output.append( (state.pop(0) + m[i])%2)
		state.append(feedback)
	return list_output
	
def give_me(m, c, i, j):
	m = to_bin(m)
	res = []
	for k in range(i,j):
		res.append((c[k]+m[k]) %2)
	return res 

ct = encrypt(message, initial_state, connection_polynomial)
print("Ciphertext:",ct)
# fin-ini must be larger than 2*len(connection_polynomial) + 8-ini%8
ini, fin = 21, 54
bits = give_me(message, ct, ini, fin)
print("Portion of known stream:", bits)
