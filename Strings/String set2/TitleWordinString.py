
'''converting first letter of every to upppercase in a sentence
Ex:-this is a day
o/p:-This Is A Day'''

def convertString(str):
    l=[(word[0].upper()+word[1:]) for word in str.split()]
    str=" ".join(l)
    return str

str=input()
d=convertString(str)
print(d)