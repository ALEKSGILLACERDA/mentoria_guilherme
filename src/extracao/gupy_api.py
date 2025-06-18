import requests
import json
import os
from typing import List, Dict, Any, Iterable

def buscar_vagas_por_termo(termo: str, offset: int):
    url = f'https://portal.api.gupy.io/api/job?name={termo}&offset={offset}&limit=10'
    print(f"🔎 Fazendo requisição para o termo '{termo}' no offset {offset}...")
    resposta = requests.get(url)
    if resposta.status_code == 200:
        vagas = resposta.json().get("data", [])
        print(f"{len(vagas)} vagas coletadas para o termo '{termo}', offset {offset}")
        return vagas
    else:
        print(f"Erro na busca: {termo} (offset {offset})")
    
    
    

def coletar_todas_as_vagas(termos: List[str], offsets: Iterable[int]):
    todas_as_vagas = []
    for termo in termos:
        for offset in offsets:
            vagas = buscar_vagas_por_termo(termo, offset)
            if vagas:
                todas_as_vagas.extend(vagas)
    print(f"📌 Finalizada a coleta para o termo: '{termo}'")
    return todas_as_vagas

def salvar_vagas_em_arquivo(vagas: List[Dict[str, Any]]):
    os.makedirs("dados", exist_ok=True)
    with open("dados/vagas_gupy.json", "w", encoding="utf-8") as arquivo:
        json.dump(vagas, arquivo, ensure_ascii=False, indent=2)
        print(f" Arquivo salvo com {len(vagas)} vagas.")


    