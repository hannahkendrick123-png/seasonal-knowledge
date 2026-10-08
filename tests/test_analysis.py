import pandas as pd
import pytest

from analysis import (
    calculate_season_statistics,
    filter_by_season,
    seasonal_summary,
)


def make_test_data():
    return pd.DataFrame(
        {
            "date": pd.to_datetime(
                ["2025-01-01", "2025-01-02", "2025-06-01", "2025-06-02"]
            ),
            "min_temp": [20, 21, 10, 11],
            "max_temp": [30, 31, 20, 21],
            "rainfall": [0, 5, 10, 0],
            "season": ["Birak", "Birak", "Makuru", "Makuru"],
        }
    )


def test_filter_by_season():
    result = filter_by_season(make_test_data(), "Birak")
    assert len(result) == 2


def test_average_maximum_temperature():
    result = calculate_season_statistics(make_test_data(), "Birak")
    assert result["average_max_temp"] == 30.5


def test_average_minimum_temperature():
    result = calculate_season_statistics(make_test_data(), "Birak")
    assert result["average_min_temp"] == 20.5


def test_total_rainfall():
    result = calculate_season_statistics(make_test_data(), "Birak")
    assert result["total_rainfall"] == 5


def test_rainy_days():
    result = calculate_season_statistics(make_test_data(), "Birak")
    assert result["rainy_days"] == 1


def test_empty_season():
    with pytest.raises(ValueError):
        calculate_season_statistics(make_test_data(), "Djilba")


def test_summary_contains_birak():
    result = seasonal_summary(make_test_data())
    assert "Birak" in result["season"].values