def solve(a, b):
    sum=0
    for i in range(a,b):
		n= str(i)[::-1]
		nnum=''
		for j in n:
			if j=="0":
				nnum+="0"
			
			elif j=="1":
				nnum+="1"
			elif j=="6":
				nnum+="9"
			
			elif j=="8":
				nnum+="8"
			
			elif j=="9":
				nnum+="6"
		if nnum==str(i):
			sum+=1
	return sum
