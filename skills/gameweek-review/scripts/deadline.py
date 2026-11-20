#!/usr/bin/env python3
"""Print the next deadline and the set-one chip expiry, live (ruled 20 Nov 2026, R1).

Dates are data. No doc types a deadline. Process error n=27: the GW10 deadline
was missed on a wrong calendar date. n=28: the GW19 expiry was wrong in five
places. Run this first, every session, in the Composio sandbox.

Usage:  python3 deadline.py
"""
import datetime as dt, json, urllib.request

API = "https://fantasy.premierleague.com/api/bootstrap-static/"
SET_ONE_LAST_GW = 19  # first chip set expires at this GW's deadline (doctrine s4)


def _t(s):
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))


def next_deadline(events, now):
    for e in sorted(events, key=lambda e: _t(e["deadline_time"])):
        when = _t(e["deadline_time"])
        if when > now:
            return e["id"], when, (when - now).total_seconds() / 3600
    return None


def chip_expiry(events):
    return next(_t(e["deadline_time"]) for e in events if e["id"] == SET_ONE_LAST_GW)


def main():
    bs = json.loads(urllib.request.urlopen(urllib.request.Request(
        API, headers={"User-Agent": "Mozilla/5.0"}), timeout=60).read())
    now = dt.datetime.now(dt.timezone.utc)
    nd = next_deadline(bs["events"], now)
    if nd:
        gw, when, h = nd
        print(f"[live] next deadline: GW{gw} {when:%a %d %b %Y %H:%M} UTC - {h:.1f} hours left")
    else:
        print("[live] no future deadline in events")
    exp = chip_expiry(bs["events"])
    print(f"[live] set-one chips expire: GW{SET_ONE_LAST_GW} deadline {exp:%a %d %b %Y %H:%M} UTC "
          f"- {(exp - now).days} days left")


if __name__ == "__main__":
    main()
