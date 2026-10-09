from pathlib import Path

from streamlit.testing.v1 import AppTest


APP_FILE = Path(__file__).resolve().parents[1] / "app.py"


def open_weather_analysis():
	app = AppTest.from_file(str(APP_FILE)).run()
	app.sidebar.radio[0].set_value("🌦️ Weather").run()
	return app


def test_analysis_subpage_shows_selected_season_summary():
	app = open_weather_analysis()

	assert not app.exception
	assert [radio.value for radio in app.sidebar.radio] == [
		"🌦️ Weather",
		"Analysis",
	]
	assert any(header.value == "Birak Summary" for header in app.subheader)
	assert any(header.value == "Daily Maximum Temperature" for header in app.subheader)
	assert len(app.metric) == 4


def test_comparison_subpage_shows_comparative_graph_sections():
	app = open_weather_analysis()
	app.sidebar.radio[1].set_value("Comparison").run()

	assert not app.exception
	assert any(
		header.value == "Comparison Across Seasons"
		for header in app.subheader
	)
	assert any(header.value == "Rainy Days by Season" for header in app.subheader)
	assert any(
		header.value == "Average Maximum Temperature by Season"
		for header in app.subheader
	)
	assert len(app.get("dataframe")) == 1
	assert len(app.metric) == 0
	assert not any(
		header.value == "Daily Maximum Temperature"
		for header in app.subheader
	)
