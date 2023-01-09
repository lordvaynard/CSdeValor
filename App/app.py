import streamlit as st
import pandas as pd
import numpy as np
import base64
import datetime
from datetime import date

def filedownloadcsv(df, season, league):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="Base_de_Dados - '+season+' - '+league+'.csv">Download CSV File</a>'
    return href

st.title("Web App Football Data")

st.sidebar.header("Ligas")
selected_league = st.sidebar.selectbox('League',['Inglaterra','Alemanha','Itália','Espanha','França'])

st.sidebar.header("Temporadas")
selected_season = st.sidebar.selectbox('Season', ['2022/2023','2021/2022','2020/2021','2019/2020'])

# WebScraping Football Data
def load_data(league, season):
  
  if selected_league == 'Inglaterra':
    league = 'E0'
  if selected_league == 'Alemanha':
    league = 'D1'
  if selected_league == 'Itália':
    league = 'I1'
  if selected_league == 'Espanha':
    league = 'SP1'
  if selected_league == 'França':
    league = 'F1'
   
  if selected_season == '2022/2023':
    season = '2223'  
  if selected_season == '2021/2022':
    season = '2122'
  if selected_season == '2020/2021':
    season = '2021'
  if selected_season == '2019/2020':
    season = '1920'
    
  url = "https://www.football-data.co.uk/mmz4281/"+season+"/"+league+".csv"
  data = pd.read_csv(url)
  return data

df = load_data(selected_league, selected_season)

st.subheader("Dataframe: "+selected_league)
st.dataframe(df)

st.markdown(filedownloadcsv(df, selected_season, selected_league), unsafe_allow_html=True)



st.title("Jogos do Dia")

dia = st.date_input(
    "Data de Análise",
    date.today())

def load_data_jogos():
    data_jogos = pd.read_csv("https://github.com/futpythontrader/YouTube/blob/main/Jogos_do_Dia_FlashScore/"+str(dia)+"_Jogos_do_Dia_FlashScore.csv?raw=true")
    
    return data_jogos

df_jogos = load_data_jogos()

st.dataframe(df_jogos)

def filedownload(df, dia):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="Jogos_do_dia-'+str(dia)+'.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_jogos, dia), unsafe_allow_html=True)
