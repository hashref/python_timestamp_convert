import argparse
from datetime import datetime, timezone
import pytz


def main():
    parser = argparse.ArgumentParser(description="Converts UTC Timestamps")
    parser.add_argument(
        "-d",
        "--date",
        help="UTC Timestamp (DEFAULT: NOW)",
        type=lambda d: datetime.fromisoformat(d)
        .replace(tzinfo=timezone.utc)
        .isoformat(sep="T"),
        default=datetime.now(tz=timezone.utc).isoformat(sep="T"),
    )

    args = parser.parse_args()

    utc = datetime.fromisoformat(args.date)

    timezones = [
        "UTC",
        "America/Los_Angeles",
        "Asia/Taipei",
        "Asia/Hong_Kong",
        "Australia/Sydney",
    ]

    for tz in timezones:
        dt = utc.astimezone(pytz.timezone(tz)).strftime("%Y-%m-%dT%H:%M:%S %Z")
        print(f"{dt.ljust(24, ' ')} | {tz}")


if __name__ == "__main__":
    main()
