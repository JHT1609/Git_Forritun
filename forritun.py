#johannes
#1/25/2017

#Verkefni 1
tala1=int(input("Sláðu inn tölu "))
tala2=int(input("Sláðu inn aðra tölu "))
print("Tölurnar lagðar saman eru",tala1+tala2,"samtals")
print("Tölurnar margfaldaðar saman eru",tala1*tala2,"samtals")

#Verkefni 2
fnfn=input("Sláðu inn fornafn þitt ")
enfn=input("Sláðu inn eftir nafn þitt ")
print("Halló",fnfn,enfn)

#Verkefni 3
tlj1=0
tlj2=0
txt=input("Sláðu inn texta")
for x in txt:
    if x.isalpha() and x.isupper():
        tlj1=tlj1+1
    if x.isalpha() and x.islower():
        tlj2=tlj2+1
print(tlj1)
print(tlj2)
