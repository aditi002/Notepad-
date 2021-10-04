import pytest
Ent1 = 'Admin'
Ent2 = '123'
@pytest.fixturedef fun():x = 'Linus'    y = 'hello'    return [x, y]def test_1(fun):a = 'hello'    b = 'jello'    assert fun[0] == aassert fun[1] == bdef test_2(fun):a= 'Linus'    b= 'hello'    assert fun[0] == a and fun[1] == bdef test_3(fun):a= 'Linu'    b= 'hell'    assert fun[0] == a and fun[1] == b@pytest.mark.parametrize("Name,Pass,Val1,Val2",[('Admin','123','Admin','123'),