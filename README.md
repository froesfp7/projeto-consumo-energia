# ⚡ Projeto G2 — Consumo de Energia Elétrica no Brasil

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

## Publicar no GitHub

Crie um repositório chamado `projeto-consumo-energia` e, dentro desta pasta, execute:

```bash
git init
git add .
git commit -m "Projeto G2 - Consumo de Energia"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/projeto-consumo-energia.git
git push -u origin main
```

Substitua `SEU-USUARIO` pelo seu usuário do GitHub.

## GitHub Pages

No GitHub:

1. Abra o repositório.
2. Acesse **Settings → Pages**.
3. Em **Build and deployment**, selecione **Deploy from a branch**.
4. Selecione `main` e a pasta `/root`.
5. Salve.

O GitHub Pages publicará o `index.html`.

## Streamlit Community Cloud

1. Acesse o Streamlit Community Cloud.
2. Entre com sua conta GitHub.
3. Selecione o repositório `projeto-consumo-energia`.
4. Escolha a branch `main`.
5. Defina `app.py` como arquivo principal.
6. Publique o aplicativo.

## Links para preencher após a publicação

- GitHub: `https://github.com/SEU-USUARIO/projeto-consumo-energia`
- GitHub Pages: `https://SEU-USUARIO.github.io/projeto-consumo-energia/`
- Streamlit: `https://SEU-APP.streamlit.app/`

## Observação

Os links acima são modelos. Depois da publicação, substitua `SEU-USUARIO` e `SEU-APP` pelos endereços reais.
