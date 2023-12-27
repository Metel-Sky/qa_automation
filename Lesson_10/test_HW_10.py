import pytest



@pytest.mark.new
def test_1():
    assert True


@pytest.mark.old
def test_2():
    assert True


@pytest.mark.main
def test_3():
    assert True


@pytest.mark.new
def test_4():
    assert True


@pytest.mark.old
def test_5():
    assert True


@pytest.mark.new
def test_6():
    assert True


@pytest.mark.main
def test_7():
    assert True


@pytest.mark.old
def test_8():
    assert True


@pytest.mark.main
@pytest.mark.old
def test_9():
    assert True


@pytest.mark.old
def test_10():
    assert True
