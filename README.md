# Delivery Mama
> A multi vendor based product & parcel delivery System.


#### Setup

##### Dependencies

- Python 3.10
- postgres  12.5

The following steps will walk you thru installation on a Mac. Linux should be similar. It's also possible to develop 
on a Windows machine, but I have not documented the steps. If you've developed django apps on Windows, you should have little problem getting up and running.


##### Create database
``
psql postgres
CREATE DATABASE bissasto
``

###### 1st open in your system terminal then follow the command line.

```bash
git clone https://gitlab.com/deliverymamadevelopmentteam/deliverymamacms.git
cd deliverymamacms
```

###### Then copy code from the ``env_example`` and create new file `.env` then pasts

-------------------------------------------
```bash
|--> .env_example
|--> .env
```


#### Open postgres using terminal database:
```
psql postgres 
```

Run the application in your local development server:

```bash
virtualenv venv --python=python3.10
source venv/bin/activate
pip install -r requirements.txt
./manage.py makemigrations user
./manage.py migrate user
./manage.py migrate
./mangae.py runserver
```


## Happy coding :wink:
