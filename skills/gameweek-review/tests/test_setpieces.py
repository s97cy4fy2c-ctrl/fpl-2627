import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import setpieces

TEAMS = {1: "ARS", 2: "AVL"}


def el(i, name, team, pen=None, cor=None, dfk=None):
    return {"id": i, "web_name": name, "team": team, "penalties_order": pen,
            "corners_and_indirect_freekicks_order": cor, "direct_freekicks_order": dfk}


def test_snapshot_keeps_only_players_with_a_set_piece_role():
    rows = setpieces.snapshot([el(1, "A", 1, pen=1), el(2, "B", 1)], TEAMS)
    assert [r["web_name"] for r in rows] == ["A"]
    assert rows[0]["club"] == "ARS" and rows[0]["pen"] == "1"


def test_diff_reports_a_new_first_choice_penalty_taker():
    old = setpieces.snapshot([el(1, "A", 1, pen=1), el(2, "B", 1, pen=2)], TEAMS)
    new = setpieces.snapshot([el(1, "A", 1, pen=2), el(2, "B", 1, pen=1)], TEAMS)
    ch = setpieces.diff(old, new)
    assert any("B" in c and "pen 2 -> 1" in c for c in ch)
    assert any("A" in c and "pen 1 -> 2" in c for c in ch)


def test_diff_reports_lost_role_and_no_change():
    old = setpieces.snapshot([el(1, "A", 2, cor=1)], TEAMS)
    assert setpieces.diff(old, old) == []
    gone = setpieces.diff(old, setpieces.snapshot([el(1, "A", 2)], TEAMS))
    assert gone and "cor 1 -> -" in gone[0]
