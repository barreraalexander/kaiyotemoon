from server.database import get_db
from server.models import Poem
from server.schemas import PoemCreate
from secrets import token_hex
from os import path, listdir

def run():
    poems_path = path.expanduser("~/drive/main_lit/poems/edits/")
    # print (poems_path)
    poems = listdir(poems_path)

    poem_dicts = []
    for poem in poems:
        absolute_path = path.join(poems_path, poem)
        poem_title, _ext = poem.split('.txt')
        poem_title = poem_title.replace('_',"'")
        with open(absolute_path, 'r') as f:
            lines = f.readlines()
            poem_content = ""
            for line in lines:
                poem_content += line


        poem_dict = {
            "title" : poem_title,
            "content" : poem_content
        }
        poem_dicts.append(poem_dict)

    for poem_dict in poem_dicts:
        new_poem = Poem(**poem_dict)    
    return poem_dicts