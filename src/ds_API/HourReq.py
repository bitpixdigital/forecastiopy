class HourReq(object):
    hourly = None

    def __init__(self, WeatherReq):
        if WeatherReq.has_hourly():
            self.hourly = WeatherReq.hourly()
            for item in WeatherReq.hourly().keys():
                setattr(self, item, WeatherReq.hourly()[item])
            for hour in range(0, self.hours()):
                for item in self.hour().keys():
                    setattr(self, 'hour_' + str(hour + 1) + '_' + item,
                            self.hour()[item])

    def get(self):
        if self.hour is None:
            return self.hourly
        else:
            return self.hour(self.hour)

    def hour(self):
        if self.hour > self.hours():
            return None
        else:
            return self.get()['data'][self.hour - 1]

    def hours(self):
        return len(self.get()['data'])
