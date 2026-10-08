import pandas as pd
import pytest

from season_logic import add_seasons, get_season


def test_january_is_birak():
	assert get_season(1) == "Birak"


def test_december_is_birak():
	assert get_season(12) == "Birak"


def test_february_is_bunuru():
	assert get_season(2) == "Bunuru"


def test_april_is_djeran():
	assert get_season(4) == "Djeran"


def test_june_is_makuru():
	assert get_season(6) == "Makuru"


def test_august_is_djilba():
	assert get_season(8) == "Djilba"


def test_october_is_kambarang():
	assert get_season(10) == "Kambarang"


def test_zero_is_invalid():
	with pytest.raises(ValueError):
		get_season(0)


def test_thirteen_is_invalid():
	with pytest.raises(ValueError):
		get_season(13)


def test_add_seasons():
	data = pd.DataFrame(
		{
			"date": pd.to_datetime(
				["2025-01-01", "2025-06-01", "2025-10-01"]
			)
		}
	)
	result = add_seasons(data)

	assert list(result["season"]) == ["Birak", "Makuru", "Kambarang"]
