import streamlit as st
import pandas as pd
import plotly.graph_objects as go

car_data = pd.read_csv('vehicles_us.csv')

hist_button = st.button('Show Histogram')

if hist_button:
    st.write('Histogram of Vehicle Prices')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'], nbinsx=20)])
    fig.update_layout(title='Distribution of Vehicle Odometer Readings',
                      xaxis_title='Odometer Reading',
                      yaxis_title='Count')
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Show Scatter Plot')

if scatter_button:
    st.write('Scatter Plot of Price vs. Odometer')
    fig = go.Figure(data=go.Scatter
                    (x=car_data['odometer'], 
                     y=car_data['price'], 
                     mode='markers'))
    
    fig.update_layout(title='Price vs. Odometer Reading',
                      xaxis_title='Odometer (miles)',
                      yaxis_title='Price (USD)')
    
    st.plotly_chart(fig, use_container_width=True)