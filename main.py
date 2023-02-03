from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

    

class Scrape:

	def __init__(self):
		chromeOptions = webdriver.ChromeOptions()
		#prefs = {'profile.managed_default_content_settings.images':2}
		#chromeOptions.add_experimental_option("prefs", prefs)
		self.driver = webdriver.Chrome(chrome_options=chromeOptions)
		self.url_home = "https://lyricsmint.com/"

	def getSongList(self, artist):
		# print(self.url_home+artist+".html")
		self.driver.get(self.url_home+artist+".html")
		soup = BeautifulSoup(self.driver.page_source, 'html.parser')
		listItem = soup.find_all('div')
		# print(listItem)
		h3_elements = [div.find('h3') for div in listItem if div.find('h3')]
		# print(h3_elements)
		h3_text = [h3.text for h3 in h3_elements]
		h3_text = [*set(h3_text)]
		
		self.quit()
		return h3_text
  
	def quit(self):
		self.driver.quit()


def get_song_details(song_name, singer):
	
    chromeOptions = webdriver.ChromeOptions()
    driver = webdriver.Chrome(chrome_options=chromeOptions)
    url_home = "https://lyricsmint.com/"
    # print(url_home+song_name+".html")
    driver.get(url_home+song_name+".html")
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listItem = soup.find_all('p')
    p_text = [p.text for p in listItem if 'ADVERTISEMENT' not in p.text]
    # print(p_text[:6])
    driver.quit()

    details =  {
    'name' : song_name,
    'artist' : singer,
    'lyrics' : (" ").join(p_text[:6])
    }

    return details

if __name__ == "__main__":
	
    data = []
    artist_name = "arijit-singh"
    song_list = Scrape().getSongList(artist_name)
    print(song_list)

    for items in song_list[2:3]:
        res = get_song_details(items, artist_name)
        data.append(res)
    
    df = pd.DataFrame(data)
    df.to_csv("songs_database.csv")