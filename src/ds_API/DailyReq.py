class DailyReq(object):
    daily = None

    def __init__(self, weather_req):
        if weather_req.has_hourly():
            self.daily = weather_req.gDaily()
            for item in weather_req.gDaily().keys():
                setattr(self, item, weather_req.gDaily()[item])
            for day in range(0, self.days()):
                for item in self.gDay(day).keys():
                    setattr(self, 'hour_' + str(day + 1) + '_' + item,
                            self.gDay(day)[item])

    def get(self, day=None):
        if day is None:
            return self.daily
        else:
            return self.get_hour(day)

    def gDay(self, day):
        if day > self.days():
            return None
        else:
            return self.get()['data'][day - 1]

    def days(self):
        return len(self.get()['data'])
