from server.models import Poem
from os import path, listdir

def run():
    poems_path = path.expanduser("./server/static/poems")
    poems = listdir(poems_path)

    poem_dicts = []
    for i,poem in enumerate(poems):
        absolute_path = path.join(poems_path, poem)
        poem_title, _ext = poem.split('.txt')
        poem_title = poem_title.replace('_',"'")
        with open(absolute_path, 'r') as f:
            lines = f.readlines()
            poem_content = ""
            for line in lines:
                poem_content += line


        poem_dict = {
            "id" : i,
            "title" : poem_title,
            "content" : poem_content
        }
        poem_dicts.append(poem_dict)

    for poem_dict in poem_dicts:
        new_poem = Poem(**poem_dict)
    return poem_dicts