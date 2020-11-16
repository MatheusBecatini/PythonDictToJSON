# -*- coding: utf-8 -*-
__author__ = 'Matheus Becatini'
__version__ = '0.1.0'

import os
import json


NAME = 'Artigos'

if (os.path.exists('data.json')):
    with open('data.json') as json_file:
        data = json.load(json_file)
else:
    data={}
    data[NAME]=[]

title = 'O titulo é tal 3333'
text = 'Dia da República é uma data histórica que comemora a instituição do sistema republicano[1] de governo em um determinado país ou região. Em alguns países, é conhecido como Dia Nacional ou Dia da Proclamação, ou por algum outro nome.'
url = 'https://wikipedia.readthedocs.io/en/latest/'

data[NAME].append({
    'title': title,
    'content': text,
    'url': url
})

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4, ensure_ascii=False)


