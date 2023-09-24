BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS temperature (
    record_id serial PRIMARY KEY,
    city TEXT,
    temperature REAL,
    timestamp DATETIME
);

COMMIT;