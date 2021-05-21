import requests
from bs4 import BeautifulSoup

import config

URLS = [config.papaUrl]
EXCL_AUTH = config.papaExcl
NAME = config.papaNaam
DATES = config.papaData
FILENAME = config.papaFileNaam
PHOTO_URL = ""

r = requests.get(URLS[0])
soup = BeautifulSoup(r.content, 'html.parser')

targetFile = '.\\' + FILENAME + '.html'

pages = soup.find_all("a", class_="page-numbers", href=True)
for page in pages:
    fullURL = config.mainURL + page.get("href")
    if fullURL not in URLS: 
        URLS.append(fullURL)

for URL in URLS:

    print(URL)

    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')

    commentlist = soup.find('ol', class_ = 'commentlist')
    comments = commentlist.find_all('li', class_='depth-1')

    with open(targetFile, 'a', encoding="utf-8") as outfile:

        for comment in comments:
            try:
                author = comment.find('cite', class_='fn')
                dateDiv = comment.find('div', class_='comment-meta')
                date = dateDiv.find('a')
                commentText = comment.find('p')

                authorPlain = author.text.strip()
                datePlain = date.text.strip()
                commentPlain = commentText.text.strip()
                if authorPlain in EXCL_AUTH:
                    continue
                
                outfile.write(str('<article class="bericht">'))
                
                outfile.write(str(commentText.prettify()))
                outfile.write('\n')
                outfile.write(str(author.prettify()))
                outfile.write(' - ' + datePlain)

                outfile.write(str('<br>'))
                outfile.write(str('</article>'))

            except:
                print(comment['id'])
                continue
        


with open('.\\chrono' + FILENAME + '.html', 'a', encoding="utf-8") as newfile:
    with open(targetFile, encoding="utf-8") as reverse_chron:
        newfile.write(str(NAME))
        newfile.write(str(PHOTO_URL))

        new_soup = BeautifulSoup(reverse_chron.read(), "html.parser")
        berichten = new_soup.find_all('article')
    

        for i in range(len(berichten)-1, -1, -1):
            newfile.write(str(berichten[i].prettify()))


    


    






