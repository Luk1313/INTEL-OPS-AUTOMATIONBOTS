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

## EJECUTA LUEGO

python - << 'PY'
import sqlite3, pathlib
pathlib.Path('intel.db').touch()
con = sqlite3.connect('intel.db')
con.executescript(open('sql/schema.sql','r',encoding='utf-8').read())
con.commit(); con.close()
print("DB inicializada")
PY
