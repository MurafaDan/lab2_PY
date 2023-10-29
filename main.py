# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print("---------Lucrare de laborator Nr2-------------")
print("------------------EX1-------------------------")
print()
s='ProgramareaInteractiva'
print("a) S[:-1]:  S=",s[:-1])
#taie sirul de la inceput pana la penultimul caracter
print("b) S[:1]:  S=",s[:1])
#se screi pana la primul caracter
print("c) S[0:1]:  S=",s[0:1])
#obtinel sirul de la indexul 0 pana la 1 similar ca b)
print("d) S[:]:  S=",s[:])
#Slice complet
print("e) S[-1:]:  S=",s[-1:])
#incepe  sirul incepand de la ultimul caracter pana la sfirsitul sirului
print("f) S[2:5]:  S=",s[2:5])
#extrage de la caracterul 2 la 5 fara al include pe 5-lea (a)
print("g) S[-3:-1]:  S=",s[-3:-1])
#extrage caracterul de la a 3lea la a 2lea de la urma
print("h) S[1:9:2]:  S=",s[1:9:2])
#fiecare a doilea caracter de la 1 la 8 fara a include a 9 element
print("i) S[::-1]:  S=",s[::-1])
#inverseaza sirul

print()
print("---------------------EX2----------------------")
print()
L=["a", "b", "c", "d", "e"]
print("a) L[-1] ", L[-1])
print("b) L[:1] ", L[:1])
print("c) L[::] ", L[::])
print("d) L[1:3:2] ", L[1:3:2])
print("e) L[2:len(l)] ", L[2:len(L)])
print("f) L[len(L)-2] ", L[len(L)-2])
print("g) L[1]+L[3] ", L[1]+L[3])
print("h) L[2]+L[-2] ", L[2]+L[-2])
print("i) L[2]*L[2:4] ", 2*L[2:4])
print("j) L[int(int('3'*2)/11))] ", L[int(int('3'*2)/11)])
print("k) L[0:1]=['x','y'] ")
L[0:1]=['x', 'y']
print(L)
# L[0:1] = ['x', 'y']
# print(L)
L[0:2] = ['Python']
print(L)

print()
print("---------------------EX3----------------------")
print()
b = [34, 45, 56, 38]

print("a) b.insert(-1, 12)")
b.insert(-1, 12)
print(b)  # [34, 45, 56, 12, 38]

print("b) b.pop()=")
b.pop()
print(b)  # Output: [34, 45, 56, 12]

print("c) b.remove(34)")
b.remove(34)
print(b)  # Output: [45, 56, 12]

print("d) b.append('doi')")
b.append('doi')
print(b)  # Output: [45, 56, 12, 'doi']

print("  e) b.index('doi')")
index_doi = b.index('doi')
print(index_doi)  # Output: 3

print("  f) b.count(34)")
print(b.count(34))  # Output: 0

print(" g) b.reverse()")
b.reverse()
print(b)  # Output: ['doi', 12, 56, 45]

print("h) b.sort()")
c = [34, 45, 56, 38]
c.sort()
print(c)

print(" i) del(b[0:2])")
del(b[0:2])
print(b)  # Output: [56, 45]

print(" j) b.extend([1]) ")
b.extend([1])
print(b)  # Output: [56, 45, 1]

print()
print("---------------------II SIRURI------------------------")
print()
print("7. Să se realizeze un program care citește un număr și stabilește dacă 3 este numărul denumărul de cifre întregi.")
numar = int(input("Introduceti un numar:"))
if -100 >= numar >= -999 or 100<= numar <= 999:
    print(f"{numar}Numarul are 3 cifre intregi")
else:
    print(f"{numar} nu are 3 cifre intregi")
print()
print("----------------III Liste ----------------------------")
print()
print("7. Să se scrie un program, care creează și afișează o listă ce conține primii M termini din secvența Fibonacci.(0,1...0+1=1, 1+1=2, 2+1=3,......etc.).")
numar=int(input("Introduceti un numar:"))
nr=numar
x = 0
temp = 1
while(nr>0):
    x, temp = temp, x + temp
    nr-=1
print(f"Sirul lui fibonnaci in seria {nr}=", x)
print()
print("-------------------IV Sarcini aditionale-----------------")
numar=int(input("introduceti un numar:"))
if 10<=numar<=99:#13
    rev=numar**2 #169
    reversednumar=int(str(numar)[::-1]) #31
    reverseddouble=reversednumar**2 #961
    if int(str(reverseddouble)[::-1])==rev:
        print("Numarul este reversibil")
    else:
        print("Numaruol nu este reversibil la putere")
else:
    print("Numarul este negativ")