
def fakrek(n):
	if n==0:
		return 0
	if n==1:
		return 1
	return n* fakrek(n-1)

print(fakrek(5))

def fakit(n):
	i=1
	fak=1 
	while i <=n:
		fak = fak*i
		i+=1
	return fak

print (fakit(5))
