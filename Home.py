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
    page_title='Main Page',page_icon='📊', layout='wide')

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


def ajuste_votes(df1):
    re1 = df2['votes'].sum()
    re1 = f'{re1:,.0f}'
    re1 = re1.replace(',','.')
    return re1


def restaurantes_map(df1):
    re6 = df1.loc[:,['restaurant_name','average_cost_for_two','currency','aggregate_rating','country_code','city','cuisines','latitude','longitude']]
    map = folium.Map(location=[0, 0],zoom_start=2)
    marker_cluster = folium.plugins.MarkerCluster().add_to(map)
    for index,location in re6.iterrows():
        folium.Marker([location['latitude'],location['longitude']],
                    popup=folium.Popup(f'''<h6><b>{location['restaurant_name']}</b></h6>
                    <h6>Preço: {location['average_cost_for_two']} ({location['currency']}) para dois <br>
                    Culinária: {location['cuisines']} <br>
                    Avaliação: {location['aggregate_rating']}/5.0</h6>''',
                    max_width=300,min_width=150),
                    tooltip=location["restaurant_name"],
                    icon=folium.Icon(color='green', icon='home', prefix='fa')).add_to(marker_cluster)

    folium_static(map,width=1024,height=600)
    ### Lembrar de definir os agrupamentos dos países



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
df2 = df1.copy()




# ===========================================================================
#Barra lateral
#==========================================================================
path = 'logo.jpg'
image = Image.open(path)
st.sidebar.image(image,width=250)

st.sidebar.markdown('# Fome Zero')
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


### Falta colocar os dados paea download



# ===========================================================================
#Layout no Streamlit
#==========================================================================
st.markdown('# Fome Zero!')
st.markdown('## O Melhor lugar para encontrar seu mais novo restaurante favorito!')

#Primeiro container dividio em 5 colunas
with st.container():
    st.markdown('### Temos as seguintes marcas dentro da nossa plataforma:')
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        re1 = len(df2['restaurant_id'].unique())
        col1.metric('Restaurantes Cadastrados',re1)
        
    with col2:
        re1 = len(df2['country_code'].unique())
        col2.metric('Países Cadastrados',re1)
        
    with col3:
        re1 = len(df2['city'].unique())
        col3.metric('Cidades Cadastrados',re1)
        
    with col4:       
        re1 = ajuste_votes(df1)
        col4.metric('Avaliações Feitas na Plataforma',re1)
        
    with col5:
        re1 = len(df2['cuisines'].unique())
        col5.metric('Tipos de Culinárias Oferecidas',re1)
    
    
#Segundo container com o mapa
with st.container():
    restaurantes_map(df1)
    