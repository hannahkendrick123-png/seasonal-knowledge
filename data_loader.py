from pathlib import Path

import pandas as pd


BASE_FOLDER = Path(__file__).resolve().parent
WEATHER_FILE = BASE_FOLDER / "data" / "weather.csv"
SEASON_FILE = BASE_FOLDER / "data" / "season_info.csv"


def load_weather_data():
	"""Load and clean the weather CSV file."""
	if not WEATHER_FILE.exists():
		raise FileNotFoundError("weather.csv was not found in the data folder.")

	df = pd.read_csv(WEATHER_FILE)
	required_columns = {"date", "min_temp", "max_temp", "rainfall"}
	missing_columns = required_columns - set(df.columns)
	if missing_columns:
		raise ValueError("Missing columns: " + ", ".join(sorted(missing_columns)))

	df["date"] = pd.to_datetime(df["date"], errors="coerce")
	for column in ("min_temp", "max_temp", "rainfall"):
		df[column] = pd.to_numeric(df[column], errors="coerce")

	df = df.dropna(subset=["date", "min_temp", "max_temp", "rainfall"])
	df = df.drop_duplicates(subset=["date"])

	if (df["rainfall"] < 0).any():
		raise ValueError("Rainfall cannot be negative.")
	if (df["max_temp"] < df["min_temp"]).any():
		raise ValueError(
			"Maximum temperature cannot be lower than minimum temperature."
		)
	if len(df) < 200:
		raise ValueError(
			f"Only {len(df)} records were found. "
			"At least 200 records are required."
		)

	return df.sort_values("date").reset_index(drop=True)


def load_season_info():
	"""Load the seasonal information CSV."""
	if not SEASON_FILE.exists():
		raise FileNotFoundError(
			"season_info.csv was not found in the data folder."
		)

	df = pd.read_csv(SEASON_FILE)
	required_columns = {"season", "period", "environmental_signs", "source"}
	missing_columns = required_columns - set(df.columns)
	if missing_columns:
		raise ValueError("Missing columns: " + ", ".join(sorted(missing_columns)))

	return df
