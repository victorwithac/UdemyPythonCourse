import json

dados = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Abre um arquivo para escrita
with open("dados.json", "w") as arquivo:
    # Usa json.dump() para escrever o dicionário no arquivo
    json.dump(dados, arquivo, indent=4)