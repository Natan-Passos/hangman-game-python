 import random

userData = ''
list_words = []
words_separated = []
letters_user = []
body = ['o', '/', '|', '\ ','/','\ ']

def game():
    contLife = 6
    randomWord = random.randint(0, len(words_separated)-1)
    print('___')
    print(person(), partsHiddenWord(randomWord, '0'))
    while True:
        #deleteMembers()
        userData = input('Digite uma letra: ')
        print('___')
        if(verificationLettlers(randomWord, userData)):
            pass
        else:
            contLife -= 1
            deleteMembers(contLife)
            if contLife == 0:
                print(person(), partsHiddenWord(randomWord, userData))
                print('\n==== YOU LOSE ====')
                break
        print(person(), partsHiddenWord(randomWord, userData))
        if verificationEnd(partsHiddenWord(randomWord, userData)):
            print('\n**** YOU WIN ****')
            break
        if userData == '0':
            break

def person():
    return  '|  {0}  \n| {1}{2}{3} \n| {4} {5}'.format(body[0], body[1],body[2], body[3],body[4], body[5])

#Function for delete person members
def deleteMembers(cont):
    if cont == 5:
        body[cont] = '  '
    else:
        body[cont] = ' '

#Function to add elements in the list List_Words that  
def append(data):
    list_words.append(data)
    separateWords(data)

def separateWords(data):
    letters = ''
    firstInteration = True
    for i in data:
        if(firstInteration):
            letters = i
            firstInteration = False
        else:
            letters += '_' + i
    words_separated.append(letters)

def printWords():
    print(list_words)
    print(words_separated)

def partsHiddenWord(position, letter):
    letters_user.append(letter)
    word = words_separated[position].split('_')
    hiddenWord = ''
    for i in word:
        for a in letters_user:
            if a == i.lower():
                hiddenWord += ' '+ a + ' '
                break
        else:
            hiddenWord += ' _ '
    return hiddenWord

def verificationEnd(word):
    key = word.split(' ')
    for i in key:
        if i == '_':
            return False
    else:
        return True

def verificationLettlers(position, lettlers):
    word = words_separated[position].split('_')
    for a in word:
        if a == lettlers:
            return True
    return False

def wordDelete(data):
        word_verification = False
        for i in range(len(list_words)-1):
            if list_words[i] == data:
                list_words.remove(data)
                words_separated.pop(i)
                word_verification = True
                print('Word successfully deleted')
                break
        if word_verification == False:
            print('Error: Word no found')

def positionDelete(data):
    if data > 0 and data <= len(list_words) and is_integer(data):
        list_words.pop(data-1)
        words_separated.pop(data-1)
        print('Word successfully deleted')
    else:
        print('Error: Number out to range')

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

#add word in the game
append('Toxic')
append('Home')
append('Cristal')
#Random 

#start game
if __name__ == "__main__":
    game()
