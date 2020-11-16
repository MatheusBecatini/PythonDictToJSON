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
## Lendo um arquivo JSON

Ler dados JSON de um arquivo é tão fácil quanto gravá-los em um arquivo. Usando o mesmo pacote 'json' novamente, podemos extrair e analisar a string JSON diretamente de um objeto de arquivo. No exemplo a seguir, fazemos exatamente isso e, em seguida, imprimimos os dados que obtivemos:

```python
import json

with open('data.json') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
```

## Informações uteis
### Pretty-Printing
Tornar JSON legível (também conhecido como "impressão bonita") é tão fácil quanto passar um valor inteiro para o parâmetro indent:
```python
>>> import json
>>> data = {'people':[{'name': 'Scott', 'website': 'stackabuse.com', 'from': 'Nebraska'}]}
>>> json.dumps(data, indent=4)
```
E teremos: 
```json
{
    "people": [
        {
            "website": "stackabuse.com", 
            "from": "Nebraska", 
            "name": "Scott"
        }
    ]
}
```

### ASCII Text (Texto com acentos)
Por padrão, json.dump garantirá que todo o seu texto no dicionário Python fornecido seja codificado em ASCII. Se caracteres não ASCII estiverem presentes, eles serão escapados automaticamente:
```python
>>> import json
>>> data = {'item': 'Cerveja', 'cost':'R$4.00'}
>>> jstr = json.dumps(data, indent=4)
>>> print(jstr)
{
    "item": "Cerveja",
    "cost": "\u00a34.00"
}
```

Isso nem sempre é aceitável e, em muitos casos, você pode querer manter seus caracteres Unicode intactos. Para fazer isso, defina a opção garantir_ascii como False.
```python
>>> jstr = json.dumps(data, ensure_ascii=False, indent=4)
>>> print(jstr)
{
    "item": "Cerveja",
    "cost": "R$4.00"
}
```

**Fonte**:https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/ 

