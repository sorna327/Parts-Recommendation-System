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
st.header("Services")
services=['','Drivetrain-Brakes-Rebuild', 'Drivetrain-Axle-Rebuild', 'Engine-Injector Group-Rebuild', 'Drivetrain-Brakes-Repair', 'Engine-Water Pump Group-Rebuild', 'Engine-Turbo Group-Rebuild', 'Drivetrain-Differential-Repair', 'Engine-Engine cooling system-Replacement']
target_service=st.selectbox("Please Select the Services Which You Prefer",services)


def find_parts_by_service(csv_file, target_service):
    df = pd.read_csv(csv_file)
    
    filtered_df = df[df['SERVICE'] == target_service]

    parts = filtered_df['PART_NAME'].tolist()
    
    return parts

csv_file = 'Currentdata5.csv'
parts_list = find_parts_by_service(csv_file, target_service)

if parts_list:
    st.write(f"**Parts provided in {target_service}:**")
    for part in parts_list:
        st.write("->",part)
else:
    st.write(f"{target_service}")
import streamlit as st
import subprocess

def main():
        st.write("Do you need to **PURCHASE** a Service?")
        if st.button("Yes"):
             st.write("Thank you for the **PURCHASE**")
             path_to_other_page = "C:/Users/Admin/OneDrive/Desktop/pages/Parts_Recommendation.py"
             subprocess.Popen(["python","-m","streamlit", "run", path_to_other_page])

if target_service is not None:
     main()