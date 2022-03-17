import streamlit as st
import leafmap.kepler as leafmap
import geopandas as gpd


def app():

    st.title("Vector")

    m= leafmap.Map(center=[13.5, 123.15], zoom=8)
    
    in_geojson = (
        'https://raw.githubusercontent.com/darfo5gis/streamlit-demo/master/data/vector/r5_municities_camsur.json'
    )
    gdf = gpd.read_file(in_geojson)
    m.add_gdf(gdf, random_color_column="ADM3_EN")
    
    m.to_streamlit(height=900)
