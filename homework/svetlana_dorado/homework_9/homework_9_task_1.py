import datetime


my_date = "Jan 15, 2023 - 12:05:33"

python_date = datetime.datetime.strptime(my_date, "%b %d, %Y - %H:%M:%S")

full_month = python_date.strftime("%B")

datetime_string = python_date.strftime("%d.%m.%Y, %H:%M")


print(full_month)
print(datetime_string)
