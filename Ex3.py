def timing (hours, minutes, seconds):
    overall_hours= 3600*hours
    overall_minutes= 60*minutes
    overall_seconds=seconds

    if overall_hours>=overall_minutes and overall_hours>=overall_seconds:
        return hours
    elif overall_minutes>=overall_hours and overall_minutes>= overall_seconds:
        return minutes
    else:
        return seconds

print(timing(15, 955, 59400))