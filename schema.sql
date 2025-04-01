DROP TABLE IF EXISTS url_shortener;

CREATE TABLE url_shortener (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    full_url TEXT NOT NULL,
    hash_code TEXT NOT NULL,
    UNIQUE(hash_code)
);