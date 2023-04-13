PRAGMA foreign_keys = ON;
CREATE TABLE countries (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE NOT NULL);
CREATE TABLE producers (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    country_id INTEGER, 
    description TEXT,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    updated_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (country_id) REFERENCES countries(id)
);
CREATE TABLE sneakers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT NOT NULL,
    color TEXT NOT NULL,
    price REAL CHECK (price > 0),
    producer_id INTEGER,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    updated_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (producer_id) REFERENCES producers(id)
);
CREATE TABLE sport_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    is_team NUMERIC,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    updated_at NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE teams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country_id INTEGER,
    description TEXT,
    sport_type_id INTEGER,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    updated_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (country_id) REFERENCES countries(id),
    FOREIGN KEY (sport_type_id) REFERENCES sport_types(id)
);
CREATE TABLE sponsors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    country_id INTEGER,
    description TEXT,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    updated_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (country_id) REFERENCES countries(id)
);
CREATE TABLE sponsors_teams (
    sponsor_id INTEGER,
    team_id INTEGER,
    start_year INTEGER NOT NULL,
    end_year INTEGER,
    PRIMARY KEY (sponsor_id, team_id),
    FOREIGN KEY (sponsor_id) REFERENCES sponsors(id),
    FOREIGN KEY (team_id) REFERENCES teams(id)
);
CREATE TABLE profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    phone TEXT,
    username TEXT UNIQUE NOT NULL,
    description TEXT,
    age INTEGER,
    height INTEGER,
    weight INTEGER
);
CREATE TABLE players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    updated_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    country_id INTEGER,
    sport_type_id INTEGER,
    team_id INTEGER,
    profile_id INTEGER UNIQUE,
    FOREIGN KEY (country_id) REFERENCES countries(id),
    FOREIGN KEY (sport_type_id) REFERENCES sport_types(id),
    FOREIGN KEY (team_id) REFERENCES teams(id),
    FOREIGN KEY (profile_id) REFERENCES profiles(id)
);
CREATE TABLE sneakers_players (
    sneaker_id INTEGER,
    player_id INTEGER,
    PRIMARY KEY (sneaker_id, player_id),
    FOREIGN KEY (sneaker_id) REFERENCES sneakers(id),
    FOREIGN KEY (player_id) REFERENCES players(id)
);
