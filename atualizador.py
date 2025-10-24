import pandas as pd

def atualizar_ncm(planilha_certa, planilha_original, coluna_chave='Produto', coluna_ncm='NCM'):
    """
    Função para atualizar os NCM da planilha original com base na planilha certa.
    
    Parâmetros:
    - planilha_certa: Caminho para a planilha Excel com os NCM corretos (deve ter colunas: coluna_chave e coluna_ncm).
    - planilha_original: Caminho para a planilha Excel a ser modificada (deve ter colunas: coluna_chave e coluna_ncm).
    - coluna_chave: Nome da coluna comum (ex: 'Produto') para fazer o mapeamento.
    - coluna_ncm: Nome da coluna do NCM (ex: 'NCM').
    
    Retorna:
    - DataFrame da planilha original modificada.
    """
    # Carregar as planilhas
    df_certa = pd.read_excel(planilha_certa)
    df_original = pd.read_excel(planilha_original)
    
    # Criar um dicionário de mapeamento: chave -> NCM correto
    mapeamento = dict(zip(df_certa[coluna_chave], df_certa[coluna_ncm]))
    
    # Atualizar o NCM na planilha original se a chave existir no mapeamento
    df_original[coluna_ncm] = df_original[coluna_chave].map(mapeamento).fillna(df_original[coluna_ncm])
    
    # Retornar o DataFrame modificado
    return df_original

# Exemplo de uso com os nomes fornecidos (assumindo extensão .xlsx; ajuste se necessário)
planilha_certa = 'importado.xlsx'  # Planilha com NCM corretos
planilha_original = 'Produtos_ARTHUR_PRESENTES_LTDA_TabPreco-1_20251024120119.xlsx'  # Planilha a ser modificada

df_modificada = atualizar_ncm(planilha_certa, planilha_original)

# Salvar a planilha modificada em um novo arquivo
df_modificada.to_excel('Produtos_ARTHUR_PRESENTES_LTDA_TabPreco-1_20251024120119_modificado.xlsx', index=False)

print("Planilha original modificada salva como 'Produtos_ARTHUR_PRESENTES_LTDA_TabPreco-1_20251024120119_modificado.xlsx'")
