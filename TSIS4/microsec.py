from datetime import datetime

current_datetime = datetime.now()

datetime_without_microseconds = current_datetime.replace(microsecond=0)

print(f"Original datetime: {current_datetime}")
print(f"Datetime without microseconds: {datetime_without_microseconds}")
