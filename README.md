# 🧾 ncm-auto-updater

Ferramenta em **Python** para validar e atualizar automaticamente os códigos **NCM** de produtos do **ERP Retaguarda**, comparando com a tabela oficial da **Receita Federal**.  
Gera planilhas corrigidas e padronizadas, garantindo conformidade fiscal e evitando erros em cadastros de produtos.

---

## ⚙️ Funcionalidades
- 🔍 Identifica produtos com NCM incorreto
- 🧠 Corrige automaticamente com base na tabela da Receita Federal
- 🗂️ Gera planilha `.xlsx` pronta para reimportar no ERP
- 🧾 Mantém o formato e estrutura original da planilha do sistema
- 🛡️ Evita erros fiscais e inconsistências no cadastro

---

## 🧰 Tecnologias utilizadas
- Python 3.13  
- Pandas  
- OpenPyXL  
- FuzzyWuzzy  
- Python-Levenshtein  

---

## 🚀 Como usar

1. Exporte a planilha de produtos do ERP Retaguarda (`planilha_erp.xlsx`);
2. Coloque o arquivo na pasta `/data` do projeto;
3. Execute o script:

   ```bash
   python src/ncm_atualizador.py
📦 Instalação
Clone o repositório e instale as dependências:

bash
Copiar código
git clone https://github.com/seuusuario/ncm-auto-updater.git
cd ncm-auto-updater
pip install -r requirements.txt
📄 Estrutura do projeto
cpp
Copiar código
ncm-auto-updater/
│
├── src/
│   └── ncm_atualizador.py
│
├── data/
│   ├── planilha_erp.xlsx
│   ├── tabela_corrigida.xlsx
│
├── requirements.txt
├── README.md
└── .gitignore
🧑‍💻 Autor
Arthur Pinheiro Alves
📚 Estudante de Sistemas de Informação – Universidade Anhembi Morumbi
💡 Foco em automação, desenvolvimento de software e integração com inteligência artificial.

🛠️ Licença
Este projeto é de código aberto sob a licença MIT – sinta-se à vontade para usar, modificar e contribuir.
