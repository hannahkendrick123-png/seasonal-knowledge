from datetime import date
from pathlib import Path

from streamlit.testing.v1 import AppTest


APP_FILE = Path(__file__).resolve().parents[1] / "app.py"


def open_date_picker():
	app = AppTest.from_file(str(APP_FILE)).run()
	app.sidebar.radio[0].set_value("📅 Select a Date").run()
	return app


def test_select_a_date_page_is_available():
	app = open_date_picker()

	assert not app.exception
	assert any(header.value == "📅 Select a Date" for header in app.header)
	assert len(app.date_input) == 1


def test_date_range_displays_filtered_summary():
	app = open_date_picker()
	app.date_input[0].set_value((date(2025, 10, 1), date(2025, 10, 2))).run()

	assert not app.exception
	metrics = {metric.label: metric.value for metric in app.metric}
	assert metrics["Days"] == "2"
	assert metrics["Average Maximum Temperature"] == "24.6 °C"
	assert metrics["Total Rainfall"] == "0.0 mm"
	assert metrics["Rainy Days"] == "0"


def test_single_day_date_range_shows_one_day_summary():
	app = open_date_picker()
	app.date_input[0].set_value((date(2025, 10, 4), date(2025, 10, 4))).run()

	assert not app.exception
	metrics = {metric.label: metric.value for metric in app.metric}
	assert metrics["Days"] == "1"
	assert metrics["Total Rainfall"] == "4.4 mm"
	assert metrics["Rainy Days"] == "1"
