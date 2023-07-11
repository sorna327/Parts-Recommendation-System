import streamlit as st
import pandas as pd

import  base64
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

set_background('demo2.jpg')

st.header("Home")

df=pd.read_csv('Currentdata5.csv')

# Example 1: Load image from a file
image_path = "1.jpg"
st.image(image_path, caption='')
st.write("Here the Products that are available in the company is available for purchase and they are used in various sector and department of development around the globe.")
st.write("Mostly Purchased Products some are Listed Below:")

sorted_df=df.sort_values('count',ascending=False)
sorted_df=sorted_df.drop(['count'],axis=1)
sorted_df=sorted_df.reset_index(drop=True)
sorted_df.index+=1
top_10=sorted_df.head(10)
st.write(top_10)
st.write("For Further Refernce Visit the Link Below")
st.write("https://www.caterpillar.com/")

st.write(""" 
**CONTACT US:**
         
CATERPILLAR CORPORATE CONTACT CENTER
 100 NE Adams St,
   Peoria, IL, 61629

 +1 (309) 675-2337

 +1 (888) 614-4328 (toll free)
         """)