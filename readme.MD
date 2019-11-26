Weatherly - A Weather App that uses Darksky API
===
Python 3 wrapper for Darksky API

Installation steps
***
```python
python3 setup.py install
```

Alternative (Docker required) [Docker installation page](https://docs.docker.com/v17.09/engine/installation/#time-based-release-schedule)


```docker
cd ~/Weatherly
docker-compose up

```


How to use this library:
***
Register for an API key for Darksky. Click here for: [Darksky](https://darksky.net/forecast/).

Sample request

Create WeatherReq object, then pass this object through the other classes.

Get the temperature for this hour in Dublin.

```python
import src.ds_API.WeatherReq as WeatherReq
import sec.ds_API.HourReq as HourReq
Dublin = [53.3244431,-6.3857877]
API_KEY=""
    req = WeatherReq.WeatherReq(API_KEY, latitude=Dublin[0], longitude=Dublin[1])
    curr = CurrentReq.CurrentReq(req)
    print(f'Temperature: {curr.temperature} degrees')
```

Dependencies:
Requests module - [Requests](https://pypi.org/project/requests/)
