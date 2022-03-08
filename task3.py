from  pprint import  pprint
# from task2 import movies
import requests,json
from bs4 import BeautifulSoup

#####**** third task content ***********#############################

file4=open("yearwise_movieT2.json","r")
b=json.load(file4)
def group_by_decade(movies):
    
    moviedec={}
    list1=[]
    for index in movies:
        mod=int(index)%10
        decade=int(index)-mod
        if decade not in list1:
            list1.append(decade)
            moviedec[decade]=[]
            dec10=decade+9
            for x in movies:
                if int(x)<=dec10 and int(x)>=decade:
                    (moviedec[decade]).extend(movies[x])
                        
    # with open('decademovieT3.json', 'w') as f:
        # json.dump(moviedec, f, indent=4)
    return moviedec                
# pprint(group_by_decade(b))


