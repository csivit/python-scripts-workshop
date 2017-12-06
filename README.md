# CSI python scripts 

Learn shortcuts to automate simple, everyday tasks.


### Prerequisites

Check if you have python3 installed by typing the following in the cmd or terminal.
```
$ python3 --version
```

### Installing

Follow the guide by [Django Girls](https://tutorial.djangogirls.org/en/)

[Installation process](https://tutorial.djangogirls.org/en/python_installation/)



## Getting Started

* [What is a script?](http://whatis.techtarget.com/definition/script)
* [Script vs Program](https://stackoverflow.com/questions/2286552/difference-between-a-script-and-a-program)


## Demo scripts

* [trello-youtube-dl](https://github.com/akigugale/trello-youtube-dl)
* [address-finder](./scripts/address_finder.py)
* pretty-episode-name


## pretty-episode-name
What you usually do is,
1. Navigate to the folder & display the list of files
2. Enter the extension of the files to rename
3. Get the SEASON NUMBER from the old name
4. List old name and new name & confirm RENAMING

With python3 active on your terminal or cmd use the following commands to learn:
``` py
# basics of os and navigation
import os
os.name
os.getcwd()  
os.chdir('path')  # windows (C:\Desktop\csi-python-scripts) & use "" for spaces
os.path.splitext(x)[-1]  # to get the file extension
for x in os.listdir():
	print(os.path.splitext(x)[-1],'\n')


# Let's rename the cover photo:
os.rename('cover.jpg', 'art.jpg')


# Regex - identify the season name
for i in os.listdir():
	print(re.findall("S..E..",i))
```

## Pip

* What are packages or modules in python?
* Why use pip?
* [Tutorial](https://www.youtube.com/watch?v=tn8L_u2pAaI)

## Cricket score

```py
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url="http://www.cricbuzz.com/"
Client=uReq(my_url)

html_page=Client.read()
Client.close()

soup_page=soup(html_page,"html.parser")

score_box=soup_page.findAll("div",{"class":"cb-col cb-col-25 cb-mtch-blk"})
l = len(score_box)
print(l)
for i in range(l):
	print(score_box[i].a["title"])
	print(score_box[i].a.text)
	print()
```
## Other scripts

* https://github.com/geekcomputers/Python
* https://github.com/realpython/python-scripts
* https://github.com/averagesecurityguy/Python-Examples
* http://www.geeksforgeeks.org/facebook-login-using-python/

## Speakers

* **Akshay Gugale** - [akigugale](https://github.com/akigugale)
* **Hitesh Mandhyan** - [Hitesh-VIT](https://github.com/Hitesh-VIT)
* **Palash Golecha** - [palashgo](https://github.com/palashgo)
* **Pradyun Gedam** - [pradyunsg](https://github.com/pradyunsg)

