import pathlib
import unidecode
import random

file_words : str = "words.txt"
list_words_size : list = []

def load_words()->list:
    # charger la liste de mots
    # retire les accents
    # stockage en mémoire
    words_list : list = []
    if not pathlib.Path(file_words).exists():
        print("le fichier words.txt n'éxiste pas !!!")
        exit()
    else:
        with open(file_words,"r") as f:
            for ligne in f:
                ligne = ligne.strip()
                words_list.append(unidecode.unidecode(ligne))
        return words_list


def pick_words(size:int)->str:
    #prendre un mot de la taille "size" dans votre stockage
    data_words = load_words()
    for word in data_words:
        if len(word) == size:
            list_words_size.append(word)
    return random.choice(list_words_size)

def is_valid(word: str ,words: list)->bool:
    # vérifier si le mot "word" existe dans la liste des mots
    if word not in words:
        return False
    else:
        return True

if __name__ == '__main__':
    result = pick_words(5)
    print(result)
    print(is_valid(result,list_words_size))