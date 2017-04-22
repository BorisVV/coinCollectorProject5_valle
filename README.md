# "coinCollectorProject5_valle"

* This app uses beautifulSoup4 for scrapping a table of quarter coins from
	https://en.wikipedia.org/wiki/50_State_Quarters
*	This information is then saved to a csv file which then is sent to the db where
*	django pulls the data to be displayed as a table on a local host IP address (127.0.0.1:8000)

* Clone of for the app. ---> https://github.com/BorisVV/coinCollectorProject5_valle

# pip freeze > requirements.txt
# create an eniroment in your machine
# $ enviromentenv nameOFEnviromentHere

# PIP INSTALL
* django
* requests
* beautifulsoup4
* Jinja2
* psycopg2
* folium
* pandas

! Pillow is not required for this app but can be install with pip if needed.

# Command lines and to RUN APP (first time follow the this instructions.).
* 		from the dirictory coinCollectorApp/ run the following commands.
* $ python coinSite/manage.py makemigrations
* $ python coinSite/manage.py migrate

* $ run_app_manager.py  --> to load the data to db.sqlite3
* $ python coinSite/manage.py runserver

#
![alt text](coinCollectorApp/screenshots/quaters_page.png "Screen shot of site")
![alt text](coinCollectorApp/screenshots/page.png "Smaller screen view")
