import calendar
import locale
from functools import wraps

def short_form(func):
    @wraps(func)
    def wrapper():
        full_days = func()
        return [calendar.day_abbr[calendar.day_name.index(day)] for day in full_days]
    return wrapper

def translate(language):
    def decorator(func):
        @wraps(func)
        def wrapper():
            locale.setlocale(locale.LC_TIME, language)
            full_days = func()
            return [day[:2] for day in full_days]  # Using first two letters for abbreviation
        return wrapper
    return decorator
