import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import n1

# Real per-start series [live, 20 Nov 2026], minutes and xGI.
MBEUMO = [(90, .73), (90, 1.97), (90, .08), (90, .57), (90, .52),
          (90, .34), (90, .65), (90, .30), (90, .35), (82, .41)]
MCGINN = [(81, .05), (90, .10), (90, .71), (90, .11), (83, .04),
          (90, .94), (45, .02), (65, .21), (86, .89), (70, .97)]


def test_mbeumo_decline_is_one_outlier_so_variance():
    r = n1.n1(MBEUMO)
    assert round(r["change"], 2) == -0.40
    assert round(r["change_dropped"], 2) == -0.03
    assert r["verdict"] == "variance"


def test_falling_minutes_make_it_a_role_question_first():
    r = n1.n1(MCGINN)
    assert r["verdict"] == "role"


def test_steady_minutes_and_broad_rise_is_a_cause():
    s = [(90, .2)] * 4 + [(90, .5), (90, .6), (90, .5), (90, .6), (90, .5), (90, .6)]
    assert n1.n1(s)["verdict"] == "cause"


def test_too_few_starts_is_only_a_look():
    assert n1.n1([(90, .5)] * 9)["verdict"] == "look"   # 6 recent, 3 earlier
    assert n1.n1([(90, .5)] * 5)["verdict"] == "look"


def test_change_under_a_fifth_of_the_earlier_rate_is_variance_not_cause():
    # Live 20 Nov: Barry -0.06 on 0.86 read CAUSE because dropping his best recent
    # match enlarged the change. A shift that small is noise, whatever the drop does.
    s = [(90, .86)] * 4 + [(90, 1.5)] + [(90, .66)] * 5
    r = n1.n1(s)
    assert round(r["change"], 2) == -0.06
    assert r["verdict"] == "variance"


def test_flat_series_is_variance_even_with_float_noise():
    s = [(90, .3), (90, .1), (90, .2), (90, .2), (90, .1), (90, .3),
         (90, .2), (90, .2), (90, .2), (90, .2)]
    assert n1.n1(s)["verdict"] == "variance"
