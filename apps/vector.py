import streamlit as st
import leafmap.foliumap as leafmap

def app():

    st.title("Vector data")

    m = leafmap.Map(center=[0, 0], zoom=2)
    m.add_basemap("HYBRID")
    m.add_basemap("Esri.NatGeoWorldMap")
    m.whiteboxgui(tree=True)
    
    in_bounds = 'https://raw.githubusercontent.com/darfo5gis/streamlit-demo/master/data/vector/r5_camsur_municities.geojson'
    m.add_geojson(in_bounds, layer_name='Camarines Sur Municities')
    in_geojson = 'https://raw.githubusercontent.com/darfo5gis/streamlit-demo/master/data/vector/ai.geojson'
    m.add_geojson(in_geojson, layer_name="AI")

    m.to_streamlit(height=700)