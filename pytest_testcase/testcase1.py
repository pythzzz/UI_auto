import pytest

@pytest.fixture(params=[1,2,3])
def data(request):
    return request.param

def testcase1(login):
    a=1
    print('用例1执行')
    assert a==1

@pytest.mark.smoking
def testcase2():
    b=1
    print(b)
    assert b+1==2

def testcase3(data):
    print(f'数据为{data}')
    assert data<5
