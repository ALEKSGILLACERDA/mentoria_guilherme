# 📊 Extração de Vagas da Gupy via API

Este projeto tem como objetivo coletar automaticamente dados de vagas da plataforma Gupy, utilizando Python para realizar requisições em lote (paginadas) na API, e salvar os resultados em arquivos `.json` para posterior análise.

---

## 🔧 Tecnologias utilizadas

- **Python 3.10+**
- **Requests** (requisições HTTP)
- **JSON** (armazenamento estruturado dos dados)
- **OS / pathlib** (manipulação de diretórios e arquivos)
- **Git e GitHub** (versionamento)

---

## 🧱 Estrutura do projeto
├── main.py # Ponto de entrada do projeto
├── config.py # Configurações como headers e parâmetros da API
├── extracao/
│ └── gupy_api.py # Funções para coletar os dados da API
├── dados/
│ └── vagas_gupy.json # Arquivos gerados com as vagas coletadas
└── README.md

 Funcionalidades
Coleta de todas as vagas ativas de uma ou mais empresas na Gupy.

Armazenamento em arquivos .json com estrutura limpa e organizada.

Modularização que permite reuso e fácil manutenção do código.



📬 Contato
Aleks Gil Lacerda de Carvalho
Estudante de Matemática Aplicada – UFRJ
