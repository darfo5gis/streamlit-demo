import streamlit as st
import leafmap.foliumap as leafmap

def app():

    st.title("Vector data")

    m = leafmap.Map(center=[0, 0], zoom=2)
    m.add_basemap("HYBRID")
    
    in_bounds = 'https://raw.githubusercontent.com/faeldon/philippines-json-maps/master/geojson/provinces/medres/provinces-region-ph050000000.0.01.json'
    m.add_geojson(in_bounds, layer_name='Camarines Sur Municities')
    

    m.to_streamlit(height=700)