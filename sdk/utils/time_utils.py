"""
Time parsing and sleep utilities.
"""
import datetime
import email.utils

def parse_http_date(header: str) -> datetime.datetime:
    """Parse HTTP-date into datetime."""
    return datetime.datetime(*email.utils.parsedate(header)[:6])

def sleep_until(timestamp: float):
    """Sleep until the given POSIX timestamp."""
    now = datetime.datetime.now().timestamp()
    delta = timestamp - now
    if delta > 0:
        time.sleep(delta)
