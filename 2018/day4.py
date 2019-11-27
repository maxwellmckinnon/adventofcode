# coding=utf-8

from collections import defaultdict
import re
import pprint

datafile = "./day4_input.txt"
data = open(datafile, 'r')

timeslept = defaultdict(lambda: 0) # dict from guard ID to total minutes slept
guardminutesasleep = {}  # dict from guard ID to dicts that map the minute of day to how many times it's been slept through

def main():
    # Only consider minutes 0 to 59 for this problem

    sorteddatalist = sorted(data.readlines())

    # pprint.pprint(sorteddatalist)
    pattern_time = re.compile(r"\[\d*-\d*-\d* (\d*):(\d*)\]")
    pattern_guardidbeginsshift = re.compile(r"Guard #(\d*) begins shift")

    for line in sorteddatalist:
        # print(f"Line: {line}")
        m = re.search(pattern_time, line)
        hour = int(m.group(1))
        minute = int(m.group(2))
        if "Guard" in line:
            m = re.search(pattern_guardidbeginsshift, line)
            guard_id = m.group(1)

            # add guard to guardminutesasleep dict as well
            if guard_id not in timeslept:
                thisguard = defaultdict(lambda: 0)
                guardminutesasleep[guard_id] = thisguard
        elif "falls asleep" in line:
            starttime = minute
        elif "wakes up" in line:
            endtime = minute
            timeslept[guard_id] += endtime - starttime
            for minute_step in range(starttime, endtime): # specifically states not to include the end time for this piece
                guardminutesasleep[guard_id][minute_step] += 1

    pprint.pprint(timeslept)
    pprint.pprint(guardminutesasleep)


    timesleptlist = list(timeslept.items())
    timesleptlist.sort(key=lambda i: i[1])
    mostslept = timesleptlist[-1][1]
    mostsleptguard = timesleptlist[-1][0]
    print(f"most slept guard: {mostsleptguard}")
    print(f"Most slept: {mostslept}")

    specific_guard_sleep_stats = guardminutesasleep[mostsleptguard]

    #print(f"specific_guard_sleep_stats: {specific_guard_sleep_stats}")
    mostminute, _ = get_minute_most_time(specific_guard_sleep_stats)
    print(f"mostminute: {mostminute}")

    print(f"answer: {int(mostsleptguard) * mostminute}")


    # Part 2
    mostminute_guard = -10
    mostminuteguard_time = -10
    mostminuteguard_minute = -10

    for guard, timetable in guardminutesasleep.items():
        if timetable:
            minutes, counter = get_minute_most_time(timetable)
            if counter > mostminuteguard_time:
                mostminute_guard = guard
                mostminuteguard_time = counter
                mostminuteguard_minute = minutes
        else:
            print(f"ERROR: {guard}")
    print(f"Most found guard and minute: {mostminute_guard}, {mostminuteguard_minute}, mult: {int(mostminute_guard) * mostminuteguard_minute}")

def get_minute_most_time(timedict):
    # Return minute as well as counts for that minute as a tuple
    statslist = list(timedict.items())
    statslist.sort(key=lambda i: i[1])

    try:
        return statslist[-1][0], statslist[-1][1]
    except IndexError:
        print(statslist)
        #print(statslist[-1])

if __name__ == '__main__':
    main()
