from setuptools import setup


setup(name='Weatherly',
      version='0.1',
      description='A wrapper to access weather data provided by darksky.net',
      url='https://github.com/MarkMcMoran/Weatherly',
      author='Mark McMoran',
      author_email='markmcmoran96@gmail.com',
      license='Eclipse Public License',
      install_requires=[
          'requests',
      ],
      zip_safe=False)