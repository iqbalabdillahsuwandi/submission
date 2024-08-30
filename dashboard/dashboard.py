import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')


def load_data(file_type):
    if file_type == 'day':
        data = pd.read_csv('https://raw.githubusercontent.com/iqbalabdillahsuwandi/submission/main/dashboard/day.csv')
    elif file_type == 'hour':
        data = pd.read_csv('https://raw.githubusercontent.com/iqbalabdillahsuwandi/submission/main/dashboard/hour.csv')
    else:
        data = pd.DataFrame()
    return data

#sidebar
with st.sidebar:
    st.image("https://raw.githubusercontent.com/iqbalabdillahsuwandi/submission/main/dashboard/bike.png")
    st.title("Bike Sharing")
    st.sidebar.header("Menu")
    data_set = st.sidebar.button('Information Data Set')
    data_day = st.sidebar.button('Data Day')
    data_hour = st.sidebar.button('Data Hour')

#Dashboard
if data_set:
    st.title('Data Set')
    st.write("Bike-sharing rental process is highly correlated to the environmental and seasonal settings. For instance, weather conditions, precipitation, day of week, season, hour of the day, etc. can affect the rental behaviors. The core data set is related to  the two-year historical log corresponding to years 2011 and 2012 from Capital Bikeshare system, Washington D.C., USA which is publicly available in http://capitalbikeshare.com/system-data. We aggregated the data on two hourly and daily basis and then extracted and added the corresponding weather and seasonal information. Weather information are extracted from http://www.freemeteo.com. ")
    st.write("For further information about this dataset please contact Hadi Fanaee-T (hadi.fanaee@fe.up.pt)")
 
elif data_day:
    st.title('Bicycle usage data by day')
    day_df = load_data('day')
      
    # Visualisasi
    season_avg = day_df.groupby('season')['registered'].mean().sort_values(ascending=False)
    
    st.write("### Average Users who register by Season")
    fig, ax = plt.subplots()
    ax.bar(season_avg.index, season_avg.values, color='skyblue')
    ax.set_title('Average Registered Users By Season')
    ax.set_xlabel('Season')
    ax.set_ylabel('Average Registered Users')
    st.pyplot(fig)
    st.caption("Information = 1:springer, 2:summer, 3:fall, 4:winter")

elif data_hour:
    st.title('bicycle usage data by hour.')
    hour_df = load_data('hour')
    
    # Visualisasi
    hourly_counts = hour_df.groupby('hr')['cnt'].sum()
    
    st.write("### Total Bicycle Users by Hour")
    fig, ax = plt.subplots()
    ax.plot(hourly_counts.index, hourly_counts.values, marker='o', linestyle='-', color='b')
    ax.set_title('Total by Hours')
    ax.set_xlabel('Hours')
    ax.set_ylabel('Total User')
    ax.grid(True)
    st.pyplot(fig)

else:
    st.title('Bike Sharing')
    st.write("Bike sharing systems are new generation of traditional bike rentals where whole process from membership, rental and return back has become automatic. Through these systems, user is able to easily rent a bike from a particular position and return back at another position. Currently, there are about over 500 bike-sharing programs around the world which is composed of over 500 thousands bicycles. Today, there exists great interest in these systems due to their important role in traffic, environmental and health issues. ")
    st.write("Apart from interesting real world applications of bike sharing systems, the characteristics of data being generated by these systems make them attractive for the research. Opposed to other transport services such as bus or subway, the duration of travel, departure and arrival position is explicitly recorded in these systems. This feature turns bike sharing system into a virtual sensor network that can be used for sensing mobility in the city. Hence, it is expected that most of important events in the city could be detected via monitoring these data.")
