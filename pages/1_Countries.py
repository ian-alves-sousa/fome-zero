#Bibiliotecas
from haversine import haversine
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st
from PIL import Image
from streamlit_folium import folium_static
import folium
import inflection

st.set_page_config(
    page_title='Countries', page_icon='🌎', layout='wide')

# ===========================================================================
#Funções
#==========================================================================
COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}

def country_name(country_id):
    return COUNTRIES[country_id]


def create_price_tye(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"



COLORS = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}

def color_name(color_code):
    return COLORS[color_code]



def rename_columns(dataframe):
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df

def apply_func(df1):
    df1['Country Code'] = df1.loc[:, 'Country Code'].apply(lambda x: country_name(x))
    df1['Price range'] = df1.loc[:, 'Price range'].apply(lambda x: create_price_tye(x))
    df1['Expressed color'] = df1.loc[:, 'Rating color'].apply(lambda x: color_name(x))
    df1 = rename_columns(df1)
    df1['cuisines'] = df1['cuisines'].astype(str)
    df1["cuisines"] = df1.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])
    return df1


def clean_code(df1):
    df1 = df1.drop(labels=['switch_to_order_menu'], axis='columns')
    df1 = df1.loc[(df1['cuisines'] != 'nan'),:].copy()
    df1 = df1.loc[(df1['cuisines'] != 'Drinks Only'),:].copy()
    df1 = df1.loc[(df1['cuisines'] != 'Mineira'),:].copy()
    df1 = df1.drop_duplicates().reset_index(drop=True)
    return df1



def bar_1(df1):
    re2 = df1.loc[:,['restaurant_id','country_code']].groupby(['country_code']).count().sort_values(by='restaurant_id',ascending=False).reset_index()
    fig = px.bar(re2, x='country_code',y='restaurant_id',text_auto=True,labels={'country_code':'Países','restaurant_id':'Quantidade de Restaurantes'},title='Quantidade de Restaurantes Registrados por País')
    return fig


def bar_2(df1):
    re1 = df1.loc[:,['country_code','city','restaurant_id']].groupby(['country_code','city']).count().sort_values(by='country_code',ascending=False).reset_index()
    re1 = re1.loc[:,['country_code','city']].groupby(['country_code']).count().sort_values(by='city',ascending=False).reset_index()
    fig = px.bar(re1, x='country_code',y='city',text_auto=True,labels={'country_code':'Países','city':'Quantidade de Cidades'},title='Quantidade de Cidades Registradas por País')
    return fig


def bar_3(df1):
    re8 = round(df1.loc[:,['votes','country_code']].groupby(['country_code']).mean().sort_values(by='votes',ascending=False).reset_index(),2)
    fig = px.bar(re8, x='country_code',y='votes',text_auto=True,labels={'country_code':'Países','votes':'Quantidade de Avaliações'},title='Média de Avaliações feitas por País')
    return fig


def bar_4(df1):
    re11 = round(df1.loc[:,['average_cost_for_two','country_code']].groupby(['country_code']).mean().sort_values(by='average_cost_for_two',ascending=False).reset_index(),2)
    fig = px.bar(re11, x='country_code',y='average_cost_for_two',text_auto=True,labels={'country_code':'Países','average_cost_for_two':'Preço de prato para duas Pessoas'},title='Média do Preço de um prato para duas pessoas por País')
    return fig

# --------------------- Início da Estrutura Lógica do Código ---------------

# ===========================================================================
#Importar os dados
#==========================================================================
df = pd.read_csv('dataset/zomato.csv')
df1 = df.copy()

# ===========================================================================
#Limpando os dados
#==========================================================================
df1 = apply_func(df1)
df1 = clean_code(df1)



# ===========================================================================
#Barra lateral
#==========================================================================
st.sidebar.markdown('## Filtros')


country = ['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey']
country_op = st.sidebar.multiselect('Escolha os Países que Deseja visualizar as informações',
                      country,
                      default=['Brazil','England','Qatar', 'South Africa','Canada','Australia'])

#Filtro de cidades
df1 = df1.loc[df1['country_code'].isin(country_op),:]




# ===========================================================================
#Layout no Streamlit
#==========================================================================
st.markdown('# 🌎 Visão Países')

#Primeiro container com um gráfico
with st.container():
    fig = bar_1(df1)
    st.plotly_chart(fig,use_container_width=True,theme=None)
    
    
#Segundo container com um gráfico
with st.container():
    fig = bar_2(df1)
    st.plotly_chart(fig,use_container_width=True,theme=None)
    

#Terceiro container com duas colunas, cada qual com um gráfico
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        fig = bar_3(df1)
        st.plotly_chart(fig,use_container_width=True,theme=None)
        
        
    with col2:
        fig = bar_4(df1)
        st.plotly_chart(fig,use_container_width=True,theme=None)