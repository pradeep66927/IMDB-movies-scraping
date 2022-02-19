from bs4 import BeautifulSoup
import requests , json
from pprint import pprint

file2=open("all_moviesT1.json","r")
movies=json.load(file2)

def group_by_year(movies):
    dict1={}
    for i in movies:
        # print(i)
        y=i["year"]
        if y not in dict1:
            dict1[y]=[]
        else:
            dict1[y].append(i)
            # pprint(dict1)
    with open('yearwise_movieT2.json','w') as f3:
        json.dump(dict1,f3,indent=4)
        return dict1       
pprint(group_by_year(movies))
    
    
    
    























###################################################################################

# scrapped = scrap_top_list()

# def group_by_year(movies):
#     years = []
#     for i in movies:
#         year = i["year"]
#         if year not in years:   # "not in " used for just not come same year again and again 
#             years.append(year)
#     movie_dict = {i:[]for i in years}
#     for i in movies:
#         year = i['year']
#         for x in movie_dict:
#             if str(x) == str(year):
#                 movie_dict[x].append(i)
#     return movie_dict
#     print(movie_dict)
# group_by_year(movies)

                
             
            
            
        
         
