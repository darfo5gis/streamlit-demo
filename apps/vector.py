import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Vector")

    m= leafmap.Map(center=[13.5, 123.15], zoom=8)
    
    in_geojson = 'https://raw.githubusercontent.com/darfo5gis/streamlit-demo/master/data/vector/r5_municities_camsur.json'
    m.add_geojson(in_geojson, layer_name="Camarines Sur Municities Boundaries", random_color_column="ADM3_EN")
    
    m.to_streamlit(height=900)
