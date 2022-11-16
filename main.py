import os
import sys
import wikipediaapi

ALPHAX = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHA = [x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
alpha = [x.lower() for x in ALPHA]
ok_fine = "-_'`&@"
punctuationx = '!?.,:;"[]}{()*&^%$#~\n\t'
punctuation = [x for x in punctuationx]

def get_page_about(topic):

    wikipedia_helper = wikipediaapi.Wikipedia(
        language='en',extract_format=wikipediaapi.ExtractFormat.WIKI)
    wikipedia_page = wikipedia_helper.page(topic)
    return wikipedia_page.text

def wikipedia_page_to_word_list(page):
    mypage = str(page)

    current_word = []

    words = []

    for character in mypage:

        current_char = character

        if current_char in ALPHA:
            current_word.append(current_char)
            continue

        if current_char in alpha:
            current_word.append(current_char)
            continue
        
        if current_char == " ":
            if current_word != "":
                words.append("".join(current_word).strip())
                current_word = []
                continue
            else:
                continue

        if current_char in punctuation:
            if current_word != []:
                words.append("".join(current_word).strip())
                current_word = []
                continue  
            else:
                continue

    non_repeating_words = set(words)

    plist = list(non_repeating_words)

    mywords2have = []

    for word in plist:
        length = len(word)
        if length < 2:
            continue
        else:
            xword = str(word).lower()
            mywords2have.append(xword)

    return mywords2have

def show_word_collection(_words):
    for word in _words:
        print(word)

def parse_words_to_file(words):

    curdir = os.getcwd()

    for word in words:

        first = word[0]
        second = word[1]

        super_path = f"{curdir}\\words\\{first}\\{first}{second}" 

        with open(super_path, "a") as afile:
            xword = str(word).strip()
            afile.write(f"{xword}\n")
        
        print(f"[ {xword} ] added to file: {super_path}")


dolphs = get_page_about("Dolphins")

mywords = wikipedia_page_to_word_list(dolphs)

parse_words_to_file(mywords)


def get_words_about(this_topic):

    mytopic = get_page_about(this_topic)

    words_on_topic = wikipedia_page_to_word_list(mytopic)

    parse_words_to_file(words_on_topic)
    

if __name__ == '__main__':
    from sys import argv

    try:
        xtopic = argv[1]
        get_words_about(xtopic)
    except:
        print("please specify the topic as an argument")
        print("Ex: python3 main.py 'Max Keeble's big move' ")

