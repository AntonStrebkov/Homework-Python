from model import open_csv
from model import open_txt
from view import quest_user
from model import add_csv
from view import add_text

def open_file():
    choice = quest_user()
    if choice == 1:
        open_txt()
    if choice == 2:
        open_csv()

