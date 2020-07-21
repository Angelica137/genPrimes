from scripts.genPrimes import genPrimes

def test_next_method_genPrimes():
    g = genPrimes()
    assert g.next() == 2
    assert g.next() == 3
    assert g.next() == 5