#  Projeto: Limpeza e Tratamento de Dados - TechVix
# Autora: Victória Araújo
# Descrição:
#   Este script lê dados fictícios com erros, faz limpeza e tratamento,
#   e exporta novamente para uma pasta organizada sem erros.
# ===============================================================

import pandas as pd
import os

# Caminho da pasta onde estão os arquivos
base_path = r"C:\Users\Kellem Victoria\Documents\testedenovo"

def limpar_dados(nome_arquivo):
    path_entrada = os.path.join(base_path, nome_arquivo)
    path_saida = os.path.join(base_path, nome_arquivo.replace("_dirty", "_tratado_python"))

    df = pd.read_excel(path_entrada)

    # -------- LIMPEZAS GERAIS --------

    # Remover espaços em colunas de texto
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip()

    # -------- TRATAMENTO DE DATAS --------

    for col in df.columns:

        # Se for coluna de data ou nascimento
        if "data" in col.lower() or "nascimento" in col.lower():

            # 1) Tentar converter normalmente
            df[col] = pd.to_datetime(df[col], errors="coerce")

            # 2) Se não funcionar, tentar converter como número serial do Excel
            if df[col].isna().sum() > 0:
                # tentar dias desde 1899
                try:
                    df[col] = pd.to_datetime(df[col], unit="d",
                                             origin="1899-12-30", errors="ignore")
                except:
                    pass

    # -------- TRATAMENTO DE COLUNAS NUMÉRICAS --------
    for col in df.columns:
        
        if df[col].dtype == object:
            if df[col].str.replace('.', '', 1).str.replace('-', '', 1).str.isdigit().all():
                df[col] = pd.to_numeric(df[col], errors="coerce")

    # -------- TRATAMENTO DE GÊNERO --------
    if "gênero" in df.columns or "genero" in df.columns:
        col_genero = "gênero" if "gênero" in df.columns else "genero"

        df[col_genero] = df[col_genero].str.lower().str.strip()

        df[col_genero] = df[col_genero].replace({
            "m": "Masculino",
            "f": "Feminino",
            "masculino": "Masculino",
            "feminino": "Feminino"
        })

        df[col_genero] = df[col_genero].replace("nan", "Outro")
        df[col_genero] = df[col_genero].fillna("Outro")

    # Remover duplicatas
    df = df.drop_duplicates()

    # Salvar
    df.to_excel(path_saida + ".xlsx", index=False)
    print(f"Arquivo tratado salvo em: {path_saida}.xlsx")


# -------- LISTA REAL DOS ARQUIVOS --------

arquivos = [
    "REAL_dCadastroCliente_dirty.xlsx",
    "REAL_dCadastroLojas_dirty.xlsx",
    "REAL_dCadastroProdutos_dirty.xlsx",
    "REAL_fBaseVendas_dirty.xlsx"
]

for arquivo in arquivos:
    limpar_dados(arquivo)

