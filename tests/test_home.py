from pathlib import Path

from streamlit.testing.v1 import AppTest


APP_FILE = Path(__file__).resolve().parents[1] / "app.py"


def test_home_displays_noongar_map_with_attribution():
	app = AppTest.from_file(str(APP_FILE)).run()

	assert not app.exception
	assert len(app.get("image")) == 1
	assert any("John D. Croft" in element.value for element in app.markdown)
	assert any("CC BY-SA 3.0" in element.value for element in app.markdown)
