def calculate_average(grades):
    if not grades:
        return None
    return sum(grades) / len(grades)

# Fungsi pengujain menggunakan assert statement
def test_calculate_average():
    assert calculate_average([90, 80, 70]) == 80
    assert calculate_average([100, 100, 100]) == 100
    assert calculate_average([50, 75, 100]) == 75
    assert calculate_average([]) == None
    assert calculate_average([88]) == 88

test_calculate_average()