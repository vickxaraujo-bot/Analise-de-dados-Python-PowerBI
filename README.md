
📊 Análise de Dados com Python, Excel e Power BI
ETL completo: extração, limpeza, padronização e organização dos dados
##
Este projeto demonstra um fluxo profissional de preparação de dados, utilizando Python (pandas) para tratar tabelas Excel de um cenário fictício de vendas e devoluções.
O resultado é um conjunto de dados padronizado, limpo e organizado, pronto para análises em qualquer ferramenta — como Power BI, Tableau ou Excel.
##

🧭 Visão Geral

Este projeto implementa um pipeline ETL completo, com foco em:

✔️ Padronização
✔️ Limpeza
✔️ Validação cruzada entre tabelas
✔️ Exportação final para análise em Power BI

O objetivo é transformar múltiplas fontes de dados brutos em um conjunto tratado, confiável e pronto para análise de indicadores de negócios.
##
🏗️ Arquitetura do Projeto

                +---------------------------+
                |        Camada RAW         |
                |    dados_originais/       |
                +-------------+-------------+
                              |
                              v
                +---------------------------+
                |     Camada de Processamento|
                |       script_p/            |
                |  - ETL                     |
                |  - Padronização            |
                |  - Validação               |
                |  - Conversão de Datas      |
                +-------------+-------------+
                              |
                              v
                +---------------------------+
                |     Camada Curated        |
                |      dados_tratados/      |
                |  Dados limpos e prontos   |
                +-------------+-------------+
                              |
                              v
                +---------------------------+
                |  Camada de Visualização   |
                |        dashboards/        |
                |      (Power BI)           |
                +---------------------------+


##
🧼 O que o script faz?

Limpa textos e padroniza nomes

Ajusta e valida documentos

Corrige formatos de data

Remove duplicatas

Corrige valores inválidos

Valida relações entre tabelas (cliente, loja, produto, vendas, devoluções)

Exporta arquivos tratados automaticamente

##
     🔧 Tecnologias Utilizadas
| Tecnologia          | Uso                                |
| ------------------- | ---------------------------------- |
| **Python (pandas)** | Limpeza, padronização e tratamento |
| **Excel**           | Origem das bases                   |
| **Power BI**        | Visualização e análises futuras    |
| **Git + GitHub**    | Versionamento e documentação       |

##
🗂️ Bases Tratadas

As tabelas finais, já limpas e prontas para o Power BI, estão em:

/dados_tratados/


Incluem:

vendas_tratado.xlsx

devolucoes_tratado.xlsx

cadastro_produtos_tratado.xlsx

cadastro_clientes_tratado.xlsx

cadastro_lojas_tratado.xlsx
##
📊 Dashboard

O dashboard do Power BI será adicionado posteriormente neste repositório em uma pasta dedicada.
##
👤 Responsável pelo Projeto

Victória Araújo

Tratamento, documentação e organização do fluxo analítico.
