# Forex Predictor

This application will display exchange rates sourced from the [US
Federal Reserve](https://www.federalreserve.gov/).

The latest available rates are displayed relative to the US Dollar by
default.  This can be changed by selecting a different *base
currency*.  A timeseries of exchange rates of a single *target
currency* relative to the base is displayed graphically.  The target
can be changed by selecting one of current rates.  The time range of
the graph is selectable also.

The exchange timeseries values are displayed in a table and there is a
link that allows this selected time series to be downloaded in *CSV*
format.

Current financial news is displayed in a sidebar next to the exchnage
rate data.

'''
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py loadcurrencies
python manage.py loadrates
python manage.py loadstories
python manage.py runserver
'''