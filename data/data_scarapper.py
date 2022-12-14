import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

topic_url = "https://rickandmorty.fandom.com/wiki/Rickipedia"

response = requests.get(topic_url)
page_contents = response.text
doc = BeautifulSoup(page_contents , 'html.parser')

topics_link_tags = doc.find_all('a' , {'class' : 'image link-internal'})

episode_url = 'https://rickandmorty.fandom.com' + topics_link_tags[8]['href']

response_episode = requests.get(episode_url)
episode_page_content = response_episode.text
doc_episode = BeautifulSoup(episode_page_content , 'html.parser')
doc_episode_tables = doc_episode.find_all('table')

b_tag = doc_episode_tables[1].find_all('b')
anchor_tag = b_tag[0].find('a')
link = 'https://rickandmorty.fandom.com' +anchor_tag['href']
print(anchor_tag[1]['title'])

doc_episode_title = doc_episode.find_all('span' , {'class' : 'mw-headline'})
print(doc_episode_title[2].contents)

def page_transcript(link , episode_num) :
    
    data = []

    response_episode_page = requests.get(link)
    page_content = response_episode_page.text

    doc_episode_page = BeautifulSoup(page_content , 'html.parser')
    para_tags = doc_episode_page.find_all('p')

    for tag in para_tags :
        try :
            if tag.find('b') == None:
                continue
            else :
                list_child = list(tag.children)
                dialouge = list_child[1]
                
                if list_child[0].find('a') == None :
                    name = list_child[0].contents[0]
                    # print(list_child[0].contents[0])

                else :
                    name = list_child[0].find('a').contents[0]
                    # print(list_child[0].find('a').contents[0])

        except Exception as e:
            continue
        
        data.append([episode_num , name , dialouge])
        
    print(data)
    return data

dataset_season = []
dataset_episode_title = []
dataset = []

j = 0
for i in range(1 , 6):
    # title = doc_episode_title[i+1].contents
    # dataset_season.append(title)
    table = doc_episode_tables[i]
    anchor_tags = doc_episode_tables[i].find_all('a')
    
    for tags in anchor_tags :
        
        try :
            dataset_episode_title.append(tags['title'])
            link = 'https://rickandmorty.fandom.com' +tags['href'] + '/Transcript'
            j+=1
            print(link , j)
            data = page_transcript(link=link , episode_num=j)
            dataset.append(data)
            
        except Exception as e:
            continue

   
    
print(dataset_episode_title)

print(dataset_season)
# dataset_episode_number = np.linspace(0 , )

# All content put in one p tag error


url_error = "https://rickandmorty.fandom.com/wiki/Pickle_Rick/Transcript"

response_error = requests.get(url_error)
content_error = response_error.text
doc_episode_error = BeautifulSoup(content_error , 'html.parser')

para_tag_error  = doc_episode_error.find('p')

text_error = para_tag_error.get_text()
text_error = text_error.rsplit("\n")

for text_e in text_error :
    try:
        text_e_i = text_e.rsplit(': ')
        dataset[23].append([24 , text_e_i[0] , text_e_i[1]])
    except Exception as e:
        continue
    