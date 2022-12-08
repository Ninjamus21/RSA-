import math

# n findes med 2 kæmpe primtal
# Dette kan gøres igennem et andet script som jeg har kaldt "CreatingRSAKey.py"
# Men for nu kunne det være fedt at bevise måde jeg fandt frem til "RSA_example.py" værdier: n, e og d 

# p og q er primtal, de det fuldkommen lige meget hvilke primtal. Der er dog nogen sikkerheds mæssige problemer ved små primtal.
# Et nogenlunde eksempel på et af de 2 primtal kunne være 2048 bits, da det ville skabe en 4096 bit n 
q = 31
p = 101

# Så udrening af n er ret simpel når man kender p og q, dette lyder på: 
n = p * q

# For at udregne e og d skal der bruges eulers totient funktion for at finde phi
# Udrening af phi(n)

phiN = (p-1)*(q-1)
print(phiN)
# phi = 3000
# e må ikke dele en factor med phi
# Der vælges en lille e, som er større end værdien 2 

# eulers theorem 
# x**phiN == 1 (mod n)
# vores eksempel
# x**3000 == 1 % 3131
# man kan ændre phiN til en værd værdi som går direkte op med 3000 
# x**6000 == 1 % 3131
# da deres værdi satdig ville give 1 
#x**(3000*t+1) == x % 3131
# men dette kunne også skrvies: 
# x**(1 % 3000) = x % 3131

e = 197 

# her er der valgt en e værdi til 197
# hvilket for formlen til at lyse på at: 
# den krypterede version af plainteksten er 
# x**e % 3000

# men hvad gør man for at dekryptere beskeden? 
# der skal udregnes noget der udligner e nemlig d, som er det omvendte / modsatte af e som vil genskabe den originale besked
# her ville formlen lyde på e * d == 1 % phiN
## eller 197 * d == 1 % 3000

# for at finde d skal man finde:  
# en måde at tjekke disse på er igennem formlen:
# (e * d) % phi == 1
# eller 
# e * d == 1 % phi

# udregning af d er omvendte af e, så man kan omstille tilbage igen
# Euclids Extended Greatest Common Divisor Algoritme 
# men først skal der laves en normal gcd (Greatest Common Divisor) udregning på værdierne 
# udregning af gcd 
Remainder = phiN%e
while int(Remainder) != 1:
    Remainder = phiN%e
    print(phiN, e, end = ' ')
    phiN = e
    e = Remainder
    print(Remainder)
print("gcd af (phiN,e) er: ", Remainder)
# udregning af Euclids Extended Greatest Common Divisor Algoritme 
# her startes der fra vores gcd udregninger som der er blevet lavet i afsnittet før 
# phiN = 6, e = 5, Remainder = 1
# nu er ideen at finde d igennem de tal som gcd udregning gav os 
1 == 6-1 % 5
1 == 2*6-1 % 11
1 == 2*17-3 % 11
1 == 8*17-3 % 45
1 == 8*197-35 % 45
1 == 533*197-35 % 3000

# der er udregnet op til starten af den første gcd udrening altså med start værdierne e = 197 og phiN = 3000
# ligning som der der bliver givet nu er: 

1 == 533*197-35 % 3000

# som omskrives til: 

1 == 533*197 % 3000

# og for at de skal gå op med vores grundformel for dekryptering (e * d == 1 % phi) omskrives den en sidste gang 

197 * 533 == 1 % 3000

# hvis man så kigger nærmere på opstillingen af formlen kan der ses at d = 533

d = 533 

# slut bevis 

# hvis der er en sætning som er krypterede med nøglen e, n fx.

besked = 45
print("Dette er den originale besked ", besked)

# kryptering af besked


hemmligeBesked = besked**e % 3131

print("Dette er den hemmelige besked ", str(hemmligeBesked))

dekrypteredeBesked = (hemmligeBesked**d % 3131)

print("Dette er den dekrypterede besked ", str(dekrypteredeBesked))





