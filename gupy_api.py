import requests
import json

# Dicionário para garantir que cada vaga apareça só uma vez (chave = id da vaga)
vagas_unicas = {}

def buscar_vagas():
    # Termos que serão usados para buscar vagas no portal da Gupy
    palavras_chave = [
        "analista de dados jr",
        "dados junior",
        "data analyst jr",
        "analista dados júnior",
        "ciência de dados jr",
        "data science jr"
    ]

    for termo in palavras_chave:
        url = f'https://portal.api.gupy.io/api/job?name={termo}&offset=0&limit=400'
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            dados = resposta.json()

            # Para cada vaga retornada na resposta
            for vaga in dados.get("data", []):
                # Usa o id da vaga como chave no dicionário para evitar duplicatas
                vagas_unicas[vaga["id"]] = vaga

    # Salva as vagas únicas em um arquivo JSON
    with open("vagas_gupy.json", "w", encoding="utf-8") as arquivo:
        json.dump(list(vagas_unicas.values()), arquivo, ensure_ascii=False, indent=2)