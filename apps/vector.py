import streamlit as st
import leafmap.foliumap as leafmap

def app():

    st.title("Vector data")

    m = leafmap.Map(center=[0, 0], zoom=2)

    in_geojson = 'https://'
    m.add_geojson(in_geojson, layer_name="")

    m.to_streamlit(height=700)