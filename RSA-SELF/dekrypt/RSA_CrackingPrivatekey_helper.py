
# Hvordan virker det

# Pick 2 prime numbers (normalt 2 kæmpe prime tal)

p = 715221027150531229989088117571256745127618921

q = 2

 
# N er produktet af p og q, N bliver brugt som en del af den offenlige nøgle 
# p og q er faktoreringen af N, det er mange gange sværer at faktorer 2 n til p og q, end at gange p og q til at få n.
# dette er selve ideen bag RSA og asymmestrisk kryptering.   
n = p * q

# udregning af euler's phi funktionen 
# denne funktion udskriver alle coprime tal fra 1 til N altså produktet af (p * q), dette kan tage "uendelige" lang tid hvis p og q ikke kendes. 
# siden man ellers ville skulle kører N igennem en brute force algoritme der ville skulle tjekke hvert tal. 
# når man kender p og q, og de begge er primtal, er det så nemt at indsætte i euler's phi funktionen.  
ΦN = (p-1)*(q-1)

# valg af krypterings tal e
#e skal være 1 < e < ΦN; det skal ligge imellem 1 og ΦN
#e skal være coprime med N samt ΦN; 
# men alt dette ved vi ikke da vi ikke har ΦN

# derfor skal der faktureres p og q som er n
# der kendes kun den offentlige nøgle (e, n)
print(n) 


