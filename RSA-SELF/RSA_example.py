# Program for RSA (Rivest-Shermir-Adlemen) kryptering 

## bevis for RSA Kryptering og hvorfor det virker asymetrisk kryptering 
# disse numre q og p er den offenlige nøgle som man benytter sig af under kryptering af beskeden. Bid mærke i at det er primtal
# krypteringslås 
q = 61
p = 53

n = p * q
#
# kryptering af besked 
# besked 
PlainText = 566


# for at dekryptere beskeden skal man kende e enkryptions nøglen samt d dekryptions nøglen hvilket er: 
# e for enkryption
e = 17
# d for dekryption 
d = 2753

# kryptering af beskeden forgår på følgende måde: 
# enkryption
c = (PlainText**e) % n

# c fungere som cipherteksten altså den krypterede ukendte besked, som ikke er læselige 
# for at få en ide om hvad uvedkommende vil se printes den krypterede tekst ud. 
print("dette er hvad man ville se uden at dekryptere med den private nøgle: " + str(c))

# hvis man så havde adgang til den private nøgle ville man kunne dekryptere den: 
# dekryption
PlainText = (c**d) % n
print("dette er hvad man ville se med den private nøgle: " + str(PlainText))

# dette var et allerede lavet eksempel på rsa algoritme som der virker. Måden man finder e samt d vi specificeres senere. 
# dette er den oplyste løsning og sådan ejeren af den offentlige og private nøgle med nemhed både kan kryptere og dekryptere beskeder. 
# normalt ville tallende være meget meget større, da det ville være ret nemt at bruteforce sig igennem dette eksempel, da tallende er små.