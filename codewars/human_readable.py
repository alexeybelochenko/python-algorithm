# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

def format_duration(seconds):
    times = ["year", "day", "hour", "minute", "second"]
    if seconds == 0:
        return "now"
    else:
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        y, d = divmod(d, 365)
        time = [y, d, h, m, s]  # [year, day, hour, ...]
        readable_time = []
        l = list(zip(time, times))  # [(y,"year"),(d,"day")...]
        for i in l:
            t, ts = i  # t=y ts=year , t=d, ts=day...
            if t:
                t_s = [ts if t is 1 else ts + "s"]  # year or +"s"
                readable_time_str = " "+str(t)+" "+"".join(t_s)  # y year/s  d day/s
                readable_time.append(readable_time_str)  # ["y year/s", "d day/s", ...]
        if len(readable_time) == 1:
            return ("".join(readable_time)).strip()
        else:
            return (",".join(readable_time[:-1]) + " and" + "".join(readable_time[-1])).strip()