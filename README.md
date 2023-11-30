# it-website
***

# 🚀 Features
- Django 4.1 & Python 3.11
- Install via Pip
- Blog website
- Comments feature included
- Interated with [Postresql](https://www.postgresql.org/)
- Static files for media,css,js
- Integrated [Summernote WYSIWYG Editor](https://summernote.org/)
- Sitemap
- Styling with Bootstrap v5
- Debugging with django-debug-toolbar
- DRY forms with django-crispy-forms
***
# 📖 Installation
it-website can be installed via Pip. To start, clone the repo to your local computer and change into the proper directory.
```
$ git clone https://github.com/SantoshAcharya1200/it-website.git
$ cd it-website
```
## pip
```
(.venv) $ pip install -r requirements.txt
(.venv) $ python manage.py makemigrations
(.venv) $ python manage.py migrate
(.venv) $ python manage.py createsuperuser
(.venv) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```
## Postgres intregation 
We need to install the PostgreSQL database adapter to communicate to the database with Python to install it run the following command in the shell.
```
pip install psycopg2
```
Open your Django project’s settings.py file (located inside the main project folder) and navigate to the DATABASES setting. By default, Django is configured to use SQLite, but we’ll change that to use PostgreSQL.
Replace the DATABASES setting with the following code:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',  # Replace with your PostgreSQL server's address if necessary
        'PORT': '',          # Leave empty to use the default PostgreSQL port (usually 5432)
    }
}
```
Next, apply the initial database migrations to create the necessary tables in the PostgreSQL database. Run the following commands:
```
python manage.py makemigrations
python manage.py migrate
```
Now run the server:
```
py manage.py runserver
```
Visit http://127.0.0.1:8000/ in your web browser, and if everything is set up correctly, you should see the Django default landing page.
# License
Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

# Screenshots
![image](https://github.com/SantoshAcharya1200/it-website/assets/41406942/ec5e9fbe-9c23-4933-957b-a32f1e2d77f4)
![image](https://github.com/SantoshAcharya1200/it-website/assets/41406942/e755fa1e-df1f-4ebf-a8f1-ff6ec1497fd2)
![image](https://github.com/SantoshAcharya1200/it-website/assets/41406942/43c4862e-6ea2-4579-a108-1239995ec5c2)
![image](https://github.com/SantoshAcharya1200/it-website/assets/41406942/7f0957ae-79e6-4175-a8d8-c67ba9b8163a)
![image](https://github.com/SantoshAcharya1200/it-website/assets/41406942/ebd02719-6541-4832-a149-04bbf6558d2b)





