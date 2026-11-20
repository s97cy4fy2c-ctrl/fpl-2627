import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import collisions


def pair(cls, gw=11, xi=True):
    return {"cls": cls, "gw": gw, "xi": xi}


def test_two_class_a_pairs_in_xi_warn_and_do_not_fail():
    # Ruled 20 Nov 2026 (R7): class A is a hedge, not a dead slot. Warn, never fail.
    msgs, code = collisions.verdict([pair("A"), pair("A")], 11)
    assert code == 0
    assert any("class A" in m for m in msgs)


def test_class_a_pairs_on_bench_or_other_gw_are_not_counted():
    msgs, code = collisions.verdict([pair("A", xi=False), pair("A", gw=12)], 11)
    assert code == 0
    assert "0 of them class A" in msgs[0]
