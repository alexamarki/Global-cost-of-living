import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter
import itertools

df = pd.read_csv('cost-of-living_v2.csv', sep=',')
del df['data_quality']
df = df.drop(df[df.isna().sum(1) > 3].index)
del df['x42']
del df['x43']
for i in ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10',
          'x11', 'x12', 'x13', 'x14', 'x15', 'x16', 'x17', 'x18', 'x19', 'x20',
          'x21', 'x22', 'x23', 'x24', 'x25', 'x26', 'x27', 'x28', 'x29', 'x30',
          'x31', 'x32', 'x33', 'x34', 'x35', 'x36', 'x37', 'x38', 'x39', 'x40',
          'x41', 'x44', 'x45', 'x46', 'x47', 'x48', 'x49', 'x50',
          'x51', 'x52', 'x53', 'x54', 'x55']:
    mean_values = df.groupby('country')[i].mean()
    df[i] = df.apply(lambda row: mean_values[row['country']] if pd.isnull(row[i]) else row[i], axis=1)
    df[i].fillna(df[i].mean(), inplace=True)
df['food'] = df.x10 * 14 + df.x11 * 1.5 + df.x12 * (
            21 / 12) + df.x13 * 1.2 + df.x14 * 2.4 + df.x15 * 2.31 + df.x16 * 2.55 + df.x17 * 2.55 + df.x21 * 0.75 + df.x20 * 8.1 + df.x23 * 40 + df.x9 * 15
df[
    'life'] = df.x48 + df.x29 + df.x33 * 187.5 + df.x35 * 0.008 + df.x37 * 2 + df.x38 + df.x44 / 6 + df.x45 / 6 + df.x46 / 12 + df.x47 / 12

st.header("Global cost of living")
st.subheader(
    "A dashboard regarding the global cost of living as of December 2022, \
    (data is available for the majority of countries, save for ones with \
     political instability and lack of outside supervision)", divider='rainbow')

st.subheader("Feature description")
st.markdown('This dataset has 2 columns denoting the :red[country] and the :red[city] in which the data were gathered respectively, \
            55 columns (:red[x1]-:red[x55]) with data about specific prices/percentages related to the cost of living around the world, as \
            well as a :red[data_quality] column, which is used as a marker for the level of credibility of the data')
expander_x = st.expander("To get more information on what x1-x55 mean, click this")
expander_x.write("""
x1	Meal, Inexpensive Restaurant (USD)  
x2	Meal for 2 People, Mid-range Restaurant, Three-course (USD)  
x3	McMeal at McDonalds (or Equivalent Combo Meal) (USD)  
x4	Domestic Beer (0.5 liter draught, in restaurants) (USD)  
x5	Imported Beer (0.33 liter bottle, in restaurants) (USD)  
x6	Cappuccino (regular, in restaurants) (USD)  
x7	Coke/Pepsi (0.33 liter bottle, in restaurants) (USD)  
x8	Water (0.33 liter bottle, in restaurants) (USD)  
x9	Milk (regular), (1 liter) (USD)  
x10	Loaf of Fresh White Bread (500g) (USD)  
x11	Rice (white), (1kg) (USD)  
x12	Eggs (regular) (12) (USD)  
x13	Local Cheese (1kg) (USD)  
x14	Chicken Fillets (1kg) (USD)  
x15	Beef Round (1kg) (or Equivalent Back Leg Red Meat) (USD)  
x16	Apples (1kg) (USD)  
x17	Banana (1kg) (USD)  
x18	Oranges (1kg) (USD)  
x19	Tomato (1kg) (USD)  
x20	Potato (1kg) (USD)  
x21	Onion (1kg) (USD)  
x22	Lettuce (1 head) (USD)  
x23	Water (1.5 liter bottle, at the market) (USD)  
x24	Bottle of Wine (Mid-Range, at the market) (USD)  
x25	Domestic Beer (0.5 liter bottle, at the market) (USD)  
x26	Imported Beer (0.33 liter bottle, at the market) (USD)  
x27	Cigarettes 20 Pack (Marlboro) (USD)  
x28	One-way Ticket (Local Transport) (USD)  
x29	Monthly Pass (Regular Price) (USD)  
x30	Taxi Start (Normal Tariff) (USD)  
x31	Taxi 1km (Normal Tariff) (USD)  
x32	Taxi 1hour Waiting (Normal Tariff) (USD)  
x33	Gasoline (1 liter) (USD)  
x34	Volkswagen Golf 1.4 90 KW Trendline (Or Equivalent New Car) (USD)  
x35	Toyota Corolla Sedan 1.6l 97kW Comfort (Or Equivalent New Car) (USD)  
x36	Basic (Electricity, Heating, Cooling, Water, Garbage) for 85m2 Apartment (USD)  
x37	1 min. of Prepaid Mobile Tariff Local (No Discounts or Plans) (USD)  
x38	Internet (60 Mbps or More, Unlimited Data, Cable/ADSL) (USD)  
x39	Fitness Club, Monthly Fee for 1 Adult (USD)  
x40	Tennis Court Rent (1 Hour on Weekend) (USD)  
x41	Cinema, International Release, 1 Seat (USD)  
x42	Preschool (or Kindergarten), Full Day, Private, Monthly for 1 Child (USD)  
x43	International Primary School, Yearly for 1 Child (USD)  
x44	1 Pair of Jeans (Levis 501 Or Similar) (USD)  
x45	1 Summer Dress in a Chain Store (Zara, H&M, …) (USD)  
x46	1 Pair of Nike Running Shoes (Mid-Range) (USD)  
x47	1 Pair of Men Leather Business Shoes (USD)  
x48	Apartment (1 bedroom) in City Centre (USD)  
x49	Apartment (1 bedroom) Outside of Centre (USD)  
x50	Apartment (3 bedrooms) in City Centre (USD)  
x51	Apartment (3 bedrooms) Outside of Centre (USD)  
x52	Price per Square Meter to Buy Apartment in City Centre (USD)  
x53	Price per Square Meter to Buy Apartment Outside of Centre (USD)  
x54	Average Monthly Net Salary (After Tax) (USD)  
x55	Mortgage Interest Rate in Percentages (%), Yearly, for 20 Years Fixed-Rate  
""")

st.subheader("Data overview")
st.markdown('Before displaying the dataset, it has to first be cleaned up. \
            I am also going to add two other columns based on my observations')
expander = st.expander("See the code that performs data cleanup and transformation")
expander.code("""
df = pd.read_csv('cost-of-living_v2.csv')
del df['data_quality']
df = df.drop(df[df.isna().sum(1) > 3].index)
del df['x42']
del df['x43']
for i in ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10',
          'x11', 'x12', 'x13', 'x14', 'x15', 'x16', 'x17', 'x18', 'x19', 'x20',
          'x21', 'x22', 'x23', 'x24', 'x25', 'x26', 'x27', 'x28', 'x29', 'x30',
          'x31', 'x32', 'x33', 'x34', 'x35', 'x36', 'x37', 'x38', 'x39', 'x40',
          'x41', 'x44', 'x45', 'x46', 'x47', 'x48', 'x49', 'x50',
          'x51', 'x52', 'x53', 'x54', 'x55']:
    mean_values = df.groupby('country')[i].mean()
    df[i] = df.apply(lambda row: mean_values[row['country']] if pd.isnull(row[i]) else row[i], axis=1)
    df[i].fillna(df[i].mean(), inplace=True)
df['food'] = df.x10*14 + df.x11*1.5 + df.x12*(21/12) + df.x13*1.2 + df.x14*2.4 + df.x15*2.31 + df.x16*2.55 + df.x17*2.55 + df.x21*0.75 + df.x20*8.1 + df.x23*40 + df.x9*15
df['life'] = df.x48 + df.x29 + df.x33*187.5 + df.x35*0.008 + df.x37*2 + df.x38 + df.x44/6 + df.x45/6 + df.x46/12 + df.x47/12
""")
st.dataframe(data=df)

st.subheader("Dashboard")
country_cities = df.country.value_counts()
country_top = list(country_cities.iloc[0:12].index)
country_cities.index = country_cities.index.map(lambda x: x if x in country_top else 'Other')
country_cities = country_cities.groupby('country').sum()
country_cities = country_cities.sort_values()
country_cities = country_cities.reset_index()
fig = px.pie(country_cities, values='count', names='country', color='country',
             hover_name="country", hover_data=['count'], hole=.3)
st.markdown('This is how much data there is on each specific country')
st.plotly_chart(fig)
st.markdown("And here's how much data there is on cities with different salaries")
fig1 = px.histogram(df, x="x54")
fig1.update_layout(xaxis_title="Average monthly salary")
st.plotly_chart(fig1)
st.markdown("Finally, here's a comparison between salary and prices per square meter outside city centre")
fig2 = px.scatter(df, x="x53", y="x54", color='country', hover_name="country")
fig2.update_layout(
    xaxis=dict(
        rangeslider=dict(
            visible=True
        ),
        type="linear"
    ),
    xaxis_title="Price per square meter (outside city centre)",
    yaxis_title="Average monthly salary"
)
st.plotly_chart(fig2)


