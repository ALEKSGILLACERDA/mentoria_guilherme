import requests
import json  
todas_as_vagas = []
def buscar_vagas():
    vagas = ["analista de dados jr",
             "dados junior",
             "data analyst jr",
             "analista dados júnior",
             "ciência de dados jr",
             "data science jr"]
    
    
    for vaga in vagas:
        url = f'https://portal.api.gupy.io/api/job?name={vaga}&offset=0&limit=400'
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            todas_as_vagas.extend(dados.get("data", []))

    with open("vagas_gupy.json", "w", encoding="utf-8") as gupy:
         json.dump(todas_as_vagas, gupy, ensure_ascii=False, indent=2)
buscar_vagas()