import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def makeWord():
    n = input("Word: ")
    if not all(x.isalpha() or x==" " for x in n) or len(n)==0:
        print("Invalid!")
        input("Press enter to continue...")
        cls()
        return makeWord()
    return n


def attempt(result=0,vidas=0):
    print(*result)
    if vidas:
        print("Vidas: {}".format(vidas))
    n = input("Letter: ")
    length = len(n)
    if not 0<length<2:
        print("Invalid!")
        input("Press enter to continue...")
        cls()
        return attempt(result)
    return n
