import streamlit as st
import pandas as pd
import plotly.express as px

# Set page title
st.set_page_config(page_title=":blue[Research Profile, Work and Publications Explorer]", layout="wide")

# Images
image_background = "https://media.licdn.com/dms/image/v2/D4D16AQH6v8f4cpIOew/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1707996146169?e=1771459200&v=beta&t=QjufdJnCYQL2aYCOWEN1Uq3-78RFHPjgRf2c1gCm-vI"
image_profile = "https://media.licdn.com/dms/image/v2/D4D03AQFvKPU7S3FegA/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1707996011543?e=1771459200&v=beta&t=s5Vyv1rrJsGDzzfvXlhTIynE_G_F_EZGBgmI6etfV7k"
image_radar = "https://weatherblog.co.za/wp-content/uploads/2024/11/randfontein-tornado-south-africa-weather-2024-01-990x546.jpg"
image_network = "https://www.researchgate.net/profile/Liesl-Dyson-2/publication/323041147/figure/fig1/AS:592132125507584@1518186708264/South-African-Weather-Service-radar-coverage-network-in-2014-Irene-weather-office.png"
image_largeradar = "https://scontent-jnb2-1.xx.fbcdn.net/v/t39.30808-6/309667974_777404876977322_248156291405082512_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=ZLrOfCPQ8TAQ7kNvwHXxHjO&_nc_oc=Admu_vUVNesCYgPtciXwbGkeOWwIJCipVaTjohvM-KafnbKFjcGcyU_9qS1fGzXE1BY&_nc_zt=23&_nc_ht=scontent-jnb2-1.xx&_nc_gid=ytflBFKIW1KmW7hBNShxWw&oh=00_Afo5rKKykR1wfVFDAjgzXLEEicEicWE3tI1uaQjCug9eSg&oe=69824532"
image_ndwi = "https://i.ibb.co/675KF0NC/Jan-NDWI-mosaic-final1.jpg"
image_earth = "https://i.ibb.co/7xJs7GN7/southern-africa-weather-satellite-photos-Infrared-Southern-Africa.jpg"

# Sidebar Menu
st.sidebar.title(":red[Content]")
menu = st.sidebar.radio(
    "Go to:",
    [":green[Researcher Profile]", ":orange[Work Data Explorer]", ":yellow[Publications]", ":violet[Contact]"],
)

weather_data = pd.read_csv("D1H003.csv",delimiter=";")
weather_data = weather_data[['Year', 'Month', 'Day', 'Streamflow']]
weather_data.dropna(inplace=True)

# Sections based on menu selection
if menu == ":green[Researcher Profile]":
    st.header("**Researcher Overview**", divider="rainbow")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Jaco (PJ) de Wit"
    field = "Scientist Hydrometeorology"
    institution = "South African Weather Service"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Research Title:** {field}")
    st.write(f"**Institution:** {institution}")
    st.image(image_background)
    #st.image( , caption="Nature (Pixabay)"
    # Background information
    st.header("\nResearch background")
    st.write("Working in the hydro-sphere doing research and developing applications for the water sector. Focussing on Python coding and developing in-house scripts to process, manipulate, analyze and produce products to help managers, forecasts, clients and goverment in decision making.")
    st.image(image_earth)

elif menu == ":yellow[Publications]":
    st.title(":yellow[Publications]")
    st.markdown("<h1 style='color: #FFFF00'>--------------------------</h1>", unsafe_allow_html=True)
    st.header("Publications List and Links")
    orcid = "https://orcid.org/0000-0003-0112-274X"
    title = ["Evaluation of Rainfall Distribution Based on the Precipitation Concentration Index: A Case Study over the Selected Summer Rainfall Regions of South Africa",
             "Temporal Variability of Hydroclimatic Extremes: A Case Study of Vhembe, uMgungundlovu, and Lejweleputswa District Municipalities in South Africa",
             "Analysis of Drought Progression Physiognomies in South Africa"]
    journal = ["Hydrology", "Water", "Water"]
    link = ["10.3390/hydrology12060136", "10.3390/w16202924", "10.3390/w11020299"]
    authors = ["Christina M. Botai; Joel O. Botai; Mxolisi B. Mukhawana; Jaco de Wit; Ndumiso S. Masilela; Nosipho Zwane; Henerica Tazvinga",
               "Christina M. Botai; Jaco P. de Wit; Joel O. Botai",
               "Joel Ondego Botai; Christina M. Botai; Jaco P. de Wit; Masinde Muthoni; Abiodun M. Adeola"]
    doi = "https://doi.org/"
    for i in range(len(title)):
        st.markdown('---')
        st.write("**Title:**", title[i])
        st.write("**Journal:**", journal[i])
        st.write("**DOI Link:**", doi+link[i])
        #st.page_link(doi+link[i])
        st.write("**Authors:**", authors[i])
               
elif menu == ":orange[Work Data Explorer]":
    st.title(":orange[Work Data Explorer]")
    st.markdown("<h1 style='color: #FFA500'>--------------------------</h1>", unsafe_allow_html=True)
    #st.sidebar.header("Data Selection")
    st.header("Work Preview Selection")
    
    # Tabbed view for STEM data
    #data_option = st.sidebar.selectbox(
        #"Choose a dataset to explore", 
        #["Physics Experiments", "Astronomy Observations", "Weather Data"]
    #)
    data_option = st.selectbox(
        "Choose a dataset to explore", 
        ["Radar Observations", "Satellite Observations", "Weather Station Data"]
    )
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown("---")

    if data_option == "Radar Observations":
        st.write("### Radar Meteorological Observation and Products")
        st.image(image_network, caption="Radar instrument network of South Africa.")
        st.markdown("---")
        st.image(image_radar, caption="Radar measured reflectance tracking a tornado in 2024.")

    elif data_option == "Satellite Observations":
        st.write("### Satellite Observations and Derived Products")
        st.image(image_largeradar, caption="Convective Clouds from Satellite Derived Data.")
        st.markdown("---")
        st.image(image_ndwi, caption="Normalized Difference Water Index Calculated from Satellite Data.")

    elif data_option == "Weather Station Data":
        st.write("### Weather Station Data")
        #st.dataframe(weather_data)
        # Add widgets to filter by temperature and humidity
        year_filter = st.slider("Filter by year [from 1914 to 2021", 1914, 2021, (1914, 2021))
        filtered_weather = weather_data[weather_data["Year"].between(year_filter[0], year_filter[1])]
        st.write(f"Filtered Results for Temperature {year_filter}:")
        fig = px.line(filtered_weather, x=filtered_weather.Year, y=filtered_weather.Streamflow, title="Streamflow on Vaal River")
        st.subheader("Interactive Plotly Chart")
        st.plotly_chart(fig, use_container_width=True)
        #fig.show()
        #st.dataframe(filtered_weather)

elif menu == ":violet[Contact]":
    # Add a contact section
    st.header(":violet[Contact Information]")
    st.markdown("<h1 style='color: #7F00FF'>--------------------------</h1>", unsafe_allow_html=True)
    email = "jaco.dewit@weathersa.co.za"
    st.write(f"You can reach me at {email}.")
    st.image(image_profile)
