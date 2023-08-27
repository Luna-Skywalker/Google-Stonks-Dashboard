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
df['Average in a day'] = (df['Close']+df['High'])/2
df['MA10'] = df['Close'].rolling(window = 10).mean().reset_index(0, drop = True)
df['MA20'] = df['Close'].rolling(window = 20).mean().reset_index(0, drop = True)
df['Volatility'] = df['Close'].pct_change().rolling(window = 10).std().reset_index(0, drop = True)
with placeholder.container():
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric(label="Average high", value=f"$ {round(avg_high,3)}")
    kpi2.metric(label="Average low", value=f"$ {round(avg_low,3)}")
    kpi3.metric(label="Average opening", value=f"$ {round(avg_open,3)}")
    kpi4.metric(label="Average closing", value=f"$ {round(avg_close,3)}")
    st.markdown("---")
    # fig_col1, fig_col2 = st.columns(2)
    # with fig_col1:
    st.markdown("### Stock Performance for GOOGLE")
    plotly_close = px.line(df, x = 'Date', y = ['Open', 'Close', 'Average in a day'], title="<b>Opening and Closing Price</b>", width=1750, height=900)
    plotly_close.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                     dict(count=1,
                     step="day",
                     stepmode="backward"),
                     dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                     dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                     dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                     dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
        )
    )
    st.plotly_chart(plotly_close)
    plotly_high = px.line(df, x = 'Date', y = ['High', 'Low'], title="<b>High and Low</b>", width=1750, height=900)
    plotly_high.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                     dict(count=1,
                     step="day",
                     stepmode="backward"),
                     dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                     dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                     dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                     dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
        )
    )
    st.plotly_chart(plotly_high)
    # with fig_col2:
    st.markdown("### Moving Averages for GOOGLE Stock")
    plotly_moving = px.line(df, x = 'Date', y = ['Close', 'MA10', 'MA20'], width=1750, height=900)
    plotly_moving.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                     dict(count=1,
                     step="day",
                     stepmode="backward"),
                     dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                     dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                     dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                     dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
        )
    )
    st.plotly_chart(plotly_moving)
    # fig_col3, fig_col4 = st.columns(2)
    # with fig_col3:
    st.markdown("### Volatility of the GOOGLE Stock")
    plotly_vola = px.line(df, x = 'Date', y = 'Volatility', width=1750, height=900)
    plotly_vola.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                     dict(count=1,
                     step="day",
                     stepmode="backward"),
                     dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                     dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                     dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                     dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
        )
    )
    st.plotly_chart(plotly_vola)
    # with fig_col4:
        # plotly_sold = px.line(df, x = 'Date', y = 'Volume', title = '<b>Volume of Stock Sold</b>')
    st.markdown("### Volume of Stock Sold")    
    plotly_sold = px.area(df, x='Date', y='Volume', width=1750, height=900)
    plotly_sold.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                     dict(count=1,
                     step="day",
                     stepmode="backward"),
                     dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                     dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                     dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                     dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
        )
    )
    st.plotly_chart(plotly_sold)    
# st.write(df.info())
# print(df.head(3))
    st.markdown("### Detailed View of the Data")
    st.dataframe(data=df, width=1900, height=370, hide_index=True)
# st.write('Hello world')