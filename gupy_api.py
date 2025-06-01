import requests
import json

def buscar_vagas_por_termo(termo, offset):
    url = f'https://portal.api.gupy.io/api/job?name={termo}&offset={offset}&limit=10'
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        vagas = dados.get("data", [])
        print(f'guardado {len(vagas)}')
        return dados.get("data", [])
        
    else:
        print(f"Erro ao buscar '{termo}' com offset {offset}: status {resposta.status_code}")
        return []

def coletar_todas_as_vagas(vagas, offsets):
    todas_as_vagas = []
    for termo in vagas:
        for offset in offsets:
            vagas_encontradas = buscar_vagas_por_termo(termo, offset)
            todas_as_vagas.extend(vagas_encontradas)
        print ("buscando vagas")
    return todas_as_vagas
    

def salvar_vagas_em_arquivo(vagas, nome_arquivo):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(vagas, arquivo, ensure_ascii=False, indent=2)
    print(f"Arquivo '{nome_arquivo}' salvo com {len(vagas)} vagas.")

def main():
    termos_de_busca = [
        "analista de dados jr",
        "dados junior",
        "data analyst jr",
        "analista dados júnior",
    ]
    offsets = range(0, 50, 10)

    todas_as_vagas = coletar_todas_as_vagas(termos_de_busca, offsets)
    salvar_vagas_em_arquivo(todas_as_vagas, "vagas_gupy.json")

if __name__ == "__main__":
    main()

 
   

