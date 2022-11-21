import os
import sys
import platform
import wikipediaapi

__platform__ = sys.platform 
match __platform__[0]:
    case 'l':
        SLASH='/'
    case 'w':
        SLASH='\\'
    case 'd':
        SLASH ='/'

ALPHAX = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHA = [x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
alpha = [x.lower() for x in ALPHA]
ok_fine = "-_'`&@"
punctuationx = '!?.,:;"[]}{()*&^%$#~\n\t'
punctuation = [x for x in punctuationx]


class WordBank:
    def __init__(self, about, to_file=True):
        self.about = about
        self.page = get_page_about(self.about)
        self.wordlist = wikipedia_page_to_word_list(self.page)
        if to_file:
            parse_words_to_file(self.wordlist)

    def about(self, topic):
        get_words_about(topic)



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

def parse_words_to_file(words):
    curdir = os.getcwd()
    for word in words:
        first = word[0]
        second = word[1]
        super_path = f"{curdir}{SLASH}words{SLASH}{first}{SLASH}{first}{second}" 
        with open(super_path, "a") as afile:
            xword = str(word).strip()
            afile.write(f"{xword}\n")
        print(f"[ {xword} ] added to file: {super_path}")

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
        print("""Ex: python3 main.py "Max Keeble's big move" """)

