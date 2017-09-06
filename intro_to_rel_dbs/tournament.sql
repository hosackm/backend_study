DROP VIEW IF EXISTS standings;
DROP VIEW IF EXISTS totalgames;
DROP VIEW IF EXISTS wins;
DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS players;

CREATE TABLE players(
    id SERIAL PRIMARY KEY,
    name VARCHAR(250)
);

CREATE TABLE matches(
    match_id SERIAL PRIMARY KEY,
    winner INTEGER,
    loser INTEGER,
    FOREIGN KEY (winner) REFERENCES players(id),
    FOREIGN KEY (loser) REFERENCES players(id)
);

-- INSERT INTO players (name) VALUES ('Matt');     -- 1-1
-- INSERT INTO players (name) VALUES ('Scott');    -- 1-1
-- INSERT INTO players (name) VALUES ('Curtis');   -- 1-1
-- INSERT INTO players (name) VALUES ('Wes');      -- 1-1

-- INSERT INTO matches (winner, loser) VALUES(1, 2); -- Matt beat Scott
-- INSERT INTO matches (winner, loser) VALUES(4, 3); -- Wes beat Curtis
-- INSERT INTO matches (winner, loser) VALUES(4, 1); -- Wes beat Matt
-- INSERT INTO matches (winner, loser) VALUES(2, 3); -- Scott beat Curtis

-- Create a view to track the wins a player has
CREATE VIEW wins AS (
    SELECT players.id, COUNT(matches.winner) as num
    FROM players
    LEFT JOIN matches
    ON players.id = matches.winner
    GROUP BY players.id
);

-- Create a view to track total game played
CREATE VIEW totalgames AS (
    SELECT players.id, COUNT(matches.loser) as num
    FROM players
    LEFT JOIN matches
    ON players.id IN (matches.winner, matches.loser)
    GROUP BY players.id
);

-- Create a view to track the standings
CREATE VIEW standings AS (
    SELECT players.id, players.name, wins.num AS wins, totalgames.num AS total
    FROM players, wins, totalgames
    WHERE players.id = wins.id
    AND players.id = totalgames.id
    ORDER BY CAST(wins.num AS FLOAT) / CAST(NULLIF(totalgames.num, 0) AS FLOAT) DESC
);
