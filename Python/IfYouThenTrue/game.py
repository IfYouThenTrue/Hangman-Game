#FORCA
#Hangman
import os
from module import *

#Cria a senha
#User input --> password
word = makeWord()

length = len(word)

vidas = length

#Lista das posteriores letras certas e "-"
#List to store the letters and "-"
result = list()

#Coloca "*" ao invés de "-" para espaços
#Put "*" instead of "-" for whitespaces
for x in range(0,length):
    if word[x]==" ": result.append("*")
    else: result.append("-")

while True:
    acertou = False
    cls()
    
    #Ganhou, ou seja, sem "-" em result
    #If there is no more "-" in result, YOU WIN
    if all(x!="-" for x in result):
        print("You win!")
        break
    
    #Perdeu - vidas == 0
    #If there is no lifes, YOU LOSE
    if not vidas:
        print("You lose...")
        break

    #Pega o input do usuário
    #Gets the input
    letter = attempt(result,vidas)

    #Verifica se há em word, e, se sim, coloca em result
    #Check if the user input is valid for the password
    for x in range(0,length):
        if letter.lower()==word[x].lower():
            result[x]=word[x]
            acertou = True

    #Se não, perde uma vida
    #If not, the user looses one life
    if not acertou:
        vidas-=1

input()

    
