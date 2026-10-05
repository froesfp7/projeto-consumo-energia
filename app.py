import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="Consumo de Energia Elétrica no Brasil", layout="wide")

DATA=Path(__file__).parent/'dados'/'simulacao_consumo_energia_brasil.csv'

@st.cache_data
def carregar_dados():
    df=pd.read_csv(DATA)
    df['data']=pd.to_datetime(df['data'])
    df['ano']=df['data'].dt.year
    df['mes']=df['data'].dt.month
    nomes={1:'Janeiro',2:'Fevereiro',3:'Março',4:'Abril',5:'Maio',6:'Junho',7:'Julho',8:'Agosto',9:'Setembro',10:'Outubro',11:'Novembro',12:'Dezembro'}
    df['mes_nome']=df['mes'].map(nomes)
    df['consumo_per_capita']=df['consumo_mwh']/df['populacao']
    df['intensidade_co2']=df['emissao_co2']/df['consumo_mwh']
    return df

df=carregar_dados()

st.title("Consumo de Energia Elétrica no Brasil")
st.markdown("### Dashboard analítico — Tema 14")
st.write("Este dashboard investiga a evolução do consumo de energia elétrica no Brasil, comparando regiões, estados e setores e explorando demanda, temperatura, eficiência e emissões de CO₂.")

with st.sidebar:
    st.header("Filtros")
    anos=st.multiselect("Ano",sorted(df.ano.unique()),default=sorted(df.ano.unique()))
    meses=st.multiselect("Mês",sorted(df.mes.unique()),default=sorted(df.mes.unique()))
    regioes=st.multiselect("Região",sorted(df.regiao.unique()),default=sorted(df.regiao.unique()))
    ufs=st.multiselect("Estado (UF)",sorted(df.uf.unique()),default=sorted(df.uf.unique()))
    setores=st.multiselect("Setor de consumo",sorted(df.setor_consumo.unique()),default=sorted(df.setor_consumo.unique()))
    niveis=st.multiselect("Nível de demanda",sorted(df.nivel_demanda.unique()),default=sorted(df.nivel_demanda.unique()))

f=df[df.ano.isin(anos)&df.mes.isin(meses)&df.regiao.isin(regioes)&df.uf.isin(ufs)&df.setor_consumo.isin(setores)&df.nivel_demanda.isin(niveis)].copy()
if f.empty:
    st.warning("Nenhum registro encontrado para os filtros selecionados."); st.stop()

# KPIs
cons=f.consumo_mwh.sum(); estado=f.groupby('uf').consumo_mwh.sum().idxmax(); setor=f.groupby('setor_consumo').consumo_mwh.sum().idxmax(); demanda=f.demanda_pico.mean(); tarifa=f.tarifa_media.mean(); co2=f.emissao_co2.sum(); eficiencia=f.eficiencia_energetica.mean()
c1,c2,c3,c4=st.columns(4)
c1.metric("Consumo total",f"{cons:,.0f} MWh".replace(',','.'))
c2.metric("UF líder",estado)
c3.metric("Setor líder",setor)
c4.metric("Demanda média",f"{demanda:,.0f}".replace(',','.'))
c5,c6,c7,c8=st.columns(4)
c5.metric("Tarifa média",f"R$ {tarifa:.2f}")
c6.metric("Emissões de CO₂",f"{co2:,.0f}".replace(',','.'))
c7.metric("Eficiência média",f"{eficiencia:.2f}")
c8.metric("Registros",f"{len(f):,}".replace(',','.'))

st.divider()

st.subheader("Evolução temporal")
t=f.groupby('data',as_index=False).agg(consumo_mwh=('consumo_mwh','sum'),demanda_pico=('demanda_pico','mean'))
fig=px.line(t,x='data',y='consumo_mwh',markers=True,labels={'data':'Data','consumo_mwh':'Consumo (MWh)'})
st.plotly_chart(fig,use_container_width=True)

c1,c2=st.columns(2)
with c1:
    st.subheader("Consumo por região")
    r=f.groupby('regiao',as_index=False).consumo_mwh.sum().sort_values('consumo_mwh',ascending=False)
    st.plotly_chart(px.bar(r,x='regiao',y='consumo_mwh',text_auto='.2s',labels={'regiao':'Região','consumo_mwh':'MWh'}),use_container_width=True)
with c2:
    st.subheader("Consumo por setor")
    s=f.groupby('setor_consumo',as_index=False).consumo_mwh.sum().sort_values('consumo_mwh',ascending=False)
    st.plotly_chart(px.bar(s,x='setor_consumo',y='consumo_mwh',text_auto='.2s',labels={'setor_consumo':'Setor','consumo_mwh':'MWh'}),use_container_width=True)

c1,c2=st.columns(2)
with c1:
    st.subheader("Ranking de estados")
    rank=f.groupby('uf',as_index=False).consumo_mwh.sum().sort_values('consumo_mwh',ascending=False)
    st.plotly_chart(px.bar(rank.head(15),x='consumo_mwh',y='uf',orientation='h',text_auto='.2s',labels={'uf':'UF','consumo_mwh':'MWh'}),use_container_width=True)
with c2:
    st.subheader("Temperatura × consumo")
    samp=f.sample(min(len(f),1500),random_state=42)
    st.plotly_chart(px.scatter(samp,x='temperatura_media',y='consumo_mwh',color='setor_consumo',trendline='ols',labels={'temperatura_media':'Temperatura média (°C)','consumo_mwh':'Consumo (MWh)'}),use_container_width=True)

st.subheader("Sazonalidade — heatmap")
h=f.pivot_table(index='ano',columns='mes',values='consumo_mwh',aggfunc='sum').fillna(0)
fig=px.imshow(h,text_auto='.0f',aspect='auto',labels=dict(x='Mês',y='Ano',color='MWh'))
st.plotly_chart(fig,use_container_width=True)

st.subheader("Demanda, eficiência e emissões")
c1,c2=st.columns(2)
with c1:
    d=f.groupby('data',as_index=False).demanda_pico.mean()
    st.plotly_chart(px.line(d,x='data',y='demanda_pico',labels={'data':'Data','demanda_pico':'Demanda média'}),use_container_width=True)
with c2:
    e=f.groupby('data',as_index=False).eficiencia_energetica.mean()
    st.plotly_chart(px.line(e,x='data',y='eficiencia_energetica',labels={'data':'Data','eficiencia_energetica':'Eficiência média'}),use_container_width=True)

st.subheader("Correlação entre variáveis")
num=f[['consumo_mwh','demanda_pico','temperatura_media','tarifa_media','populacao','eficiencia_energetica','emissao_co2']]
corr=num.corr()
st.plotly_chart(px.imshow(corr,text_auto='.2f',aspect='auto',color_continuous_scale='RdBu_r',zmin=-1,zmax=1),use_container_width=True)

st.subheader("Interpretação automática")
year=f.groupby('ano').consumo_mwh.sum()
trend=((year.iloc[-1]/year.iloc[0])-1)*100 if len(year)>1 else 0
peak_month=f.groupby('mes').consumo_mwh.sum().idxmax()
peak_level=f.groupby('nivel_demanda').consumo_mwh.sum().idxmax()
st.info(f"No recorte selecionado, o consumo total foi de {cons:,.0f} MWh. O setor com maior participação foi **{setor}** e a UF com maior consumo foi **{estado}**. A variação do consumo entre o primeiro e o último ano disponível no filtro foi de **{trend:.1f}%**. O mês com maior consumo agregado foi **{peak_month}** e o nível de demanda com maior volume de consumo associado foi **{peak_level}**.")

st.subheader("Tabela detalhada")
cols=['data','regiao','uf','setor_consumo','consumo_mwh','demanda_pico','temperatura_media','tarifa_media','eficiencia_energetica','emissao_co2','nivel_demanda']
st.dataframe(f[cols].sort_values('data',ascending=False),use_container_width=True,hide_index=True)

st.subheader("Conclusão executiva")
st.write("A análise permite acompanhar a dinâmica do consumo de energia, identificar os maiores centros consumidores, comparar setores e regiões e observar períodos de maior demanda. Os indicadores de eficiência, tarifa e emissões complementam a leitura operacional e ambiental. Os resultados devem ser interpretados conforme os filtros aplicados, evitando conclusões fora do recorte selecionado.")
