import pytest
from eta import eta_hours

def test_regular_delivery_standard_distance():
    assert eta_hours(250, False) == 26.0

def test_regular_delivery_zero_distance_boundary():
    assert eta_hours(0, False) == 24.0

def test_express_delivery_half_time():
    assert eta_hours(250, True) == 13.0

def test_negative_distance_raises_value_error():
    with pytest.raises(ValueError, match="Відстань не може бути від'ємною"):
        eta_hours(-10.0)

def test_express_delivery_minimum_limit():
    assert eta_hours(0, True) == 12.0