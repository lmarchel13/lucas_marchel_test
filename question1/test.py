from main import overlapping

def test_overlapping():
    assert(overlapping((1,5),(3,4))) == True
    assert(overlapping((1,4),(3,5))) == True
    assert(overlapping((1,3),(3,4))) == True
    assert(overlapping((1,4),(3,4))) == True
    assert(overlapping((3,4),(1,4))) == True
    assert(overlapping((10,4),(1,6))) == True

    assert(overlapping((1,2),(3,4))) == False
    assert(overlapping((3,4),(1,2))) == False
    assert(overlapping((1,4),(5,10))) == False
    assert(overlapping((4,1),(5,10))) == False
    


if __name__ == "__main__":
    test_overlapping()
    print("Everything passed")
