import pandas as pd

from data_loader import load_season_info, load_weather_data


def test_weather_data_is_dataframe():
	data = load_weather_data()
	assert isinstance(data, pd.DataFrame)


def test_weather_data_has_200_records():
	data = load_weather_data()
	assert len(data) >= 200


def test_weather_columns_exist():
	data = load_weather_data()
	required_columns = {"date", "min_temp", "max_temp", "rainfall"}
	assert required_columns.issubset(data.columns)


def test_dates_are_datetime():
	data = load_weather_data()
	assert pd.api.types.is_datetime64_any_dtype(data["date"])


def test_rainfall_is_positive_or_zero():
	data = load_weather_data()
	assert (data["rainfall"] >= 0).all()


def test_season_info_loads():
	data = load_season_info()
	assert len(data) == 6


def test_season_info_columns():
	data = load_season_info()
	required_columns = {"season", "period", "environmental_signs", "source"}
	assert required_columns.issubset(data.columns)
