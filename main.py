import schedule, datetime


def job():
    hour = str(datetime.datetime.now().time()).split(":")[0]
    print(f"Ку " * (hour % 12))


schedule.do(job)

while True:
    schedule.run_pending()