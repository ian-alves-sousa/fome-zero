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
    page_title='Cuisines', page_icon='🍽️', layout='wide')

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

def max_rating_cuisines(df1,tipo):
    re1 = df1.loc[(df1['cuisines'] == tipo),['restaurant_name','restaurant_id','aggregate_rating']].groupby(['restaurant_name','restaurant_id']).mean().sort_values(by='aggregate_rating',ascending=False).reset_index()
    re1 = re1.loc[re1['aggregate_rating'] == re1['aggregate_rating'].max(),['restaurant_name','restaurant_id']].groupby('restaurant_name').min().sort_values(by='restaurant_id',ascending=True).reset_index()

    re1 = df1.loc[df1['restaurant_id'] == re1.iloc[0,1],['restaurant_name','country_code','city','average_cost_for_two','currency','cuisines','aggregate_rating']]
    
    label = f'{re1.iloc[0,5]}: {re1.iloc[0,0]}'
    value = f'{re1.iloc[0,6]}/5.0'
    ajuda = f'''País: {re1.iloc[0,1]}
        
Cidade: {re1.iloc[0,2]}
        
Média Prato para dois: {re1.iloc[0,3]} {re1.iloc[0,4]}'''
    
    return label,value,ajuda



def bar_1(df1,data_slider):
    graf1 = round(df3.loc[:,['cuisines','aggregate_rating']].groupby(['cuisines']).mean().sort_values(by='aggregate_rating',ascending=False).reset_index(),2)
    graf1 = px.bar(graf1.head(data_slider), x='cuisines',y='aggregate_rating',text_auto=True,labels={'cuisines':'Tipo de Culinária','aggregate_rating':'Média da Avaliação Média'},title=f'Top {data_slider} Melhores Tipos de Culiárias')
    return graf1
        
        
def bar_2(df1,data_slider):
    graf1 = round(df3.loc[:,['cuisines','aggregate_rating']].groupby(['cuisines']).mean().sort_values(by='aggregate_rating',ascending=True).reset_index(),2)
    graf1 = px.bar(graf1.head(data_slider), x='cuisines',y='aggregate_rating',text_auto=True,labels={'cuisines':'Tipo de Culinária','aggregate_rating':'Média da Avaliação Média'},title=f'Top {data_slider} Piores Tipos de Culiárias')
    return graf1
        


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
df3 = df1.copy()



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



data_slider = st.sidebar.slider('Selecione a quantidade de Restaurantes que deseja visualizar',
                 value=10,
                 min_value=1,
                 max_value=20)



cuisines_list = ['Italian', 'European', 'Filipino', 'American', 'Korean', 'Pizza',
       'Taiwanese', 'Japanese', 'Coffee', 'Chinese', 'Seafood',
       'Singaporean', 'Vietnamese', 'Latin American', 'Healthy Food',
       'Cafe', 'Fast Food', 'Brazilian', 'Argentine', 'Arabian', 'Bakery',
       'Tex-Mex', 'Bar Food', 'International', 'French', 'Steak',
       'German', 'Sushi', 'Grill', 'Peruvian', 'North Eastern',
       'Ice Cream', 'Burger', 'Mexican', 'Vegetarian', 'Contemporary',
       'Desserts', 'Juices', 'Beverages', 'Spanish', 'Thai', 'Indian',
       'BBQ', 'Mongolian', 'Portuguese', 'Greek', 'Asian', 'Author',
       'Gourmet Fast Food', 'Lebanese', 'Modern Australian', 'African',
       'Coffee and Tea', 'Australian', 'Middle Eastern', 'Malaysian',
       'Tapas', 'New American', 'Pub Food', 'Southern', 'Diner', 'Donuts',
       'Southwestern', 'Sandwich', 'Irish', 'Mediterranean', 'Cafe Food',
       'Korean BBQ', 'Fusion', 'Canadian', 'Breakfast', 'Cajun',
       'New Mexican', 'Belgian', 'Cuban', 'Taco', 'Caribbean', 'Polish',
       'Deli', 'British', 'California', 'Others', 'Eastern European',
       'Creole', 'Ramen', 'Ukrainian', 'Hawaiian', 'Patisserie',
       'Yum Cha', 'Pacific Northwest', 'Tea', 'Moroccan', 'Burmese',
       'Dim Sum', 'Crepes', 'Fish and Chips', 'Russian', 'Continental',
       'South Indian', 'North Indian', 'Salad', 'Finger Food', 'Mandi',
       'Turkish', 'Kerala', 'Pakistani', 'Biryani', 'Street Food',
       'Nepalese', 'Goan', 'Iranian', 'Mughlai', 'Rajasthani', 'Mithai',
       'Maharashtrian', 'Gujarati', 'Rolls', 'Momos', 'Parsi',
       'Modern Indian', 'Andhra', 'Tibetan', 'Kebab', 'Chettinad',
       'Bengali', 'Assamese', 'Naga', 'Hyderabadi', 'Awadhi', 'Afghan',
       'Lucknowi', 'Charcoal Chicken', 'Mangalorean', 'Egyptian',
       'Malwani', 'Armenian', 'Roast Chicken', 'Indonesian', 'Western',
       'Dimsum', 'Sunda', 'Kiwi', 'Asian Fusion', 'Pan Asian', 'Balti',
       'Scottish', 'Cantonese', 'Sri Lankan', 'Khaleeji', 'South African',
       'Durban', 'World Cuisine', 'Izgara', 'Home-made', 'Giblets',
       'Fresh Fish', 'Restaurant Cafe', 'Kumpir', 'Döner',
       'Turkish Pizza', 'Ottoman', 'Old Turkish Bars', 'Kokoreç']
cuisines_op = st.sidebar.multiselect('Escolha os Tipos de Culinária',
                      cuisines_list,
                      default=['Home-made','BBQ','Japanese', 'Brazilian','Arabian','American','Italian'])





#Filtro de cidades
df1 = df1.loc[df1['country_code'].isin(country_op),:]
df3 = df3.loc[df3['country_code'].isin(country_op),:]

#Filtro das colunárias
df1 = df1.loc[df1['cuisines'].isin(cuisines_op),:]




# ===========================================================================
#Layout no Streamlit
#==========================================================================
st.markdown('# 🍽️ Visão Tipos de Cusinhas')
st.markdown('## Melhores Restaurantes dos Principais tipos Culinários')

#Primeiro container dividio em 5 colunas
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        label, value, ajuda = max_rating_cuisines(df2,'Italian')
        col1.metric(label,value,help=ajuda)
        
        
    with col2:
        label, value, ajuda = max_rating_cuisines(df2,'American')
        col2.metric(label,value,help=ajuda)
        
    with col3:
        label, value, ajuda = max_rating_cuisines(df2,'Arabian')
        col3.metric(label,value,help=ajuda)
        
    with col4:       
        label, value, ajuda = max_rating_cuisines(df2,'Japanese')
        col4.metric(label,value,help=ajuda)
        
    with col5:
        label, value, ajuda = max_rating_cuisines(df2,'Brazilian')
        col5.metric(label,value,help=ajuda)
    
    
#Segundo container com o DataFrame
with st.container():
    st.markdown(f'## Top {data_slider} Restaurantes')
    dataframe = df1.loc[df1['aggregate_rating'] == df1['aggregate_rating'].max(),['restaurant_id', 'restaurant_name', 'country_code', 'city','cuisines','average_cost_for_two','aggregate_rating','votes']].sort_values(by='restaurant_id',ascending=True)
    dataframe.columns = ['ID Restaurante', 'Nome do Restaurante', 'País', 'Cisade','Culinária','Média do preço de um prato para dois','Avaliação média','Qtde de votos']
    st.dataframe(dataframe.head(data_slider))
    
    

#Terceiro container com duas colunas, cada qual com um gráfico
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        graf1 = bar_1(df1,data_slider)
        st.plotly_chart(graf1,use_container_width=True,theme=None)
        
    with col2:
        graf1 = bar_2(df1,data_slider)
        st.plotly_chart(graf1,use_container_width=True,theme=None)