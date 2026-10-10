import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')

st.title('California Housing Data (1990) by Sichen Li')

df = pd.read_csv('housing.csv')

# 1. 滑块：Minimal Median House Value
value_filter = st.slider('Minimal Median House Value', 0, 500001, 200000)

st.subheader('See more filters in the sidebar:')

# 2. 侧边栏多选：ocean_proximity
location_filter = st.sidebar.multiselect(
    'Choose the location type',
    df.ocean_proximity.unique(),
    df.ocean_proximity.unique()
)

# 3. 侧边栏单选：收入水平
income_filter = st.sidebar.radio(
    'Choose income level',
    ('Low', 'Medium', 'High')
)

# 按 median_house_value 过滤
df = df[df.median_house_value >= value_filter]

# 按 ocean_proximity 过滤
df = df[df.ocean_proximity.isin(location_filter)]

# 按收入水平过滤
if income_filter == 'Low':
    df = df[df.median_income <= 2.5]
elif income_filter == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
elif income_filter == 'High':
    df = df[df.median_income >= 4.5]

# 显示地图
st.map(df)

# 显示直方图
st.subheader('Histogram of Median House Value')
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(df.median_house_value, bins=30)
ax.set_xlabel('Median House Value')
ax.set_ylabel('Frequency')
st.pyplot(fig)