class MinuteReq(object):
    minutely = None

    def __init__(self, weather_req):
        if weather_req.has_minutely():
            self.minutely = weather_req.gMinutely()
            for item in weather_req.gMinutely().keys():
                setattr(self, item, weather_req.gMinutely()[item])
            for minute in range(0, self.minutes()):
                for item in self.getMinutes(minute).keys():
                    setattr(self, 'minute_' + str(minute + 1) + '_' + item,
                            self.getMinutes(minute)[item])

    def get(self, minute=None):
        if minute is None:
            return self.minutely
        else:
            return self.getMinutes(minute)

    def getMinutes(self, minute):
        if minute > self.minutes():
            return None
        else:
            return self.get()['data'][minute - 1]

    def minutes(self):
        return len(self.get()['data'])
