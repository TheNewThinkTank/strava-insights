
from src.convert_data import transform_data

examples = [
    'Run	Mon, 10/30/2023	Afternoon Run	18:57	4.01 km',
    'Run	Sun, 10/22/2023	easy jog	23:43	4.50 km',
    'Ride	Wed, 9/27/2023	Afternoon Ride	23:00	6.85 km',
    ]


def test_transform_data():
    # TODO: parameterize and add all examples
    example = examples[0]

    activity_date = "Oct 30, 2023, 00:00:00 PM"
    activity_type = "Run"
    elapsed_time = "18:57"
    distance = "4.01"

    result = transform_data(example)

    assert result[0] == activity_date
    assert result[1] == activity_type
    assert result[2] == elapsed_time
    assert result[3] == distance

