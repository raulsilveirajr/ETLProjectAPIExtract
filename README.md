# ETL Project - API Data Extraction

## Overview
This project implements an ETL (Extract, Transform, Load) pipeline that extracts data from various APIs, transforms it according to business rules, and loads it into a target database.

## Features
- API data extraction with error handling and retry mechanisms
- Data transformation and cleaning
- Configurable data loading to different destinations
- Logging and monitoring capabilities
- Rate limiting support for API calls

## Prerequisites
- Python 3.8+
- pip (Python package installer)
- poetry (Python package manager)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/raulsilveirajr/ETLProjectAPIExtract
cd ETLProjectAPIExtract
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Instale o Poetry (caso ainda não tenha):
```bash
curl -sSL https://install.python-poetry.org | python3 -
# No Windows, você pode usar:
# (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

4. Instale as dependências do projeto:
```bash
poetry install
```

5. Ative o ambiente virtual do Poetry:
```bash
poetry shell
```

## Exemplos
O projeto inclui exemplos de implementação na pasta `exemplos/`. Para executar cada exemplo, use os seguintes comandos:

### Exemplo 01
```bash
python3 exemplos/exemplo_01.py
```

### Exemplo 02
```bash
python3 exemplos/exemplo_02.py
```

### Exemplo 03
```bash
python3 exemplos/exemplo_03.py
```

### Exemplo 04
```bash
python3 exemplos/exemplo_04.py
```


## Dashboard Logfire
https://logfire.pydantic.dev/raulsilveirajr/etl-project-api-extract/dashboards/6cc25f8c-c7c8-4b73-989e-21d0327ef6db