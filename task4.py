
import requests,json
from bs4 import BeautifulSoup
from pprint import pprint
# from lxml import etree

def scrape_movie_details(movie_url):
    page=requests.get(movie_url)
    #########   movie  name **********************************
    soup=BeautifulSoup(page.text,"html.parser")
    title_dive=soup.find("h1",class_="TitleHeader__TitleText-sc-1wu6n3d-0 dxSWFG").get_text()


    #*********************** run times of movie *********************************************************##
    sub_div = soup.find("li", attrs={"data-testid":"title-techspec_runtime"}).div.get_text()
    
    
    movierun_time=soup.find("ul",attrs={"data-testid":"hero-title-block__metadata"}).findAll("li")[2].get_text()
    runtime_hours=int(movierun_time[0])*60
    if "m" in movierun_time:
        runtime_minuts=int(movierun_time[3:].strip("m"))
        movierun2_time=runtime_hours+runtime_minuts
    else:
        movierun_time=runtime_hours
    # return movierun2_time
       
    ###########  genre #######################################################################
    
    genre = []
    genre_div=soup.find("li",attrs={"data-testid":"storyline-genres"}).find("div").find("ul").findAll("li")
    for i in genre_div:
        genre.append(i.get_text())
        

######## "bio"  of the movie    #################################################################

    bio_span=soup.find("span",attrs={"data-testid":"plot-xl"}).get_text()
    # return bio_span

##########    director name ########################################################3
    director=[]
    director_name=soup.find("li",attrs={"data-testid":"title-pc-principal-credit"})
    dd = director_name.find('a').text
    director.append(dd)
    # print(dd)
    
    # return director

###########   country name #####################################################################

    country_name=soup.find("li",attrs={"data-testid":"title-details-origin"})
    country=[]
    for i in country_name:
        country.append(i.get_text())
    
    # print(country[1]) 
    # return country
    
######    language #####################################################################3
    
    language = []
    lang_div=soup.find("li",attrs={"data-testid":"title-details-languages"}).find("div").find("ul").findAll("li")
    for i in lang_div:
        language.append(i.get_text())
    # return language

############  poster url ######################################################################

    # poster_movies_link=soup.find("div",attrs={"cel_widget_id":"DynamicFeature_HeroPoster"}).a["href"]
    poster_movies_link=soup.find("img",class_="ipc-image")['src']
    # movie_poster="https://www.imdb.com"+poster_movies_link
    
    # return poster_movies_link
    
    
    ##########  main dictionary formate as task-4 ###############################
    main_movie_dict={"name":"","director":"","bio":"","runtime":"","genre":"","language":"","country":"","poster_image_url":""}
    
    main_movie_dict["name"]=title_dive
    main_movie_dict["director"]=director
    main_movie_dict["bio"]=bio_span
    main_movie_dict["runtime"]=movierun2_time
    main_movie_dict["genre"]=genre
    main_movie_dict["language"]=language
    main_movie_dict["country"]=country[1]
    main_movie_dict["poster_image_url"]=poster_movies_link
    
    task4=main_movie_dict
    with open("single_movieT4.json","w") as f5:
        json.dump(task4,f5,indent=4)
    
    return main_movie_dict
url1="https://www.imdb.com/title/tt0066763/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=690bec67-3bd7-45a1-9ab4-4f274a72e602&pf_rd_r=QHWV4XQ5D12M18Y3QQYJ&pf_rd_s=center-4&pf_rd_t=60601&pf_rd_i=india.top-rated-indian-movies&ref_=fea_india_ss_toprated_tt_68"

# pprint(scrape_movie_details(url1))  # https://www.imdb.com/title/tt0066763/mediaviewer/rm2015744257/