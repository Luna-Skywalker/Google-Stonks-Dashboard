import numpy as np
import pandas as pd
import plotly_express as px
import streamlit as st
import datetime as dt

st.set_page_config(page_title="Google Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide",
                   menu_items={
                       'About': "This is a dashboard for presenting Google Stocks information",
                       'Report a bug':"mailto:devasmita.2002@gmail.com",
                   })
st.title(":chart: Google Stock Dashboard :money_with_wings:")
st.markdown("---")
df = pd.read_csv("GOOGLE.csv")
placeholder = st.empty()
last6months = df.tail(250)
avg_high = np.mean(last6months['High'])
avg_low = np.mean(last6months['Low'])
avg_open = np.mean(last6months['Open'])
avg_close = np.mean(last6months['Close'])
# def str_to_datetime(s):
#     split = s.split('-')
#     year, month, day = int(split[0]), int(split[1]), int(split[2])
#     return dt.datetime(year=year, month=month, day=day)
# df['Date'] = df['Date'].apply(str_to_datetime)
df['Date'] = pd.to_datetime(df['Date'], errors = 'coerce', dayfirst=True, yearfirst=False)
df['MA10'] = df['Close'].rolling(window = 10).mean().reset_index(0, drop = True)
df['MA20'] = df['Close'].rolling(window = 20).mean().reset_index(0, drop = True)
df['Volatility'] = df['Close'].pct_change().rolling(window = 10).std().reset_index(0, drop = True)
with placeholder.container():
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric(label="Average high", value=f"$ {round(avg_high,3)}")
    kpi2.metric(label="Average low", value=f"$ {round(avg_low,3)}")
    kpi3.metric(label="Average opening", value=f"$ {round(avg_open,3)}")
    kpi4.metric(label="Average closing", value=f"$ {round(avg_close,3)}")

    fig_col1, fig_col2 = st.columns(2)
    with fig_col1:
        plotly_close = px.line(df, x = 'Date', y = 'Close', title = '<b>Stock Performance for GOOGLE</b>')
        st.plotly_chart(plotly_close)
    with fig_col2:
        plotly_moving = px.line(df, x = 'Date', y = ['Close', 'MA10', 'MA20'], title = '<b>Moving Averages for Stock GOOGLE</b>')
        st.plotly_chart(plotly_moving)
    fig_col3, fig_col4 = st.columns(2)
    with fig_col3:
        plotly_vola = px.line(df, x = 'Date', y = 'Volatility', title = '<b>Volatility of the Stock GOOGLE</b>')
        st.plotly_chart(plotly_vola)
    with fig_col4:
        plotly_sold = px.line(df, x = 'Date', y = 'Volume', title = '<b>Volume of Stock Sold</b>')
        st.plotly_chart(plotly_sold)    
# st.write(df.info())
# print(df.head(3))
    st.markdown("### Detailed View of the Data")
    st.dataframe(data=df, width=1900, height=370, hide_index=True)
# st.write('Hello world')