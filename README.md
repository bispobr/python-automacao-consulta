# Automação de Consultas

Automação desenvolvida em Python para acessar um site utilizando o navegador Microsoft Edge, realizar autenticação e preencher campos de pesquisa para consultar informações específicas.

Os resultados obtidos pela automação são armazenados em uma planilha para posterior utilização.

## Funcionalidades

- Acesso automatizado ao site
- Login automatizado
- Preenchimento de campos de pesquisa
- Execução de consultas
- Coleta das informações retornadas
- Exportação dos resultados para planilha

## Tecnologias

- Python
- Selenium
- OpenPyXL
- Microsoft Edge

## Requisitos

- Python instalado
- Microsoft Edge instalado
- Acesso ao site utilizado pela automação
- Credenciais necessárias para autenticação
- Selenium
- OpenPyXL

Instale as bibliotecas necessárias com:

```bash
pip install selenium openpyxl
```

## Como utilizar

Clone o repositório:

```bash
git clone https://github.com/bispobr/python-automacao-consulta.git
cd python-automacao-consulta
```

Configure o local onde a planilha de resultados deverá ser armazenada de acordo com a implementação da aplicação.

Execute a automação:

```bash
python app.py
```

## Fluxo da automação

```text
Início
  │
  ▼
Acessar site
  │
  ▼
Realizar login
  │
  ▼
Preencher campos de busca
  │
  ▼
Executar consulta
  │
  ▼
Coletar informações
  │
  ▼
Salvar resultados na planilha
  │
  ▼
Fim
```

## Estrutura

O ponto de entrada da aplicação é o arquivo `app.py`.

Os demais arquivos e configurações devem ser consultados diretamente no projeto para identificar detalhes específicos da implementação.

## Status

Projeto de automação em Python desenvolvido para reduzir tarefas repetitivas de consulta e organização de informações em planilhas.
