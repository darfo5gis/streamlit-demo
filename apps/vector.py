import streamlit as st
import leafmap.kepler as leafmap
import geopandas as gpd



def app():

    st.title("Vector")

    m= leafmap.Map(center=[13.5, 123.15], zoom=8)
    
    municities = (
        'https://raw.githubusercontent.com/darfo5gis/streamlit-demo/master/data/vector/r5_municities_camsur.json'
    )
    m_config = 'https://raw.githubusercontent.com/darfo5gis/streamlit-demo/master/config/vector/m.config'
    gdf = gpd.read_file(municities)
    m.add_gdf(gdf, layer_name='Municities')
    #m.save_config(m_config.json)
    
    m.to_streamlit(height=900)
