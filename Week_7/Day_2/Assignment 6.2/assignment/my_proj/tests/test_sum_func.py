from my_proj.sum_func import add, add_positive

# Testing add function on positive integers
def test_add_2_2_returns_4():
    assert add(2, 2) == 4

# Testing add function on zeros
def test_add_0_0_returns_0():
    assert add(0, 0) == 0

# Testing add function on negative integers
def test_add_negative_nums_4_2_returns_0():
    assert add(-4, -2) == -6

# Testing add function on one positive and one negative integer
def test_add_negative_and_positive_nums_4_2_returns_0():
    assert add(-4, 2) == -2


# Testing add positive function on positive integers
def test_add_positive_2_2_returns_4():
    assert add_positive(2, 2) == 4

# Testing add function on one zeros  (>0)
def test_add_positive_0_0_returns_none():
    assert add_positive(0, 0) == None


# Testing add postive function on negative integers
def test_add_positive_negative_nums_1_2_returns_None():
    assert add_positive(-1, -2) == None

# Testing add postive function on postive (a) negative (b > 0) integers
def test_add_positive_postivie_negative_nums_1_2_returns_None():
    assert add_positive(1, -2) == None

# Testing add postive function on negative (a > 0) positvive (b) integers
def test_add_positive_negative_positive_nums_1_2_returns_None():
    assert add_positive(-1, 2) == None

