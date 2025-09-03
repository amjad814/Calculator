import datetime
import time

# User se alarm time lena (format HH:MM)
alarm_time = input("Set alarm time (HH:MM 24-hour format): ")

print(f"⏰ Alarm set for {alarm_time}")

while True:
    # Current time nikalna
    now = datetime.datetime.now().strftime("%H:%M")

    # Agar current time alarm time ke barabar ho jaye
    if now == alarm_time:
        print("⏰ Wake up! Time's up!")
        break

    # CPU ko free rakhne ke liye thoda wait
    time.sleep(10)
