import requests
import json  # Biblioteca para trabalhar com arquivos JSON

def buscar_vagas():
    vagas = [
        "analista de dados jr",
        "dados junior",
        "data analyst jr",
        "analista dados júnior",
        "ciência de dados jr",
        "data science jr"
    ]

    conjunto_vagas = set()

    for vaga in vagas:
        url = f"https://portal.api.gupy.io/api/job?name={vaga}&offset=0&limit=400"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()
            vagas_encontradas = dados.get("data", [])

            for v in vagas_encontradas:
                tupla_vaga = (
                    v.get("name"),
                    v.get("careerPageName"),
                    v.get("city"),
                    v.get("workplace") == "remote",
                    f"https://{v.get('careerPageSlug')}.gupy.io/job/{v.get('id')}"
                )
                conjunto_vagas.add(tupla_vaga)

    # Converte as tuplas em dicionários antes de salvar em JSON
    lista_vagas = [
        {
            "titulo": vaga[0],
            "empresa": vaga[1],
            "cidade": vaga[2],
            "remoto": vaga[3],
            "link": vaga[4]
        }
        for vaga in conjunto_vagas
    ]

    # Salva em arquivo JSON
    with open("vagas.json", "w", encoding="utf-8") as f:
        json.dump(lista_vagas, f, ensure_ascii=False, indent=2)

buscar_vagas()