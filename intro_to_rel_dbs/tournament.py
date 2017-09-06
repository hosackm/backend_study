import psycopg2
from collections import namedtuple

# used namedtuple for nice attribute access
Record = namedtuple("Record", ("id", "name", "wins", "total"))


class DBConnection:
    """
    DB Context Manager for getting rid of duplicated connect, execute, commit, and close calls.
    """
    def __enter__(self):
        self.db = connect()
        self.cursor = self.db.cursor()
        return self.cursor

    def __exit__(self, *args):
        self.db.commit()
        self.db.close()

    # expose methods from Python's DB-API
    def execute(self):
        self.cursor.execute()

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    with DBConnection() as db:
        db.execute("DELETE FROM matches;")


def deletePlayers():
    """Remove all the player records from the database."""
    with DBConnection() as db:
        db.execute("DELETE FROM players;")


def countPlayers():
    """Returns the number of players currently registered."""
    with DBConnection() as db:
        db.execute("SELECT COUNT(*) FROM players;")
        n = db.fetchone()
    return n[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    with DBConnection() as db:
        db.execute("INSERT INTO players (name) VALUES (%s);", (name,))


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    with DBConnection() as db:
        db.execute("SELECT * FROM standings;")
        standings = db.fetchall()

    # assemble a named tuple for every database entry
    return [Record(*s) for s in standings]


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    with DBConnection() as db:
        db.execute("INSERT INTO matches (winner, loser) VALUES (%s, %s)", (winner, loser))


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    return [(standings[2*i].id, standings[2*i].name, standings[2*i+1].id, standings[2*i+1].name)
            for i in range(len(standings)//2)]
