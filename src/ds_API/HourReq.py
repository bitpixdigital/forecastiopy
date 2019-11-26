class HourReq(object):
    hourly = None

    def __init__(self, weather_req):
        if weather_req.has_hourly():
            self.hourly = weather_req.hourly()
            for item in weather_req.hourly().keys():
                setattr(self, item, weather_req.hourly()[item])
            for hour in range(0, self.hours()):
                for item in self.hour().keys():
                    setattr(self, 'hour_' + str(hour + 1) + '_' + item,
                            self.hour()[item])

    def get(self):
        if self.hour is None:
            return self.hourly
        else:
            return self.get_hour(self.hour)

    def hour(self):
        if self.hour > self.hours():
            return None
        else:
            return self.get()['data'][self.hour - 1]

    def hours(self):
        return len(self.get()['data'])
