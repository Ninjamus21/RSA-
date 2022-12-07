# Hvordan virker det

# Pick 2 prime numbers (normalt 2 kæmpe prime tal) men i dette eksempel for at vise matematikken bag det det er gjort
# med mindre tal 

p = 2 
q = 7 
 
# N er produktet af p og q, N bliver brugt som en del af den offenlige nøgle 
# p og q er faktoreringen af N, det er mange gange sværer at faktorer 2 n til p og q, end at gange p og q til at få n.
# dette er selve ideen bag RSA og asymmestrisk kryptering.   
N = p * q

# udregning af euler's phi funktionen 
# denne funktion udskriver alle coprime tal fra 1 til N altså produktet af (p * q), dette kan tage "uendelige" lang tid hvis p og q ikke kendes. 
# siden man ellers ville skulle kører N igennem en brute force algoritme der ville skulle tjekke hvert tal. 
# når man kender p og q, og de begge er primtal, er det så nemt at indsætte i euler's phi funktionen.  
ΦN = (p-1)*(q-1)

# valg af krypterings tal e
#e skal være 1 < e < ΦN; det skal ligge imellem 1 og ΦN
#e skal være coprime med N samt ΦN; 


for i in range(1,ΦN+1):
    if (i % ΦN) == 0:
        break
    else:
        ## make is so it checks the numbers to that are coprime with N 
        for i in range(1,ΦN+1):
            if (i % N) == 0:
                break 
            else: 
                print(i)




