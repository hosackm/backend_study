# Frontend Foundations

 This course covers:

  1. CRUD operations
  2. database ORMs (like SQLAlchemy) and how they are used as a backend for web applications
  3. Web application frameworks like Flask
  4. How to blend 2 and 3 to create a data driven dynamic web application

## Final Project

The final project is an API for restaurants.  The homepage of the application lists the restaurants in the database.  You can add a new restaurant, click to view the menu of one of the restaurants in the database, edit a restaurant, or delete a restaurant.

Each restaurant has its own menu.  The menu lists the items that can be ordered from a restaurant as well as links to edit or a delete an entry.

The application can also serve restaurant and menu information in JSON form by exposing extra endpoints ending in `<route>/json`

## What I learned

I was already familiar with SQL databases and Flask.  This course mainly taught me about [SQLAlchemy](https://www.sqlalchemy.org/) and how to use it to implement a CRUD application.  The power of a object relational mapper was immediately apparent to me.  Using a tool like SQLAlchemy I am able to focus on defining my models and their relationships and not setting up the database correctly and typing out the boilerplate necessary to connect the dots.

This is also the first time I every implemented a REST api myself.  I've consumed information from REST apis many times but never the other way around.
