from gupy_api import coletar_todas_as_vagas
from gupy_api import salvar_vagas_em_arquivo
from typing import List, Optional

def main(termos_de_busca: Optional[List[str]] = None, offset_final: int = 640) -> None:
    """função principal que define os termos padrão e o limite de páginas, se não for passado nenhum parâmetro externo"""
    if termos_de_busca is None:
        termos_de_busca = [
            "dados"
        ]
    offsets = range(0, 640, 10)

    todas_as_vagas = coletar_todas_as_vagas(termos_de_busca, offsets)
    salvar_vagas_em_arquivo(todas_as_vagas, "vagas_gupy.json")

if __name__ == "__main__":
    main()