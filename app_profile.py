import streamlit as st
import pandas as pd
import numpy as np
import os
from PIL import Image

# Title of the app
st.title(":blue[Researcher Profile Page]")
#st.title("<h1 style='color: #FF5733;'>Researcher Profile Page</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='color: #FF5733;'>----------------------------------------------</h1>", unsafe_allow_html=True)

# Collect basic information
name = "Jaco (PJ) de Wit"
field = "Scientist Hydrometeorology"
institution = "South African Weather Service"

# Display basic profile information
st.header("**Researcher Overview**", divider="rainbow")
st.write(f"**Name:** {name}")
st.write(f"**Research Title:** {field}")
st.write(f"**Institution:** {institution}")
image_profile = "https://media.licdn.com/dms/image/v2/D4D03AQFvKPU7S3FegA/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1707996011543?e=1771459200&v=beta&t=s5Vyv1rrJsGDzzfvXlhTIynE_G_F_EZGBgmI6etfV7k"
image_background = "https://media.licdn.com/dms/image/v2/D4D16AQH6v8f4cpIOew/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1707996146169?e=1771459200&v=beta&t=QjufdJnCYQL2aYCOWEN1Uq3-78RFHPjgRf2c1gCm-vI"
# Background information
st.header("\nResearch background")
st.write("Working in the hydro-sphere doing research and developing applications for the water sector. Focussing on Python coding and developing in-house scripts to process, manipulate, analyze and produce products to help managers, forecasts, clients and goverment in decision making.")

st.markdown("Work activities:")
st.markdown("• Python / Bash / Linux")
st.markdown("• GIS and Remote Sensing")
st.markdown("• Data processing and ETL")
st.markdown("• Hydrological Modelling")
st.markdown("• Data visualisation and analysis")
image_radar = "https://weatherblog.co.za/wp-content/uploads/2024/11/randfontein-tornado-south-africa-weather-2024-01-990x546.jpg"
image_network = "https://www.researchgate.net/profile/Liesl-Dyson-2/publication/323041147/figure/fig1/AS:592132125507584@1518186708264/South-African-Weather-Service-radar-coverage-network-in-2014-Irene-weather-office.png"
image_largeradar = "https://scontent-jnb2-1.xx.fbcdn.net/v/t39.30808-6/309667974_777404876977322_248156291405082512_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=ZLrOfCPQ8TAQ7kNvwHXxHjO&_nc_oc=Admu_vUVNesCYgPtciXwbGkeOWwIJCipVaTjohvM-KafnbKFjcGcyU_9qS1fGzXE1BY&_nc_zt=23&_nc_ht=scontent-jnb2-1.xx&_nc_gid=ytflBFKIW1KmW7hBNShxWw&oh=00_Afo5rKKykR1wfVFDAjgzXLEEicEicWE3tI1uaQjCug9eSg&oe=69824532"
image_ndwi = "https://i.ibb.co/675KF0NC/Jan-NDWI-mosaic-final1.jpg"

st.image(
    image_largeradar,
    caption="Convective clouds over South Africa on a radar product"
)

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add STEM Data Section
st.header("Explore STEM Data")

# Generate dummy data
physics_data = pd.DataFrame({
    "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
    "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2024-01-01", periods=5),
})

astronomy_data = pd.DataFrame({
    "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
    "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
})

weather_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

# Tabbed view for STEM data
st.subheader("STEM Data Viewer")
data_option = st.selectbox(
    "Choose a dataset to explore", 
    ["Physics Experiments", "Astronomy Observations", "Weather Data"]
)

if data_option == "Physics Experiments":
    st.write("### Physics Experiment Data")
    st.dataframe(physics_data)
    # Add widget to filter by Energy levels
    energy_filter = st.slider("Filter by Energy (MeV)", 0.0, 10.0, (0.0, 10.0))
    filtered_physics = physics_data[
        physics_data["Energy (MeV)"].between(energy_filter[0], energy_filter[1])
    ]
    st.write(f"Filtered Results for Energy Range {energy_filter}:")
    st.dataframe(filtered_physics)

elif data_option == "Astronomy Observations":
    st.write("### Astronomy Observation Data")
    st.dataframe(astronomy_data)
    # Add widget to filter by Brightness
    brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
    filtered_astronomy = astronomy_data[
        astronomy_data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
    ]
    st.write(f"Filtered Results for Brightness Range {brightness_filter}:")
    st.dataframe(filtered_astronomy)

elif data_option == "Weather Data":
    st.write("### Weather Data")
    st.dataframe(weather_data)
    # Add widgets to filter by temperature and humidity
    temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
    humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
    filtered_weather = weather_data[
        weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
        weather_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
    ]
    st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
    st.dataframe(filtered_weather)

# Add a contact section
st.header("Contact Information")
email = "jane.doe@example.com"
st.write(f"You can reach {name} at {email}.")
