from setuptools import setup

# This is a fork of forecastiopy by David Ervideira david.dme@gmail.com
# This version provides Python 3 compatibility

setup(name='forecastiopy',
      version='0.1',
      description='A wrapper to access weather data provided by forecast.io',
      url='https://github.com/bitpixdigital/forecastiopy',
      author='Angel Hernandez',
      author_email='info@bitpixdigital.com',
      license='Eclipse Public License',
      packages=['forecastiopy'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
