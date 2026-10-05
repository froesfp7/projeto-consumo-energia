# Projeto G2 — Consumo de Energia Elétrica no Brasil

- Aluno: Felipe Fróes Lopes Antunes
- Professor: Alexandre Neves Louzada
- Disciplina: Linguagem de programação

Projeto acadêmico do **Tema 14**, desenvolvido para analisar padrões de consumo de energia elétrica no Brasil.

## Objetivo

Investigar evolução temporal, diferenças regionais e setoriais, sazonalidade, demanda de pico, temperatura, eficiência energética e emissões de CO₂.

## Base utilizada

- Arquivo: `dados/simulacao_consumo_energia_brasil.csv`
- Registros: **4.440**
- Variáveis: **14**
- Período: **2015 a 2024**
- Valores ausentes: **nenhum**

## Tecnologias

Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly, Streamlit, SQLite, SQLAlchemy e GitHub.

## Estrutura

```text
projeto-consumo-energia/
├── app.py
├── requirements.txt
├── README.md
├── index.html
├── .gitignore
├── dados/
├── database/
├── notebooks/
└── imagens/
```

## Executar localmente

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute:

```bash
streamlit run app.py
```


