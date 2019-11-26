class DailyReq(object):
    daily = None

    def __init__(self, WeatherReq):
        if WeatherReq.has_hourly():
            self.daily = WeatherReq.gDaily()
            for item in WeatherReq.gDaily().keys():
                setattr(self, item, WeatherReq.gDaily()[item])
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
