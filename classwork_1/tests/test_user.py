from classwork_1.src.user import User
import pytest

@pytest.mark.user
@pytest.mark.parametrize('name, age, expected_result',
                         [
                             ('Иван', 20, User('Иван', 20)),
                             ('Федор', 30, User('Федор', 30)),
                             ('Дмитрий', 33, User('Дмитрий', 33)),
                             ('Иванфедордмитрийкириллантонолег', 20, User('Иванфедордмитрийкириллантонолег', 20)),
                             ('Антон', 1, User('Антон', 1)),
                             ('Олег', 100, User('Олег', 100)),
                             ('Игорь', 110, User('Игорь', 110)),
                             ('Мария', 48, User('Мария', 48)),
                             ('Эдуард', 50, User('Эдуард', 50)),
                             ('John', 33, User('John', 33)),
                             ('Jack', 10, User('Jack', 10)),
                             ('Антон', 90, User('Антон', 90)),
                             ('Жанна', 110, User('Жанна', 110)),
                             ('Peter', 15, User('Peter', 15))
                         ])

def test_init_positive(name, age, expected_result):
    user = User(name, age)

    assert user.get_age() == expected_result.get_age() and user.get_name() == expected_result.get_name()

@pytest.mark.user
@pytest.mark.parametrize('name, age, expected_result',
                         [
                             ('Иван', '20', pytest.raises(TypeError)),
                             (True, 20, pytest.raises(TypeError)),
                             (None, '20', pytest.raises(TypeError)),
                             (None, 20, pytest.raises(TypeError)),
                             ('Иван', -20, pytest.raises(ValueError)),
                             ('Иван', None, pytest.raises(TypeError)),
                             ('Иван', 1000, pytest.raises(ValueError)),
                             (None, None, pytest.raises(TypeError)),
                             (None, -20, pytest.raises(TypeError))
                         ])

def test_init_negative(name, age, expected_result):

    with expected_result:
        User(name, age) == expected_result

@pytest.mark.user
@pytest.mark.parametrize('user, expected_result',
                         [
                             (User('Иван', 20), 'Иван'),
                             (User('John', 20), 'John'),
                             (User('Олег', 20), 'Олег')
                         ])

def test_get_name_positive(user, expected_result):

    assert user.get_name() == expected_result

@pytest.mark.user
@pytest.mark.parametrize('user, expected_result',
                         [
                             (User('Иван', 90), 90),
                             (User('John', 110), 110),
                             (User('Олег', 48), 48)
                         ])

def test_get_name_positive(user, expected_result):

    assert user.get_age() == expected_result

@pytest.mark.user
@pytest.mark.parametrize('user, expected_result',
                         [
                             (User('Иван', 90), 90),
                             (User('John', 110), 110),
                             (User('Олег', 48), 48)
                         ])

def test_get_name_positive(user, expected_result):

    assert user.get_age() == expected_result


@pytest.mark.user
@pytest.mark.parametrize('name, age, expected_result',
                         [
                             ('Иван', 90, 91)
                         ])
def test_get_name_positive(name, age, expected_result):
    user = User(name, age)

    user.up_age()
    assert user.get_age() == expected_result
