from task4 import scrape_movie_details

import requests,json
from pprint import pprint
from bs4 import BeautifulSoup

with open("all_moviesT1.json","r") as f5:
    ff5=json.load(f5)
    # print(len(ff5))
    
def get_movie_list_details():
    list_moviesT5=[]
    for i in ff5[:10]:
        list_moviesT5.append(scrape_movie_details(i["url"]))
    #print(len(list_moviesT5))   # to checking only length
    f=open("imdb_movie_detailT5.json","w")
    json.dump(list_moviesT5,f,indent=4)
    f.close()
    return list_moviesT5    
# pprint(get_movie_list_details())

