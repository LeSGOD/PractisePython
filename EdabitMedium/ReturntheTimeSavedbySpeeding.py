    """One cause for speeding is the desire to shorten the time spent traveling. While in long distance trips speeding does save an appreciable amount of time, the same cannot be said about short distance trips.

Create a function that calculates the amount of time saved (in minutes) were you traveling with an average speed that is above the speed-limit as compared to traveling with an average speed exactly at the speed-limit.

    """
def time_saved(s_lim, s_avg, d):
    return round(d/s_lim - d/s_avg,1)

