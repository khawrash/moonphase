from calc_time.calc_time import calc_time_return_dict

def test_it_should_return_tz_name_of_Tokyo():
    dt = calc_time_return_dict('Asia/Tokyo')
    assert 'JST' == dt.tzname()
