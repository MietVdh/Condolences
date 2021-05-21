# Condolences
Web scraper to collect condolences from funeral home webpage
Creates a .html file with the name of the deceased at the top, and comments in chronological order (oldest first).
Creates a .html helper file that lists comments in reverse chronological order.

Use a config.py file to enter the relevant information, or enter directly into condolences.py file:


mainURL : URL for homepage of funeral home, or wherever condolences are located
EXCL_AUTH : authors of any comments you do not want included, such as replies by family members
NAME : Name of the deceased, as you would like it on top of the page
DATES : Dates of birth and death, in the format you would like it added to the html file.
FILENAME : filename for the html file - don't include .html extension

