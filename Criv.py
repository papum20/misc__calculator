import math

def prime(l, n) :	#prime
	for d in l :
		if n%d == 0 :
			return False
	return True

def exp(num, max, res=1) :	#exponent
	while max%(res*num) == 0 :
		res *= num
	return int(math.log(res, num))




while True :
	
	try:
		n = int(input('\nn: '))
	except:
		break
		
	div = []	#dividers
	fac = []	#factors
	
#dividers

	if n%2 == 0 :
		div.append(2)
	any(div.append(k) for k in range(3, int(n**(1/2)+1), 2) if n%k==0 and prime(div, k) is True)

#prime factors

	any(fac.append( str(f)+'^'+str(exp(f, n)) if exp(f, n)!=1 else str(f) ) for f in div)
	
	m = n	#factor > sqrt(n)
	for divide in div :
		m //= divide**(exp(divide, n))
	if m!=1 and m not in div :
		fac.append(str(m))
			
	#prime/not prime
	
	print('\nnot prime:\n{}\n\n\n'.format(' '.join(fac)) ) if len(div)>0 else print('\nprime.\n\n\n')