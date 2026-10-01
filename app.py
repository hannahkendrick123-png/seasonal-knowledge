import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from season_logic import add_seasons
from data_loader import load_weather_data, load_season_info
from analysis import calculate_season_statistics, seasonal_summary


st.set_page_config(
	page_title="Seasonal Knowledge Explorer",
	page_icon="🌿",
	layout="wide"
)

st.title("🌿 Seasonal Knowledge Explorer")

try:
	weather = load_weather_data()
	season_info = load_season_info()
	weather = add_seasons(weather)
except Exception as error:
	st.error(f"Error loading data: {error}")
	st.stop()

st.sidebar.title("Navigation")
page = st.sidebar.radio(
	"Choose a page:",
	["Home", "Seasonal Explorer", "Weather Analysis"]
)

if page == "Home":
	st.header("Explore seasonal knowledge and weather patterns")
	st.write(
		"This interactive application explores published Indigenous "
		"seasonal information and investigates associated weather observations."
	)
	st.subheader("What can you do?")
	st.write(
		"Use the navigation menu to explore seasonal information, analyse "
		"weather observations, and compare weather patterns across seasons."
	)
	st.info(
		"Cultural information displayed in this application comes from "
		"recognised published sources."
	)
	st.subheader("Dataset information")
	st.write(f"Number of weather records: {len(weather)}")
	st.write(f"Number of seasonal categories: {weather['season'].nunique()}")

elif page == "Seasonal Explorer":
	st.header("🌿 Seasonal Explorer")
	st.write("Select a season to view published information associated with that seasonal period.")
	selected_season = st.selectbox("Choose a season:", season_info["season"].tolist())
	selected = season_info[season_info["season"] == selected_season].iloc[0]
	st.subheader(selected["season"])
	st.write("Typical period:")
	st.write(selected["period"])
	st.write("Environmental indicators:")
	st.write(selected["environmental_signs"])
	st.caption(f"Source: {selected['source']}")

elif page == "Weather Analysis":
	st.header("📊 Weather Analysis")
	selected_season = st.selectbox("Choose a season:", sorted(weather["season"].unique()))
	statistics = calculate_season_statistics(weather, selected_season)
	st.subheader(f"{selected_season} Summary")

	col1, col2, col3, col4 = st.columns(4)
	col1.metric("Average Maximum Temperature", f"{statistics['average_max_temp']:.1f} °C")
	col2.metric("Average Minimum Temperature", f"{statistics['average_min_temp']:.1f} °C")
	col3.metric("Total Rainfall", f"{statistics['total_rainfall']:.1f} mm")
	col4.metric("Rainy Days", int(statistics["rainy_days"]))

	selected_data = weather[weather["season"] == selected_season]
	st.subheader("Daily Maximum Temperature")
	fig, ax = plt.subplots()
	ax.plot(selected_data["date"], selected_data["max_temp"])
	ax.set_xlabel("Date")
	ax.set_ylabel("Maximum Temperature (°C)")
	ax.set_title(f"{selected_season} Maximum Temperature")
	fig.autofmt_xdate(rotation=45)
	fig.tight_layout()
	st.pyplot(fig)
	plt.close(fig)

	st.subheader("Comparison Across Seasons")
	summary = seasonal_summary(weather)
	st.dataframe(summary, use_container_width=True)

	st.subheader("Rainy Days by Season")
	fig2, ax2 = plt.subplots()
	ax2.bar(summary["season"], summary["rainy_days"])
	ax2.set_xlabel("Season")
	ax2.set_ylabel("Number of Rainy Days")
	ax2.set_title("Rainy Days by Season")
	fig2.autofmt_xdate(rotation=45)
	fig2.tight_layout()
	st.pyplot(fig2)
	plt.close(fig2)

	st.subheader("Average Maximum Temperature by Season")
	fig3, ax3 = plt.subplots()
	ax3.bar(summary["season"], summary["average_max_temp"])
	ax3.set_xlabel("Season")
	ax3.set_ylabel("Average Maximum Temperature (°C)")
	ax3.set_title("Average Maximum Temperature by Season")
	fig3.autofmt_xdate(rotation=45)
	fig3.tight_layout()
	st.pyplot(fig3)
	plt.close(fig3)
