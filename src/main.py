from gupy_api import coletar_todas_as_vagas, salvar_vagas_em_arquivo
from config import termos_de_busca, offsets

def main():
    vagas = coletar_todas_as_vagas(termos_de_busca, offsets)
    salvar_vagas_em_arquivo(vagas)

if __name__ == "__main__":
    main()