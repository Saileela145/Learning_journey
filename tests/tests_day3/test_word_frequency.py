from programs.day3.word_frequency import word_frequency

def test_word_frequency():
    assert word_frequency("hi hi hello") == {"hi": 2, "hello": 1}
    assert word_frequency("apple banana apple") == {"apple": 2, "banana": 1}
    assert word_frequency("") == {}
