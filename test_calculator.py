from calculator import add, subtract, multiply, divide, CircleArea

def test_add():
	assert add(2, 3) == 5

def test_divide():
	assert divide(6, 2) == 3

def test_subtract():
	assert subtract(5, 3) == 2

def test_multiply():
	assert multiply(4, 3) == 12

def test_divide_uneven():
        # Arrange
        a, b = 9, 2
        # Act
        result = divide(a, b)
        # Assert
        assert result == 4.5

def test_multiply_uneven():
        # Arrange
        a, b = 7, 0
        # Act
        result = multiply(a, b)
        #Assert
        assert result == 0

def test_CircleArea():
	assert CircleArea(-4) == "Error"
