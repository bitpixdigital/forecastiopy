class FlagReq(object):
    flags = None

    def __init__(self, WeatherReq):
        if WeatherReq.has_flags():
            self.flags = WeatherReq.gFlags()
            for item in self.flags.keys():
                setattr(self, item, self.flags[item])

    def get(self):
        return self.flags

    def available_flags(self):
        return self.get().keys()