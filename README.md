# CONDOLENCES
#### Description:
Condolences is a web app that allows clients of a specific Belgian funeral home ([Begrafenissen Rummens](https://begrafenissen-rummens.be/)) to generate a printable list of all the condolence messages left on the website.

The project was made with Flask and deployed using Heroku ([link here](https://peaceful-journey-39065.herokuapp.com/)). The webscraping is done with BeautifulSoup. For styling, I used the Bulma framework.

The main code for the app is in the app.py file. The static folder holds the css file that specifies how to print the data, and the html files are in the templates folder. All dependencies are listed in requirements.txt, and the Procfile file holds instructions for Heroku.

The main page contains a form where users can enter the link they received from the funeral home to access (and respond to) messages of condolences. They can choose to enter names of people whose messages they don't want to include. This should not be necessary in most cases, but sometimes replies to messages get added as a new seperate message rather than as a reply, and this option allows users to filter out those replies.
Finally, users can choose to add the date or date and time each message was posted.

When users submit this information, a page is generated that lists all the messages in chronological order. At the top of the page is the name of the deceased, followed by the dates of birth and death. Then the messages follow.

This page is formatted to be easy to print, and messages don't break when printing.

I don't store any information, because the app works fine without it, and privacy is very important to me.

#### Why this project
This project is obviously only useful to a very small number of people, but I wanted to create something that had an actual use, and not just yet another to-do app. Earlier this year, my dad died unexpectedly, and 2 months later my great-aunt died. My mom asked me to collect the messages left after my aunt died, so my grandmother could read them (she doesn't do technology). 
Rather than go through all the messages manually and copy-paste, I thought it would be more interesting to write some code to extract the messages. That way, I could do the same thing for the condolences for my dad. 
When my great-uncle died a few weeks ago, I wanted to offer gathering the messages to his daughter, but I didn't want to ask for the link, because those messages can be very personal. So I decided to turn the code I had into a web app, so anyone can use it without having to give me access to their link.
