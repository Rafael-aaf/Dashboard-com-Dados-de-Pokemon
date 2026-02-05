import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Pokemon!",
    page_icon="⚡",
    layout="wide",
)

df = pd.read_csv("pokemon_data_clean.csv")

st.sidebar.header("Filtros")

# Filtro de tipos
tipos_disponiveis = df['type_1'].unique()
tipos_selecionados = st.sidebar.multiselect("Tipos", tipos_disponiveis, default=tipos_disponiveis)

# Filtro de Habilidades
habilidades_disponiveis = df['ability_1'].unique()
habilidades_selecionadas = st.sidebar.multiselect("Habilidades", habilidades_disponiveis, default=habilidades_disponiveis)

# Filtragem do DataFrame
df_filtrado = df[
    (df['type_1'].isin(tipos_selecionados)) &
    (df['ability_1'].isin(habilidades_selecionadas))
]

st.title("Análise de Dados de Pokémon")

if not df_filtrado.empty:
    stats = ['hp', 'attack', 'defense', 'specialattack', 'specialdefense', 'speed']
    quantidade_pokemon = df_filtrado.shape[0]
    bst_medio = df_filtrado[stats].sum(axis=1).mean()
    peso_medio = df_filtrado['weight_kg'].mean()
    altura_media = df_filtrado['height_m'].mean()
else:
    quantidade_pokemon, bst_medio, peso_medio, altura_media = 0, 0, 0, 0

linha1_quantidade, linha1_bst, linha1_altura, linha1_peso = st.columns(4)

linha1_quantidade.metric("Quantidade de Pokémon", f"{quantidade_pokemon}")
linha1_bst.metric("BST Médio", f"{bst_medio:.2f}")
linha1_altura.metric("Peso Médio", f"{peso_medio:.2f}")
linha1_peso.metric("Altura Média", f"{altura_media:.2f}")

st.subheader("Gráficos")

col1, col2 = st.columns(2)

with col1:
    stats = ['hp', 'attack', 'defense', 'specialattack', 'specialdefense', 'speed']
    df_tipos_bst = pd.DataFrame()
    df_tipos_bst['type_1'] = df_filtrado['type_1']
    df_tipos_bst['bst'] = df_filtrado.loc[:, stats].sum(axis=1)
    bst_media_tipo = df_tipos_bst.groupby('type_1')['bst'].mean().sort_values(ascending=False).reset_index()

    fig = px.bar(bst_media_tipo,
        x='type_1',
        y='bst',
        title='Status base total por tipo',
        labels={'type_1': 'Tipos', 'bst': 'BST'})

    st.plotly_chart(fig, use_container_width=True)

with col2:
    df_tipos_peso = (
        df_filtrado
        .groupby('type_1')['weight_kg']
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )
    
    fig = px.bar(df_tipos_peso,
                 x='type_1',
                 y='weight_kg',
                 title='Peso por tipo',
                 labels={'type_1':'Tipos', 'weight_kg':'Peso'})
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Dados Detalhados")
st.dataframe(df_filtrado)