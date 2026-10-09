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
	["🏠 Home", "🌼 Seasonal Overview", "📊 Weather Analysis", "📅 Select a Date"]
)

if page == "🏠 Home":
	st.markdown(
		"""
		<style>
		.stApp {
			background-color: #a4baa6;
		}
		</style>
		""",
		unsafe_allow_html=True,
	)
	st.header("Explore seasonal knowledge and weather patterns")
	st.write(
		"This interactive application explores published Indigenous "
		"seasonal information and investigates associated weather observations."
	)
	st.image(
		"https://upload.wikimedia.org/wikipedia/commons/b/bc/Noongar1.jpg"
		"?utm_source=en.wikipedia.org&utm_campaign=imageinfo"
		"&utm_content=thumbnail_unscaled",
		caption="Noongar groups of the Southwest of Western Australia",
		width=500,
	)
	st.markdown(
		"Map by [John D. Croft](https://commons.wikimedia.org/wiki/"
		"File:Noongar1.jpg), via Wikimedia Commons, licensed under "
		"[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)."
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

elif page == "🌼 Seasonal Overview":
	st.markdown(
		"""
		<style>
		.stApp {
			background-color: #a4bab9;
		}
		</style>
		""",
		unsafe_allow_html=True,
	)
	st.header("🌼 Seasonal Overview")
	st.write("Select a season to view published information associated with that seasonal period.")
	selected_season = st.selectbox("Choose a season:", season_info["season"].tolist())
	selected = season_info[season_info["season"] == selected_season].iloc[0]
	st.subheader(selected["season"])
	st.write("Typical period:")
	st.write(selected["period"])
	st.write("Environmental indicators:")
	st.write(selected["environmental_signs"])
	if selected_season == "Birak":
		st.image(
			"https://thumb.wikimedia.org/wikipedia/commons/thumb/5/58/"
			"Christmas_tree_02_gnangarra.jpg/1920px-Christmas_tree_02_gnangarra.jpg"
			"?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=thumbnail",
			caption="Western Australian Christmas tree (Nuytsia floribunda)",
		)
		st.markdown(
			"Image by [Gnangarra](https://commons.wikimedia.org/wiki/"
			"File:Christmas_tree_02_gnangarra.jpg), via Wikimedia Commons, "
			"licensed under [CC BY 2.5 AU]"
			"(https://creativecommons.org/licenses/by/2.5/au/deed.en)."
		)
	elif selected_season == "Bunuru":
		st.image(
			"https://thumb.wikimedia.org/wikipedia/commons/thumb/3/33/"
			"Corymbia_aparrerinja_blossom.jpg/1280px-Corymbia_aparrerinja_blossom.jpg"
			"?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=thumbnail",
			caption="Corymbia aparrerinja blossom",
		)
		st.markdown(
			"Image by [Mark Marathon](https://commons.wikimedia.org/wiki/"
			"File:Corymbia_aparrerinja_blossom.jpg), via Wikimedia Commons, "
			"licensed under [CC BY-SA 4.0]"
			"(https://creativecommons.org/licenses/by-sa/4.0/)."
		)
	elif selected_season == "Djeran":
		st.image(
			"https://thumb.wikimedia.org/wikipedia/commons/thumb/a/a4/"
			"Corymbia_ficifolia_Flowers.jpg/1280px-Corymbia_ficifolia_Flowers.jpg"
			"?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=thumbnail",
			caption="Flowering Corymbia ficifolia",
		)
		st.markdown(
			"Image by [JJ Harrison](https://commons.wikimedia.org/wiki/"
			"File:Corymbia_ficifolia_Flowers.jpg), via Wikimedia Commons, "
			"licensed under [CC BY-SA 3.0]"
			"(https://creativecommons.org/licenses/by-sa/3.0/)."
		)
	elif selected_season == "Makuru":
		st.image(
			"https://upload.wikimedia.org/wikipedia/commons/0/05/"
			"Dianella_revoluta.jpg?utm_source=en.wikipedia.org"
			"&utm_campaign=imageinfo&utm_content=thumbnail_unscaled",
			caption="Dianella revoluta (Black-anther Flax-lily)",
		)
		st.markdown(
			"Image by [Sam Genas](https://commons.wikimedia.org/wiki/"
			"File:Dianella_revoluta.jpg), via Wikimedia Commons, "
			"licensed under [CC BY-SA 3.0]"
			"(https://creativecommons.org/licenses/by-sa/3.0/)."
		)
	elif selected_season == "Djilba":
		st.image(
			"https://upload.wikimedia.org/wikipedia/commons/9/9b/"
			"Acacia_pycnantha_Golden_Wattle.jpg?utm_source=en.wikipedia.org"
			"&utm_campaign=imageinfo&utm_content=thumbnail_unscaled",
			caption="Acacia pycnantha (Golden Wattle)",
		)
		st.markdown(
			"Image by [Melburnian](https://commons.wikimedia.org/wiki/"
			"File:Acacia_pycnantha_Golden_Wattle.jpg), via Wikimedia Commons, "
			"licensed under [CC BY-SA 3.0]"
			"(https://creativecommons.org/licenses/by-sa/3.0/)."
		)
	elif selected_season == "Kambarang":
		st.image(
			"https://thumb.wikimedia.org/wikipedia/commons/thumb/0/0a/"
			"Anigozanthos_manglesii_gnangarra-1007.jpg/3840px-"
			"Anigozanthos_manglesii_gnangarra-1007.jpg"
			"?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=thumbnail",
			caption="Anigozanthos manglesii (Red and Green Kangaroo Paw)",
		)
		st.markdown(
			"Image by [Gnangarra](https://commons.wikimedia.org/wiki/"
			"File:Anigozanthos_manglesii_gnangarra-1007.jpg), "
			"via Wikimedia Commons, licensed under [CC BY 2.5 AU]"
			"(https://creativecommons.org/licenses/by/2.5/au/deed.en)."
		)
	st.caption(f"Source: {selected['source']}")

elif page == "📅 Select a Date":
	st.markdown(
		"""
		<style>
		.stApp {
			background-color: #d1c290;
		}
		</style>
		""",
		unsafe_allow_html=True,
	)
	st.header("📅 Select a Date")
	st.write("Choose a date range to explore the weather observations in that period.")

	available_start = weather["date"].min().date()
	available_end = weather["date"].max().date()
	selected_dates = st.date_input(
		"Choose a date range:",
		value=(available_start, available_end),
		min_value=available_start,
		max_value=available_end,
	)

	if not isinstance(selected_dates, tuple) or len(selected_dates) != 2:
		st.info("Select both a start date and an end date to view the analysis.")
		st.stop()

	start_date, end_date = selected_dates
	selected_weather = weather[
		weather["date"].between(pd.Timestamp(start_date), pd.Timestamp(end_date))
	]
	if selected_weather.empty:
		st.warning("No weather observations were found in that date range.")
		st.stop()

	st.caption(
		f"Showing observations from {start_date:%d %b %Y} "
		f"to {end_date:%d %b %Y}."
	)

	st.subheader("Selected Period Summary")
	col1, col2, col3, col4, col5 = st.columns(5)
	col1.metric("Days", len(selected_weather))
	col2.metric("Average Maximum Temperature", f"{selected_weather['max_temp'].mean():.1f} °C")
	col3.metric("Average Minimum Temperature", f"{selected_weather['min_temp'].mean():.1f} °C")
	col4.metric("Total Rainfall", f"{selected_weather['rainfall'].sum():.1f} mm")
	col5.metric("Rainy Days", int((selected_weather["rainfall"] > 0).sum()))

	selected_season = st.selectbox(
		"Choose a season:",
		sorted(selected_weather["season"].unique()),
	)
	statistics = calculate_season_statistics(selected_weather, selected_season)
	st.subheader(f"{selected_season} Summary")
	col1, col2, col3, col4 = st.columns(4)
	col1.metric("Average Maximum Temperature", f"{statistics['average_max_temp']:.1f} °C")
	col2.metric("Average Minimum Temperature", f"{statistics['average_min_temp']:.1f} °C")
	col3.metric("Total Rainfall", f"{statistics['total_rainfall']:.1f} mm")
	col4.metric("Rainy Days", int(statistics["rainy_days"]))

	selected_data = selected_weather[selected_weather["season"] == selected_season]
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

	st.subheader("Comparison Across Seasons in Selected Period")
	summary = seasonal_summary(selected_weather)
	st.dataframe(summary, use_container_width=True)

elif page == "📊 Weather Analysis":
	st.markdown(
		"""
		<style>
		.stApp {
			background-color: #c2a7a7;
		}
		</style>
		""",
		unsafe_allow_html=True,
	)
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
