from datetime import date, timedelta
import calendar
import re
from dateutil.relativedelta import relativedelta


def day(date_str: str) -> int | None:
    if not is_date(date_str):
        raise TypeError("Invalid date")

    pattern = r'^\d{4}-\d{2}-(\d{2})$'
    if match := re.search(pattern, date_str):
        return int(match.group(1))
    return None

def month(date_str: str) -> int | None:
    if not is_date(date_str):
        raise TypeError("Invalid date")

    pattern = r'^\d{4}-(\d{2})-\d{2}$'
    if match := re.search(pattern, date_str):
        return int(match.group(1))
    return None

def year(date_str: str) -> int | None:
    if not is_date(date_str):
        raise TypeError("Invalid date")

    pattern = r'^(\d{4})'
    if match := re.search(pattern, date_str):
        return int(match.group(1))
    return None

def week(date_str: str) -> int:
    if not is_date(date_str):
        raise TypeError("Invalid date")

    dt = date(
        year=int(year(date_str)),
        month=int(month(date_str)),
        day=int(day(date_str))
    )
    return dt.isocalendar()[1]

def week_day(date_str: str) -> int:
    if not is_date(date_str):
        raise TypeError("Invalid date")
    dt = date(
        year=int(year(date_str)),
        month=int(month(date_str)),
        day=int(day(date_str))
    )
    return dt.weekday()

def quarter(date_str: str) -> int:
    if not is_date(date_str):
        raise TypeError("Invalid date")
    return (month(date_str) - 1) // 3 + 1

def day_of_week(date_str: str) -> str:
    if not is_date(date_str):
        raise TypeError("Invalid date")
    dt = date(
        year=int(year(date_str)),
        month=int(month(date_str)),
        day=int(day(date_str))
    )
    return dt.strftime("%A")

def day_of_year(date_str: str) -> int:
    if not is_date(date_str):
        raise TypeError("Invalid date")
    dt = date(
        year=int(year(date_str)),
        month=int(month(date_str)),
        day=int(day(date_str))
    )
    return int(dt.strftime("%j"))

def is_date(date_str: str) -> bool:
    pattern = r'^\d{4}-?(?:\d{2})?-?(?:\d{2})?$'
    if not re.fullmatch(pattern, date_str):
        return False
    parts = date_str.split('-')

    # Year check
    yy: int = int(parts[0])
    if not (1900 <= yy <= 2100):
        return False

    if len(parts) > 1:
        # Month check
        mm: int = int(parts[1])
        if not (1 <= mm <= 12):
            return False

        if len(parts) > 2:
            # Day check
            dd: int = int(parts[2])

            days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if mm == 2 and (yy % 4 == 0 and (yy % 100 != 0 or yy % 400 == 0)):
                max_day = 29  # Leap year
            else:
                max_day = days_in_month[mm - 1]

            if not (1 <= dd <= max_day):
                return False
    return True

def date_part(date_str: str, part: str = 'year') -> int:
    if not is_date(date_str):
        raise TypeError("Invalid date")

    mapping = {
        'day': day(date_str),
        'month': month(date_str),
        'year': year(date_str),
        'week': week(date_str),
        'week_day': week_day(date_str),
        'quarter': quarter(date_str)
    }

    try:
        return mapping[part]
    except KeyError:
        raise TypeError(
            "Invalid argument for date_part, part: expects ['day', 'month', 'year', 'week', 'week_day', 'quarter']")

def date_name(date_str: str, part: str = 'month') -> str:
    """
        Returns a string representation of a specific part of a date.

        Args:
            date_str: A string representing a date.
            part: One of ['day', 'day_of_week', 'month', 'year'].

        Returns:
            str: The requested part of the date.

        Raises:
            TypeError: If the date is invalid or the part is unknown.
    """

    if not is_date(date_str):
        raise TypeError('Invalid date format')

    dt = date(
        year=int(year(date_str)),
        month=int(month(date_str)),
        day=int(day(date_str))
    )

    mapping = {
        'day': f"{day(date_str):02}",
        'day_of_week': dt.strftime("%A"),
        'month': f"{dt.strftime("%B"):02}",
        'year': dt.strftime("%Y")
    }

    try:
        return mapping[part]
    except KeyError:
        raise TypeError("Invalid argument for date_name, part: expects ['day', 'month', 'year', 'day_of_week']")

def date_trunc(date_str: str, arg: str = 'year') -> str:
    """
        Truncate a date string to the start of the day, month, or year.

        Args:
            date_str: A string representing a date.
            arg: One of ['day', 'month', 'year'].

        Returns:
            str: The truncated date string.

        Raises:
            TypeError: If `arg` is not 'day', 'month', or 'year'.
    """

    if not arg in ['day', 'month', 'year']:
        raise TypeError("Invalid argument for date_trunc, arg: expects ['day', 'month', 'year']")

    # If invalid date, raise TypeError
    if not is_date(date_str):
        raise TypeError("Invalid date format")

    pattern = r'^(\d{4})-(\d{2})-(\d{2})$'
    match = re.fullmatch(pattern, date_str)

    if match:
        dt = date(
            year=int(year(date_str)),
            month=int(month(date_str)),
            day=int(day(date_str))
        )

        mapping = {
            'year': f"{dt.year}-01-01",
            'month': f"{dt.year}-{dt.month:02}-01",
            'day': f"{dt.year}-{dt.month:02}-{dt.day:02}"
        }

        try:
            return mapping[arg]
        except KeyError:
            raise TypeError("Invalid argument for date_trunc, arg: expects ['year', 'month', 'day']")
    return f"{date_str}-01-01"

def end_of_month(date_str: str) -> str:
    """
    Returns the last day of the month for a given date string.

    Args:
        date_str: A string representing a date.

    Returns:
        str: Date string for the last day of the month in YYYY-MM-DD format.

    Raises:
        TypeError: If the date format is invalid.
    """

    if not is_date(date_str):
        raise TypeError("Invalid date format")

    yy = int(year(date_str))
    mm = int(month(date_str))

    # Use calendar module to get number of days in month
    last_day = calendar.monthrange(yy, mm)[1]

    return f"{yy}-{mm:02}-{last_day:02}"

def start_of_month(date_str: str) -> str:
    """
    Returns the first day of the month for a given date string.

    Args:
        date_str: A string representing a date.

    Returns:
        str: Date string in YYYY-MM-DD format.

    Raises:
        TypeError: If the date format is invalid.
    """

    if not is_date(date_str):
        raise TypeError("Invalid date format")

    # Delegate to date_trunc for month
    return date_trunc(date_str, "month")

def date_format(date_str: str, d_format: str = 'dd') -> str | TypeError:
    if not is_date(date_str):
        raise TypeError("Invalid date format")

    mapping = {
        'dd': date_name(date_str, 'day'),
        'ddd': (date_name(date_str, 'day_of_week'))[:3],
        'dddd': date_name(date_str, 'day_of_week'),
        'mm': str(month(date_str)),
        'mmm': (date_name(date_str, 'month'))[:3],
        'mmmm': date_name(date_str, 'month'),
        'yy': (date_name(date_str, 'year'))[-2:],
        'yyyy': date_name(date_str, 'year'),
        'dd-mmm': f"{date_part(date_str, 'day'):02} {(date_name(date_str, 'month'))[:3]}",
        'dd-mmmm': f"{date_part(date_str, 'day'):02} {date_name(date_str, 'month')}",
        'mmm-yy': f"{(date_name(date_str, 'month'))[:3]} {(date_name(date_str, 'year'))[-2:]}",
        'mmm-yyyy': f"{(date_name(date_str, 'month'))[:3]} {date_name(date_str, 'year')}",
        'mmmm-yyyy': f"{date_name(date_str, 'month')} {date_name(date_str, 'year')}",
        'yyyy-mm-dd': date_str,
        'dd-mm-yyyy': f"{date_part(date_str, 'day'):02}-{date_part(date_str, 'month'):02}-{date_part(date_str, 'year')}",
        'dd-mmm-yyyy': f"{date_part(date_str, 'day'):02} {(date_name(date_str, 'month'))[:3]}, {date_part(date_str, 'year')}",
        'dd-mmmm-yyyy': f"{date_part(date_str, 'day'):02} {date_name(date_str, 'month')}, {date_part(date_str, 'year')}",
        'dd-mm-yy': f"{date_part(date_str, 'day'):02}-{date_part(date_str, 'month'):02}-{(date_name(date_str, 'year'))[-2:]}"
    }

    try:
        return mapping[d_format]
    except KeyError:
        raise TypeError("Invalid Key for d_format")

def date_add(date_str: str, interval=0, unit: str='days') -> str | TypeError:
    if not is_date(date_str):
        raise TypeError("Invalid date")

    pattern = r'^(\d{4})-(\d{2})-(\d{2})$'
    match = re.fullmatch(pattern, date_str)

    if match:
        dt = date(
            year=int(year(date_str)),
            month=int(month(date_str)),
            day=int(day(date_str))
        )

        mapping = {
            'days': dt + timedelta(days=interval),
            'weeks': dt + relativedelta(weeks=interval),
            'months': dt + relativedelta(months=interval),
            'years': dt + relativedelta(years=interval)
        }

        try:
            return mapping[unit].isoformat()
        except KeyError:
            raise TypeError(
                "Invalid unit. Choose from ['days', 'weeks', 'months', 'years']"
            )
    return date_add(date_trunc(date_str), interval, unit)

def date_diff(start_date: str, end_date: str, unit: str = 'days') -> int | TypeError:

    if not (is_date(start_date) and is_date(end_date)):
        raise TypeError("Invalid date")

    dt1 = date(
        year=int(year(start_date)),
        month=int(month(start_date)),
        day=int(day(start_date))
    )

    dt2 = date(
        year=int(year(end_date)),
        month=int(month(end_date)),
        day=int(day(end_date))
    )

    diff = relativedelta(dt2, dt1)

    mapping = {
        'days': abs((dt2 - dt1).days),
        'weeks': abs((dt2 - dt1).days) // 7,
        'months': abs(diff.years * 12 + diff.months),
        'years': abs(diff.years)
    }

    try:
        return mapping[unit]
    except KeyError:
        raise TypeError(
            "Invalid unit. Choose from ['days', 'weeks', 'months', 'years']"
        )

def main():

    dt = input("Date: ")

    print(date_add(dt, 10, 'days'))

if __name__ == '__main__':
    main()
