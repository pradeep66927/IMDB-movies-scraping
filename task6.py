from task5 import get_movie_list_details
import json
from pprint import pprint

a = get_movie_list_details()
# print(type(a))

def analyse_movies_language ():
    dict_lang_details={}
    for i in a:
        for j in i["language"]:
            if j in dict_lang_details:
                dict_lang_details[j]+=1
            else:
                dict_lang_details[j]=1
                   
    pprint(dict_lang_details)
    
# analyse_movies_language()