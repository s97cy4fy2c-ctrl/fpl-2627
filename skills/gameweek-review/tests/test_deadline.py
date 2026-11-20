import os, sys, datetime as dt
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import deadline

EV = [{"id": 10, "deadline_time": "2026-11-06T18:30:00Z"},
      {"id": 11, "deadline_time": "2026-11-21T11:00:00Z"},
      {"id": 19, "deadline_time": "2027-01-01T18:30:00Z"}]
NOW = dt.datetime(2026, 11, 20, 13, 0, tzinfo=dt.timezone.utc)


def test_next_deadline_is_the_first_one_after_now():
    gw, when, hours = deadline.next_deadline(EV, NOW)
    assert gw == 11 and when.hour == 11 and round(hours, 1) == 22.0


def test_set_one_chip_expiry_is_the_gw19_deadline_read_from_events():
    assert deadline.chip_expiry(EV).isoformat() == "2027-01-01T18:30:00+00:00"


def test_no_future_deadline_returns_none():
    assert deadline.next_deadline(EV, NOW + dt.timedelta(days=60)) is None
