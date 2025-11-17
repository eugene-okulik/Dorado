import os

from datetime import datetime, timedelta


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
data_file_path = os.path.join(
    homework_path, "eugene_okulik", "hw_13", "data.txt"
)


def get_date_from_line(line):
    date_str = line.split(". ", 1)[1].split(" - ")[0]
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")


def add_week(date_object):
    return date_object + timedelta(weeks=1)


def get_weekday(date_object):
    return date_object.strftime("%A")


def days_ago(date_object):
    return (datetime.now() - date_object).days


with open(data_file_path) as file:
    lines = file.readlines()

    date_from_line_one = get_date_from_line(lines[0])
    print(add_week(date_from_line_one))

    date_from_line_two = get_date_from_line(lines[1])
    print(get_weekday(date_from_line_two))

    date_from_line_three = get_date_from_line(lines[2])
    print(f"{days_ago(date_from_line_three)} days ago")
