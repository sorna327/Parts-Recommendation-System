import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import base64

df1 = pd.read_csv('Currentdata5.csv')

pivot_df1 = df1.pivot(index='SERVICE', columns='PART_NAME', values='count')
pivot_df1.fillna(0, inplace=True)
part_sim = cosine_similarity(pivot_df1.T)


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


def generate_string(string1, string2, string3, string4):
    given_parts = [string1, string2, string3, string4]

    similar_parts = []
    for part in given_parts:
        if part in pivot_df1.columns:
            part_index = pivot_df1.columns.get_loc(part)
            similar_part_indices = part_sim[part_index].argsort()[::-1][1:]  # Exclude the given part itself
            similar_parts.extend(pivot_df1.columns[similar_part_indices])

    if not similar_parts:
        st.write("No similar parts found.")
        return ""

    # Step 5: Recommend the 5th part
    recommendations = pivot_df1.loc[:, similar_parts].sum().sort_values(ascending=False)
    # Remove the given parts from the recommendations
    recommended_parts = recommendations[~recommendations.index.isin(given_parts)]

    if recommended_parts.empty:
        st.write("No recommended part found.")
        return ""

    fifth_part = recommended_parts.index[0]

    return fifth_part


def main():
    st.title("ADD TO CART")
    word_list = ['Screen Filters', 'Gaskets', 'Seals Gaskets and O-Rings', 'Bolts and Screws', 'Kit - Drivetrain and Steering', 'Washers and Spacers', 'Shims', 'Caps and Plugs', 'Impellers', 'Clamps and Clips', 'Hose Assemblies', 'Housings and Covers', 'Grommets', 'Fasteners Nuts', 'Hose adapters', 'Bearings', 'Kit - Maintenance', 'Kit - Engines', 'Springs', 'Water Pumps', 'Rotating Seals', 'Pins', 'Injectors', 'Valve Cartridges', 'Information Films', 'Rings', 'Grease', 'Valve Components', 'Driveshafts and Joint Groups', 'Friction Discs', 'Kit - Hydraulics', 'Retaining Rings', 'Thrust Washers', 'Bars Plates and Strips', 'Transmission Cases', 'Fasteners Studs', 'Solid Rods', 'Duo Cone Group', 'Brake Groups', 'Planet Carriers', 'Dowel Pins', 'Controls-Switching', 'Joystick Components', 'Breathers', 'Tubes', 'Tanks', 'Hydraulics Filter Components', 'Temperature Sensors', 'Mounts', 'Bearing Housings', 'No Data', 'Hyd Cylinder Piston', 'Separator Plates', 'Valve Groups and Assemblies', 'Brake Valves', 'Shafts', 'Fasteners Rivets', 'Connector', 'Fluid Filter', 'Hubs', 'Housing', 'Yoke Assemblies', 'Master Cylinders', 'Manually Operated Valves', 'Turbos and Turbo Groups', 'Planet Gears', 'Trunnion Supports', 'Sun Gears', 'Dealer Shop Supplies and Specialty', 'Shaft Seals', 'Sensors', 'Retaining Pins', 'DT Valve Groups', 'Thermostat', 'Tube Components', 'Other Non-Metallic Covers and Supports', 'Linkage Pins', 'Bridge', 'Pulleys', 'Spherical Balls', 'Controls-Primary', 'Custom Supports', 'Bulk Seals', 'Connector Components', 'Bearing', 'Yokes', 'Needs Class', 'Seat Assembly', 'Bearing Retainers', 'Accumulators and Accumulator Components', 'Cartridges', 'Rounds', 'Being reviewed', 'Position Sensors', 'Fuel Pumps', 'Buttons and Knobs', 'Threaded Bosses', 'Common Electrical Components', 'Brackets Supports and Mounts', 'Valve In-line', 'Harness Assembly', 'Dust Ejector Check Valves', 'Accumulators Receivers and Dryers', 'Hub', 'Trunnions', 'Carburetors and Governors', 'Gears', 'Brake Anchor', 'Other Metallic Covers', 'Control Units and ECMs', 'Dealer Service Tools', 'Impeller Hubs', 'Dampers', 'Tube and Bellows Assemblies', 'Speed and Timing Sensors', 'Miscellaneous Cylinder Components', 'Grab Handles', 'Kit - Electronics', 'Terminal Blocks', 'Belts', 'Spindles', 'P&M Pressure Plates and Blocks', 'Other Operator Control Components', 'Latches', 'P&M Actuator and Control Parts', 'Foam Insulation and Liners', 'Hose Guards', 'Oils', 'Wheels', 'Brake Linings', 'Cooling Module', 'Electrical Connectors', 'Radiator Caps', 'Control Valves', 'Fuel Filter Components', 'Levers and Links', 'Yoke', 'Trays', 'Information Plates', 'Seals', 'Covers', 'Pressure Caps', 'Bumpers', 'Foot Pedal', 'Manifolds', 'Structural Fabrications', 'Lube Filters', 'Elbows', 'Cabin Air', 'Compressor Bypass Valve', 'Heat Shrinks', 'Dipsticks', 'P&M Housings and Bodies', 'Keys', 'Clutch Piston', 'Engine Bearings', 'Power Socket', 'Hyd Cylinder Groups', 'Ignition Switch and Key', 'Brake Piston', 'One Piece', 'Alarm', 'Angles and Channels', 'Tank Groups and Assemblies', 'Hyd Cylinder Rod Assembly', 'Mounts Bushing', 'Pressure Switches', 'Service and Repair Drivetrain and Steering Kit', 'Yoke-Clevis', 'Spherical Rings', 'Bushing', 'Other Turbo Components', 'Engine Air Components', 'Parking Brake Discs', 'Supports', 'Gear Groups', 'Cooling Tanks', 'Rod Eye', 'Turbo Housings and Covers', 'Liquid Level Sensors', 'Air Cooler', 'Valves', 'P&M Gears and Gear Assemblies', 'Engine Covers', 'Hand Levers', 'Heaters', 'Fast Fill', 'Telematics', 'Temperature Switches']

    input_word1 = st.text_input("Search Item 1", "", key="text_input1")
    string1 = ""

    if input_word1:
        suggestions = [word for word in word_list if word.startswith(input_word1)]
        if suggestions:
            string1 = st.selectbox("Item No 1:", suggestions)

    input_word2 = st.text_input("Search Item 2", "", key="text_input2")
    string2 = ""

    if input_word2:
        suggestions = [word for word in word_list if word.startswith(input_word2)]
        if suggestions:
            string2 = st.selectbox("Item No 2:", suggestions)

    input_word3 = st.text_input("Search Item 3", "", key="text_input3")
    string3 = ""

    if input_word3:
        suggestions = [word for word in word_list if word.startswith(input_word3)]
        if suggestions:
            string3 = st.selectbox("Item No 3:", suggestions)

    input_word4 = st.text_input("Search Item 4", "", key="text_input4")
    string4 = ""

    if input_word4:
        suggestions = [word for word in word_list if word.startswith(input_word4)]
        if suggestions:
            string4 = st.selectbox("Item No 4:", suggestions)

    if string1 and string2 and string3 and string4:
        # Generate the result
        fifth_part = generate_string(string1, string2, string3, string4)

        # Display the result
        if fifth_part:
            st.write("This is our **Recommendation**:", fifth_part)
            st.write("Do you wish to **PURCHASE** the recommended part?")
            if st.button("Yes"):
                st.write("**The Items in the CART** : ",string1,",",string2,",",string3,",",string4,",",fifth_part)
                st.write("Thank you for the purchase from the **CATERPILLAR!**")
            if st.button("No"):
                st.write("**The Items in the CART** : ",string1,",",string2,",",string3,",",string4)
                st.write("Thank you for the purchase from the **CATERPILLAR!**")

if __name__ == "__main__":
    main()
