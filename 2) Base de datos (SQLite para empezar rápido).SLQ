CREATE TABLE IF NOT EXISTS indicators (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ioc_type TEXT NOT NULL,
  value TEXT NOT NULL,
  first_seen TEXT,
  last_seen  TEXT,
  source     TEXT,
  confidence INTEGER,
  tags       TEXT,       -- JSON como string en SQLite
  ttps       TEXT,       -- JSON como string
  metadata   TEXT,       -- JSON como string
  UNIQUE (ioc_type, value, source)
);
