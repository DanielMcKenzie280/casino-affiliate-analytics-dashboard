from app.analytics import calculate_metrics

def test_conversion_rate():
    data = {"clicks": 100, "signups": 10, "deposits": 5}
    result = calculate_metrics(data)
    
    assert result["conversion_rate"] == 0.1
