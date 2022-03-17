import streamlit as st
import leafmap.kepler as leafmap
import geopandas as gpd


def app():

    st.title("Vector")

    m= leafmap.Map(center=[13.5, 123.15], zoom=8, config=config)
    
    municities = (
        'https://raw.githubusercontent.com/darfo5gis/streamlit-demo/master/data/vector/r5_municities_camsur.json'
    )

    gdf = gpd.read_file(municities)
    m.add_gdf(gdf, layer_name='Municities')
    
    m.to_streamlit(height=900)
