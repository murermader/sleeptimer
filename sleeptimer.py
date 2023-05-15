import argparse
import re
import datetime
import time
import subprocess

if __name__ == "__main__":
    parser = argparse.ArgumentParser("sleeptimer")
    parser.add_argument(
        "time_span",
        metavar="TIME_SPAN",
        help="Time to wait before going to sleep. h = hours, m = minutes, s = seconds. For example: 1h30m",
        type=str,
    )

    args = parser.parse_args()
    time_span = args.time_span

    total_wait_time_s = 0

    hours_match = re.search(r"(\d+)h", time_span)
    minutes_match = re.search(r"(\d+)m", time_span)
    seconds_match = re.search(r"(\d+)s", time_span)

    if hours_match:
        hours = int(hours_match.group(1))
        total_wait_time_s += hours * 60 * 60
    if minutes_match:
        minutes = int(minutes_match.group(1))
        total_wait_time_s += minutes * 60
    if seconds_match:
        seconds = int(seconds_match.group(1))
        total_wait_time_s += seconds

    now = datetime.datetime.now()
    sleep_time = now + datetime.timedelta(0, total_wait_time_s)
    
    print(f"Will go to sleep at [{sleep_time.time():%H:%M:%S}]. Press CTRL+C to cancel.")
    time.sleep(total_wait_time_s)
    subprocess.run(["pmset", "sleepnow"])