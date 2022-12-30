import math

def pr(l, y) :	#prime
	for t in l :
		if y%t == 0 :
			return False
	return True

def exp(m, v, z=1) :	#exponent
	while m%(z*v) == 0 :
		z *= v
	return int(math.log(z, v))


stop = 'no'
while stop not in 'SisiYesyes' :
	
	n = int(input('\ninsert a number: '))
	div = []	#dividers
	fac = []	#factors
	
#dividers

	if n%2==0 :
		div.append(2)
	any(div.append(k) for k in range(3, int(n**(1/2)+1), 2) if n%k==0 and pr(div, k) is True)

#prime factors

	any(fac.append(''.join([str(f), '^', str(	exp(n, f))] if exp(n, f)!=1 else [str(f)])) for f in div)
	m = n
	for e in div :
		m //= e**(exp(n, e))
	if m!=1 and m not in div :
		fac.append(str(m))
			
	#prime/not prime
	
	print('\n{} is not a prime number;\nits prime factors are:\n\n{}\n\n\n'.format(n, ' '.join(fac)) ) if len(div)>0 else print('\n', n, 'is a prime number.\n\n\n')
	stop = input('stop? ')