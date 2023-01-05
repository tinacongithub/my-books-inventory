# my-books-inventory

This inventory has two separate apps developed using Django.

One of these two apps, my_books_blog, has Bootstrap components that show a Web Blog.

On the Blog you can:

Create, read, update and delete blog posts.
Create and update profiles.
Add a picture to a blog post.
Send, read and delete messages.

Install

To install this software you need to:

Check your python version

This project was written with python 3.11.0 so make sure you test it with this version or higher to avoid compatibility issues.

Install Dependencies

In order to install dependencies, run pip install (make sure you are in the project folder)

Some operative systems will require you to use pip3 instead of pip 

Setting Up the Django Application

Once you finish the dependencies installation, run the following Django commands:

Migrations

To initialize the database:

> python mananage.py migrate

windows:

c:\> py mananage.py migrate

Run the test server

> python mananage.py runserver
windows:

c:\> py mananage.py runserver

Go to localhost:8000/ to have access to the app.

If everthing goes well, you should be able to open the browser and see the application running

