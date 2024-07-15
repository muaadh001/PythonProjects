from project import fetch_weather_data, process_weather_data, display_weather_summary

def test_fetch_weather_data():
    location = "Test Location"
    start_date = "2023-06-01"
    end_date = "2023-06-05"
    data = fetch_weather_data(location, start_date, end_date)
    assert len(data) == 5
    assert all(isinstance(day["temp"], (int, float)) for day in data)

def test_process_weather_data():
    data = [
        {"date": "2023-06-01", "temp": 20},
        {"date": "2023-06-02", "temp": 22},
        {"date": "2023-06-03", "temp": 21},
        {"date": "2023-06-04", "temp": 23},
        {"date": "2023-06-05", "temp": 19}
    ]
    summary = process_weather_data(data)
    assert summary["average"] == 21.0
    assert summary["highest"] == 23
    assert summary["lowest"] == 19

def test_display_weather_summary(capsys):
    location = "Test Location"
    start_date = "2023-06-01"
    end_date = "2023-06-05"
    summary = {"average": 21.0, "highest": 23, "lowest": 19}

    display_weather_summary(location, start_date, end_date, summary)
    captured = capsys.readouterr()
    assert "Weather summary for Test Location from 2023-06-01 to 2023-06-05:" in captured.out
    assert "Average Temperature: 21.0°C" in captured.out
    assert "Highest Temperature: 23°C" in captured.out
    assert "Lowest Temperature: 19°C" in captured.out
