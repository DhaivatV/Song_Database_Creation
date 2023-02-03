from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time

    

class Scrape:

	def __init__(self):
		chromeOptions = webdriver.ChromeOptions()
		#prefs = {'profile.managed_default_content_settings.images':2}
		#chromeOptions.add_experimental_option("prefs", prefs)
		self.driver = webdriver.Chrome(chrome_options=chromeOptions)
		self.url_home = "https://lyricsmint.com/"

	def getSongList(self, artist):
		print(self.url_home+artist+".html")
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


def get_song_details(song_name):
	
    chromeOptions = webdriver.ChromeOptions()
    driver = webdriver.Chrome(chrome_options=chromeOptions)
    url_home = "https://lyricsmint.com/"
    print(url_home+song_name+".html")
    driver.get(url_home+song_name+".html")
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    listItem = soup.find_all('p')
    # print(listItem)
    # p_elements = [div.find('p') for div in listItem if div.find('p')]
    # print(p_elements)
    p_text = [p.text for p in listItem if 'ADVERTISEMENT' not in p.text]
    print(p_text[:6])
    
    driver.quit()
	

song_list = Scrape().getSongList("arijit-singh")

for items in song_list:
	get_song_details(items)