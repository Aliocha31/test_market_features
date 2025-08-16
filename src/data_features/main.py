from downlaod import download_data
import streamlit as st 

tesla = download_data(index_name="TSLA")
mc =  download_data(index_name="MC.PA")
open = download_data(index_name="OPEN")
nvdia = download_data(index_name="NVDA")

print(tesla)