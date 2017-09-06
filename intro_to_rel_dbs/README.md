# Intro to Relational Databases

This course is an introduction to relational databases. It covers topics like: SQLite, Postgres, Python's DB API, and beginner SQL Syntax.

## Final Project

The final project is to build an application that simulates a [Swiss Tournament](https://en.wikipedia.org/wiki/Swiss-system_tournament).  I had to design the database to hold players' information and the outcomes of matches in order to simulate the tournament described on the wiki page.


## Database Design

### Tables
The first table (Players) keeps track of the players in the tournament and has a unique ID and a non-unique name.

    |  id   |  name   |
    | ----- | ------  |
    |   1   |  Matt   |
    |   2   |  Batman |

The second table keeps track of each match.  The first column is a unique match_id and serves as the primary key of the table.  The next columns are winner and loser.  Winner and loser are both foreign keys which reference the id in the Players table.

    | match_id | winner | loser |
    | -------- | ------ | ----- |
    |     1    |    1   |   2   |

In the table above the first match was between Matt and Batman. Matt won the match.

### Views
It was recommended to make views for information that we would regularly be gathering from the table.  The business logic of the tournament relies on the **standings** so this is an obvious candidate.  The standings rely on the number of **wins** a player has as well as the **total number of games** they have played.  I decided to make these views as well.

## Application
The Python code is very simple.  There are methods for adding/deleting players and matches as well as recording results of a match and gathering the standings.

### My Additions

* I decided to clean up the code by adding a namedtuple for the standings.  Now the tuple can be accessed by attritbute names instead of magic numbers.
* I also decided to add a context manager for connecting to the database.  This got rid of lots of duplication by doing the connecting and cleanup in the `__enter__` and `__exit__` methods.

Most of the functions had the following code:

    db = connect()
    cursor = db.cursor()
    cursor.execute(...)
    db.commit()
    db.close()
