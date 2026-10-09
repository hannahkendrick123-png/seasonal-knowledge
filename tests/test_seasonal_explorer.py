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

def test_bunuru_displays_image_with_attribution():
	app = open_seasonal_explorer()
	app.selectbox[0].set_value("Bunuru").run()

	assert not app.exception
	assert len(app.get("image")) == 1
	assert any("Mark Marathon" in element.value for element in app.markdown)
	assert any("CC BY-SA 4.0" in element.value for element in app.markdown)


def test_djeran_displays_image_with_attribution():
	app = open_seasonal_explorer()
	app.selectbox[0].set_value("Djeran").run()

	assert not app.exception
	assert len(app.get("image")) == 1
	assert any("JJ Harrison" in element.value for element in app.markdown)
	assert any("CC BY-SA 3.0" in element.value for element in app.markdown)


def test_makuru_displays_image_with_attribution():
	app = open_seasonal_explorer()
	app.selectbox[0].set_value("Makuru").run()

	assert not app.exception
	assert len(app.get("image")) == 1
	assert any("Sam Genas" in element.value for element in app.markdown)
	assert any("CC BY-SA 3.0" in element.value for element in app.markdown)


def test_djilba_displays_image_with_attribution():
	app = open_seasonal_explorer()
	app.selectbox[0].set_value("Djilba").run()

	assert not app.exception
	assert len(app.get("image")) == 1
	assert any("Melburnian" in element.value for element in app.markdown)
	assert any("CC BY-SA 3.0" in element.value for element in app.markdown)


def test_kambarang_displays_image_with_attribution():
	app = open_seasonal_explorer()
	app.selectbox[0].set_value("Kambarang").run()

	assert not app.exception
	assert len(app.get("image")) == 1
	assert any("Gnangarra" in element.value for element in app.markdown)
	assert any("CC BY 2.5 AU" in element.value for element in app.markdown)
