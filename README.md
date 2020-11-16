# Como criar um JSON a partir de uma dicionário python

## Escrevendo um arquivo
A maneira mais fácil de gravar seus dados no formato JSON em um arquivo usando Python é armazenar seus dados em um objeto dict, que pode conter outros dicts aninhados, arrays, booleanos ou outros tipos primitivos como inteiros e strings.

O pacote json integrado possui o código mágico que transforma seu objeto Python dict na string JSON serializada.

```python
import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
```
