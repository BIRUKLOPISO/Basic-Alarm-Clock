import time
import datetime


def set_alarm():
    alarm_time = input("Enter the alarm time (HH:MM AM/PM): ")

    # Convert the input time to 24-hour format
    hour, minute, period = alarm_time.split(':')
    hour = int(hour)
    minute = int(minute)
    if period.upper() == 'PM' and hour != 12:
        hour += 12
    elif period.upper() == 'AM' and hour == 12:
        hour = 0

    alarm_datetime = datetime.datetime.now().replace(hour=hour, minute=minute, second=0)

    # Check if the alarm time is in the past
    if alarm_datetime < datetime.datetime.now():
        alarm_datetime += datetime.timedelta(days=1)

    print(f"Alarm set for {alarm_datetime.strftime('%I:%M %p')}")
    return alarm_datetime


def main():
    alarm_datetime = set_alarm()

    while True:
        current_time = datetime.datetime.now()
        if current_time >= alarm_datetime:
            print("Wake up!")
            break
        time.sleep(1)


if __name__ == "__main__":
    main()