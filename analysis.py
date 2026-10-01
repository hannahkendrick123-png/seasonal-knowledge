def filter_by_season(df, season):
    """Return only the records for one season."""
    if "season" not in df.columns:
        raise ValueError("The data must contain a season column.")

    return df[df["season"] == season].copy()


def calculate_season_statistics(df, season):
    """Calculate statistics for one season."""
    selected = filter_by_season(df, season)
    if selected.empty:
        raise ValueError(f"No data found for {season}.")

    return {
        "average_max_temp": selected["max_temp"].mean(),
        "average_min_temp": selected["min_temp"].mean(),
        "total_rainfall": selected["rainfall"].sum(),
        "rainy_days": (selected["rainfall"] > 0).sum(),
    }


def seasonal_summary(df):
    """Calculate statistics for all seasons."""
    return (
        df.groupby("season")
        .agg(
            average_max_temp=("max_temp", "mean"),
            average_min_temp=("min_temp", "mean"),
            total_rainfall=("rainfall", "sum"),
            average_rainfall=("rainfall", "mean"),
            rainy_days=("rainfall", lambda values: (values > 0).sum()),
        )
        .reset_index()
    )