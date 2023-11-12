
import pytest

from src.convert_data import transform_data

examples = [
    'Run\tMon, 10/30/2023\tAfternoon Run\t18:57\t4.01 km',
    'Run\tSun, 10/22/2023\teasy jog\t23:43\t4.50 km',
    'Ride\tWed, 9/27/2023\tAfternoon Ride\t23:00\t6.85 km',
]


@pytest.mark.parametrize("example, expected_result", [
    (examples[0], ("Oct 30, 2023, 00:00:00 PM", "Run", "18:57", "4.01")),
    (examples[1], ("Oct 22, 2023, 00:00:00 PM", "Run", "23:43", "4.50")),
    (examples[2], ("Sep 27, 2023, 00:00:00 PM", "Ride", "23:00", "6.85")),
])
def test_transform_data(example, expected_result):
    result = transform_data(example)
    assert result == expected_result
