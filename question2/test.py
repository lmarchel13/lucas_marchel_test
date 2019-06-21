from main import compare

def test_compare():
    assert(compare('1.2','1.1')) == 1
    assert(compare('1.1.1','1.1')) == 1
    assert(compare('1.0.1','1')) == 1
    assert(compare('1.1','1')) == 1
    assert(compare('1','')) == 1
    
    assert(compare('1.1','1.2')) == -1
    assert(compare('1.1','1.1.1')) == -1
    assert(compare('1','1.0.1')) == -1
    assert(compare('1','1.1')) == -1
    assert(compare('','1.1')) == -1

    assert(compare('','')) == 0
    assert(compare('1','1')) == 0
    assert(compare('1.1','1.1')) == 0
    assert(compare('1.2.3.4.5','1.2.3.4.5')) == 0

if __name__ == "__main__":
    test_compare()
    print("Everything passed")
