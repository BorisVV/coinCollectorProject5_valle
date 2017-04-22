# "coinCollectorProject5_valle"

* This app uses beautifulSoup4 for scrapping a table of quarter coins from
	https://en.wikipedia.org/wiki/50_State_Quarters
	This information is then saved to a csv file.

# PIP INSTALL
* django
* requests
* beautifulsoup4
* Jinja2
* psycopg2
* folium

! Pillow is not required for this app.

# Command lines and to RUN APP from it.
*	from the dir coinCollectorApp/ run the following commands.
* $ python coinSite/manage.py makemigrations
* $ python coinSite/manage.py migrate

* $ run_app_manager.py  --> to load the data to db.sqlite3
* $ python coinSite/manage.py runserver

#
![alt text](coinCollectorApp/screenshots/quaters_page.png "Screen shot of site")
![alt text](coinCollectorApp/screenshots/page.png "Smaller screen view")
