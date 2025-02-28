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

    # when we calculate the volume
    output = methods.volume_of_parallelepiped(length, width, height)
    
    # then the volume should be 30
    assert output == 30

def teste_soma():
    # given a value 'a' of 5 and 'b' of 7
    a = 5
    b = 7

    # when we calculate the adding of the values
    output = methods.soma(a, b)

    # then the sum should be 12
    assert output == 12

def teste_subtracao():
    # given a value 'a' of 15 and 'b' of 8
    a = 15
    b = 8

    # when we calculate the subtraction of the values
    output = methods.subtracao(a, b)

    # then the subtraction should be 7
    assert output == 7

def teste_multiplicacao():
    # given a value 'a' of 5 and 'b' of 4
    a = 5
    b = 4

    # when we calculate the multiplying of the values
    output = methods.multiplicacao(a, b)

    # then the multiplying should be 20
    assert output == 20

def teste_divisao():
    # given a value 'a' of 20 and 'b' of 4
    a = 20
    b = 4

    # when we calculate the division of the values
    output = methods.divisao(a, b)

    # then the division should be 20
    assert output == 5