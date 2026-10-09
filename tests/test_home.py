from pathlib import Path

from streamlit.testing.v1 import AppTest


APP_FILE = Path(__file__).resolve().parents[1] / "app.py"


def test_home_displays_noongar_map_with_attribution():
	app = AppTest.from_file(str(APP_FILE)).run()

	assert not app.exception
	assert any(header.value == "What does our app do?" for header in app.header)
	assert any(
		"All of our data was sourced from" in element.value
		and "https://www.bom.gov.au/" in element.value
		for element in app.markdown
	)
	assert len(app.get("image")) == 1
	assert any(header.value == "The Noongar People" for header in app.subheader)
	assert any(
		"the Perth Area being the Whadjuk group. The Noongar people follow a yearly "
		"calendar with six distinct seasons"
		in element.value
		for element in app.markdown
	)
	assert any("John D. Croft" in element.value for element in app.markdown)
	assert any("CC BY-SA 3.0" in element.value for element in app.markdown)
