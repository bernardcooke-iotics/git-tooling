from datetime import datetime


def today() -> None:
    print("Today is:", datetime.utcnow().strftime("%Y-%m-%d"))
