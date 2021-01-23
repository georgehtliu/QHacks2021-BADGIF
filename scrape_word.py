from bs4 import BeautifulSoup
import requests
import pandas as pd
import random


def get_random_happy_word():
    word = "happy"
    url = "https://www.enchantedlearning.com/wordlist/"+word+".shtml"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    words = soup.find_all('div', attrs={'class': 'wordlist-item'})
    last_index = len(words) - 1
    index = random.randint(0, last_index)
    got_word = words[index].get_text()

    return word+"-"+got_word


def get_random_sad_word():
    word = "sad"
    url = "https://www.thesaurus.com/browse/sad"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    words = soup.find_all('a', attrs={'class': 'css-1m14xsh eh475bn1'})
    last_index = len(words) - 1
    index = random.randint(0, last_index)
    got_word = words[index].get_text()

    return word+"-"+got_word


print(get_random_sad_word())
print(get_random_happy_word())
