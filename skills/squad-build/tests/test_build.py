import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import build


def test_full_season_thresholds_are_unchanged():
    assert build.thresholds(38) == {"mins": 1800, "starts": 24, "low_starts": 20}


def test_thresholds_scale_to_games_played_n22():
    # n=22: the 1800-min / 24-start rule made every player 'not nailed' mid-season.
    assert build.thresholds(10) == {"mins": 474, "starts": 7, "low_starts": 6}


def test_no_games_played_means_prior_season_data_so_full_thresholds():
    assert build.thresholds(0) == build.thresholds(38)


def _row(name, club, pos, pts, cost=40):
    return dict(name=name, club=club, pos=pos, cost=cost, pts=pts, nailed=True,
                starts=30, transferable=True)


def test_solver_may_start_same_club_gk_and_def_r5():
    # R5, 20 Nov 2026: a same-club GK+DEF pair is a scorecard axis, not a cap.
    rows = [_row("GK1", "BHA", "GKP", 200), _row("D1", "BHA", "DEF", 200)]
    clubs = ["C%d" % i for i in range(20)]
    rows += [_row("GK%d" % i, clubs[i], "GKP", 10) for i in range(2, 4)]
    rows += [_row("D%d" % i, clubs[i], "DEF", 10) for i in range(2, 8)]
    rows += [_row("M%d" % i, clubs[i], "MID", 10) for i in range(2, 9)]
    rows += [_row("F%d" % i, clubs[i], "FWD", 10) for i in range(2, 6)]
    squad, xi = build.solve(rows, 12, False, set(), 3, 1000)
    names = {rows[i]["name"] for i in xi}
    assert {"GK1", "D1"} <= names


def test_transferability_is_off_by_default_r4():
    assert build.parser().parse_args([]).thesis == "off"
