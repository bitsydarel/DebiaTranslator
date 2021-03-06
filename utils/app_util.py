# coding=utf-8
import platform
import sqlite3

from utils.constant_holder import *
from pages import add_word, translate_word, welcome, modify_word, remove_word


def get_welcome_page():
    return welcome.WelcomeWindow


def get_translate_page():
    return translate_word.TranslatePage


def get_add_word_page():
    return add_word.AddWordPage


def get_modify_word_page():
    return modify_word.ModifyWordPage


def get_remove_word_page():
    return remove_word.RemoveWordPage


def get_database():
    if platform.system() == "Windows":
        if (os.path.isdir(DISK_NAME + "\DTranslator")):
            os.chdir(DISK_NAME + "\DTranslator")
        else:
            os.mkdir(DISK_NAME + "\DTranslator")
            os.chdir(DISK_NAME + "\DTranslator")

    if os.path.exists("dictionary.db"):
        return sqlite3.connect("dictionary.db")
    else:
        connection = sqlite3.connect("dictionary.db")
        connection.execute('''CREATE TABLE dictionary (word_key text , word_value text)''')
        connection.commit()

        one_letter_map = {'k': 'b', 'j': 'c', 'f': 'd', 'i': 'e', 'y': 'f',
                          'w': 'g', 'l': 'h', 'o': 'i', 'v': 'k', 'b': 'l',
                          'h': 'm', 'd': 'n', 'u': 'o', 'p': 'r', 'g': 's',
                          'm': 't', 's': 'v', 'c': 'w', 'a': 'y', 'x': 'z',
                          "e’": 'a', "no’": 'j', "nu’": 'p', "na’": 'q', "ni’": 'u',
                          "ne": 'x', "e'": 'a', "no'": 'j', "nu'": 'p',
                          "na'": 'q', "ni'": 'u'}

        for key, value in one_letter_map.items():
            connection.execute(INSERT_INTO, (key, value))
            connection.commit()

        return connection
