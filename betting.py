#include <iostream>
import sys
import os


winner = ''
FighterA = ''
FighterB = ''


i = int(0)
j = int(0)
k = int(0)

a = int(0) #Μετράει πόσοι έχουν ποντάρει στο Α
b = int(0) #Μετράει πόσοι έχουν ποντάρει στο Β

sumA = float(0) #Το συνολικό ποσό για το Α
sumB = float(0) #Το συνολικό ποσό για το Β
sumAll = float(sumA + sumB)

Gamblers = [] #Λίστα που κρατάει τα ονόματα όσων έχουν στοιχηματίσει
GamblersBets = [] #Λίστα που κρατάει τα ποσά όσων έχουν στοιχηματίσει

BetForA = [] #Λίστες που κρατάνε ποιος στοιχηματίζει σε ποιον
BetForB = []
AmountForA = [] #Λίστες που κρατάνε το ποσό που στοιχημάτησε ένας χρήστης
AmountForB = []




FighterA = input('First Fighter (a): ')
FighterB = input('Second Fighter (b): ')
os.system('cls||clear')

Gambler = input('Gambler: ')
os.system('cls||clear')



while Gambler != 'stop':
    
    Gamblers.append(Gambler)

    bet = input('Betting on "a" or "b": ')
    os.system('cls||clear')
    
    betMoney = int(input('Amount: '))
    os.system('cls||clear')
    GamblersBets.append(betMoney)

    if bet == 'a': 
        a += 1
        sumA += betMoney
        BetForA.append(Gambler)
        AmountForA.append(betMoney)
        print(Gambler, 'is betting ', betMoney, 'd on a')
        
    elif bet == 'b':
        b += 1
        sumB += betMoney
        BetForB.append(Gambler)
        AmountForB.append(betMoney)
        print(Gambler, 'is betting ', betMoney, 'd on b')

    else:
        print('You have to put "a" or "b"')

    sumAll = sumA + sumB

    Gambler = input('Gambler: ')
    os.system('cls||clear')


print('Waiting for Match to End...\n')
print(FighterA, 'VS', FighterB)
print('\n')
print(FighterA, '(a):', sumA,'d')
print(FighterB, '(b):', sumB,'d')
print('At Risk:', sumAll,'d\n')



A_Range = int(len(BetForA))
B_Range = int(len(BetForB))



print('Bets on ', FighterA)
for k in range(A_Range):
    print(BetForA[k], '-->', AmountForA[k], 'd', )


k = int(0)
print('\n')


print('Bets on ', FighterB)
for k in range(B_Range):
    print(BetForB[k], '-->', AmountForB[k], 'd', )
        


print('\n')
winner = input('Who won the match (a) or (b) ?: ')
print('\n')



if winner == 'a':
    for i in range(A_Range):
        perc = float((AmountForA[i]/sumA)*100)
        gets = float((perc*sumAll)/100)
        perc = round(perc)
        gets = round(gets)
        print(BetForA[i],'with',perc,'% of',sumAll,'d gets:', gets,'d')
elif winner == 'b':
    for j in range(B_Range):
        perc = float((AmountForB[j]/sumB)*100)
        gets = float((perc*sumAll)/100)
        perc = round(perc)
        gets = round(gets)
        print(BetForB[j],'with',perc,'% of',sumAll,'d gets:',gets,'d')
else:
    print('You have to put "a" or "b"') 

print('\n')
input('<Press Enter>')










        
