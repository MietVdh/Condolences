from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/condolences", methods=["POST"])
def condolences():
    src_url=request.form.get("src-url")
    excl_auth_str=request.form.get("excl-auth")
    add_date=request.form.get("date")
    
    excl_auth=excl_auth_str.splitlines()
    plain_excl_auth = []
    for auth in excl_auth:
        plain_excl_auth.append(auth.strip())
    URLS = [src_url]
    r = requests.get(URLS[0])
    soup = BeautifulSoup(r.content, 'html.parser')
    photoDiv = soup.find('div', class_="deceased-img")
    PHOTO=photoDiv.img
    PHOTO_URL = PHOTO['src']
    NAME = soup.find(class_='deceased-name').text
    birth_info = soup.find('div', class_='deceased-born-place-and-date')
    birth_string = birth_info.find('p').find('span', class_='deceased-info-body').text
    birth_string = " ".join(birth_string.split())
    BIRTH_DATE = birth_string.split(' op ')[1]
    death_info = soup.find('div', class_='deceased-death-place-and-date')
    death_string = death_info.find('p').find('span', class_='deceased-info-body').text
    death_string = " ".join(death_string.split())
    DEATH_DATE = death_string.split(' op ', 1)[1]

    pages = soup.find_all("a", class_="page-numbers", href=True)
    for page in pages:
        fullURL = "https://begrafenissen-rummens.be" + page.get("href")
        if fullURL not in URLS: 
            URLS.append(fullURL)
    condolences_list = []

    for URL in URLS:

        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html.parser')

        commentlist = soup.find('ol', class_ = 'commentlist')
        comments = commentlist.find_all('li', class_='depth-1')

        for comment in comments:
            try:
                author = comment.find('cite', class_='fn')
                authorPlain = author.text.strip()
                if authorPlain in plain_excl_auth:
                    continue
                dateDiv = comment.find('div', class_='comment-meta')
                date = dateDiv.find('a')
                commentText = comment.find('p')
               
                datePlain = date.text.strip()
             
                if add_date == "date":
                    dateFinal = "- " + datePlain.split(" om")[0]
                elif add_date == "date-time":
                    dateFinal = "- " + datePlain
                else:
                    dateFinal = ""

                commentPlain = commentText.text.strip()
                commentDict = {
                    "author": authorPlain,
                    "comment": commentPlain,
                    "date": dateFinal
                }
        
                condolences_list.append(commentDict)

            except:
                # print id of comments that do not get added to file
                print(comment['id'])
                continue
    print(len(condolences_list))
    # print_condolences(src_url, excl_auth)
    return render_template("condolences.html", dec_name=NAME, dec_dob=BIRTH_DATE, dec_dod=DEATH_DATE, 
    comments=condolences_list, picture_url=PHOTO_URL)