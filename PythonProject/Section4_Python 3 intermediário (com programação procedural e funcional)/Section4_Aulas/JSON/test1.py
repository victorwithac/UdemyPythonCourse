import json

dados = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Serializa os dados em uma string JSON
json_string = json.dumps(dados, indent=4)

# Exibe a string JSON resultante
print(json_string)