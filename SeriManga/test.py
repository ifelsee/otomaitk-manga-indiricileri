import requests 
import wget
from bs4 import BeautifulSoup
import time
import os 
#<img class="chapter-pages__item mt-1 mb-1" data-number="5" data-src="https://serimanga.com/uploads/2018/12/15/pTsfbTRJbeeldRl.jpg" style="display:none"/>

def download_chapter(req,episode):
    req = req
    episode = episode
    soup  = BeautifulSoup(req.content, 'html.parser')
    manga_links = soup.find_all("img")
    have_episode = False 

  
    try:
        os.mkdir(episode)
    except:print("dosya yaratılamadı")
    os.chdir(episode)
    print(f"İNDİRİLEN BÖLÜM {episode} \n ------------------- \n")
    for i in manga_links:
        if str(i.get("data-src")).find("uploads") != -1:
            get_data_number = str(i.get("data-number")) 
            get_data_src = str(i.get("data-src"))
            have_chapter = False 
            
            for c in os.listdir():
                if c[:-4] == get_data_number:
                    print("dirs num = ",c, "  chapter num = ", get_data_number)
                    have_chapter = True
                    break
            if get_data_src[-3:] =="jpg" and have_chapter == False: 
                try:
                    response = requests.get(get_data_src)
                    with open(f"{get_data_number}.jpg","wb") as file:
                        file.write(response.content)
                        print(f"{get_data_number}.jpg  İndirildi ✔ ") 
                except KeyboardInterrupt:
                    print(f"En son İndirilen bölüm {episode} ")
                    quit()
            else:pass
    os.chdir("../")
                



def find_episode():
    episode = 1
    episode_finder = True    
    while episode_finder:
        
        req = requests.get(f"https://serimanga.com/manga/please-dont-bully-me-nagatoro-san/{episode}")
        if req.status_code == 200:
            
            download_chapter(req=req, episode = str(episode))

        episode= episode +1            






def main():
     
    anime_name = "please-dont-bully-me-nagatoro-san" 
    try:
        os.mkdir(anime_name)

    except:pass

    os.chdir(anime_name)

    find_episode()

main()
