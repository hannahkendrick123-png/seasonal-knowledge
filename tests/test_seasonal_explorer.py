from pathlib import Path

from streamlit.testing.v1 import AppTest


APP_FILE = Path(__file__).resolve().parents[1] / "app.py"


def open_seasonal_explorer():
	app = AppTest.from_file(str(APP_FILE)).run()
	app.sidebar.radio[0].set_value("Seasonal Explorer").run()
	return app


def test_birak_displays_image_with_attribution():
	app = open_seasonal_explorer()

	assert not app.exception
	assert len(app.get("image")) == 1
	assert any("Gnangarra" in element.value for element in app.markdown)
	assert any("CC BY 2.5 AU" in element.value for element in app.markdown)


def test_other_seasons_do_not_display_birak_image():
	app = open_seasonal_explorer()
	app.selectbox[0].set_value("Bunuru").run()

	assert not app.exception
	assert len(app.get("image")) == 0
