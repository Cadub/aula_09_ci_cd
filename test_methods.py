import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_volume():
    # given a lenght of 3, a width of 2 and a height of 5
    length = 3
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.volume_of_parallelepiped(length, width, height)
    
    # then the perimeter should be 30
    assert output == 30