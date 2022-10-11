import requests
from bs4 import BeautifulSoup

#находим xG для обеих команд в игре
def find_xg(url = "https://soccer365.ru/games/1743335/"):
    
    
    headers = {
    
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
        }
    req = requests.get(url,headers=headers)


    src = req.text

    #print(src)






    with open("index.html","w",encoding="utf-8") as file:

        file.write(src)

    with open("index.html",encoding="utf-8") as file:

        readpls=file.read()

    soup = BeautifulSoup(readpls,"lxml")

    xg =soup.find("div",class_="stats_inf").next_element
    next_el=soup.find("div",class_="stats_inf").next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
    #print(xg)
    #print(next_el)
    #for item in xg:
    return xg,next_el
    #print(item)



#получаем список ссылок на каждую команду
def table_of_league(ref="https://soccer365.ru/competitions/13/"):

    req1 = requests.get(ref)


    src = req1.text

    with open("index.html","w",encoding="utf-8") as file:

        file.write(src)

    with open("index.html",encoding="utf-8") as file:

        readpls=file.read()

    soup = BeautifulSoup(readpls,"lxml")

    ref_for_team =soup.find(id="competition_table").find_all("a")
    
    for item in ref_for_team:
        
        item_text=item.text
        item_url=item.get("href")
        #print(f"{item_text}:{item_url}")
        #print("https://soccer365.ru"+item_url)
        #i=ref_of_5games("https://soccer365.ru"+item_url)
#получаем список на 5 последних игр для команды по ссылке из таблицы

def ref_of_5games(ref):
    
    req1 = requests.get(ref)


    src = req1.text

    with open("index.html","w",encoding="utf-8") as file:

        file.write(src)

    with open("index.html",encoding="utf-8") as file:

        readpls=file.read()

    soup = BeautifulSoup(readpls,"lxml")

    
    last_game1=soup.find("div",class_="block_body_nopadding").find("div",class_="game_block").find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()#взять 6 game_block
    #достать ссылку на шестую игру
    #last_game2
    #last_game3
    #last_game4
    #last_game5
    
    print(last_game1)
    return 0
    


#print(find_xg())

ref_of_5games("https://soccer365.ru/clubs/52/")