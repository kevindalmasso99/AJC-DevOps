from main import count_char, check_if_maj, check_if_special, check_if_valid_password

def test_count_char():
    input1 = "Bonjour"
    input2 = ""
    input3 = "Pa*Ss!Wo-rd"

    expected1 = 7
    expected2 = 0
    expected3 = 11

    result1 = count_char(input1)
    result2 = count_char(input2)
    result3 = count_char(input3)

    assert expected1 == result1
    assert expected2 == result2
    assert expected3 == result3

def test_check_if_maj():
    input1 = "Bonjour"
    input2 = ""
    input3 = "Pa*Ss!Wo-rd"
    input4 = "minuscule"
    input5 = "bonjouR"
    input6 = "pa*ss!wo-rd"

    expected1 = True
    expected2 = False
    expected3 = True
    expected4 = False
    expected5 = True
    expected6 = False

    result1 = check_if_maj(input1)
    result2 = check_if_maj(input2)
    result3 = check_if_maj(input3)
    result4 = check_if_maj(input4)
    result5 = check_if_maj(input5)
    result6 = check_if_maj(input6)

    assert expected1 == result1
    assert expected2 == result2
    assert expected3 == result3
    assert expected4 == result4
    assert expected5 == result5
    assert expected6 == result6

def test_check_if_special():
    input1 = "Bonjour"
    input2 = ""
    input3 = "Pa*Ss!Wo-rd"
    input4 = "pas&swor$d"

    expected1 = False
    expected2 = False
    expected3 = True
    expected4 = False

    result1 = check_if_special(input1)
    result2 = check_if_special(input2)
    result3 = check_if_special(input3)
    result4 = check_if_special(input4)

    assert expected1 == result1
    assert expected2 == result2
    assert expected3 == result3
    assert expected4 == result4

def test_check_if_valid_password():
    input1 = "Pa*Ss!Wo-rd"
    input2 = "Pa*S-s!"
    input3 = "pa*ss!wo-rd"
    input4 = "Pas&SW_or$d"
    input5 = ""

    expected1 = True
    expected2 = False
    expected3 = False
    expected4 = False
    expected5 = False

    result1 = check_if_valid_password(input1)
    result2 = check_if_valid_password(input2)
    result3 = check_if_valid_password(input3)
    result4 = check_if_valid_password(input4)
    result5 = check_if_valid_password(input5)

    assert expected1 == result1
    assert expected2 == result2
    assert expected3 == result3
    assert expected4 == result4
    assert expected5 == result5