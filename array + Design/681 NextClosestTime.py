def nextClosestTime(time):
        """
        :type time: str
        :rtype: str
        """
        time_str = time.split(":")
        minute, hour = int(time_str[1]), int(time_str[0])
        a = set(time)
        while True:
            minute += 1
            if minute == 60:
                minute =0
                hour += 1
            if hour == 24:
                hour = 0
            hour_str = str(hour) if hour > 9 else "0"+str(hour)
            minute_str = str(minute) if minute > 9 else "0"+str(minute)
            new_set = set(hour_str + minute_str)
            if new_set <= a:
                return hour_str + ":"+ minute_str