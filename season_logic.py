def get_season(month):
	"""Assign a month to a seasonal category."""
	if month in (12, 1):
		return "Birak"
	elif month in (2, 3):
		return "Bunuru"
	elif month in (4, 5):
		return "Djeran"
	elif month in (6, 7):
		return "Makuru"
	elif month in (8, 9):
		return "Djilba"
	elif month in (10, 11):
		return "Kambarang"
	raise ValueError("Month must be between 1 and 12.")


def add_seasons(df):
	"""Add a season column using the date column."""
	if "date" not in df.columns:
		raise ValueError("The data must contain a date column.")

	result = df.copy()
	result["season"] = result["date"].dt.month.apply(get_season)
	return result
