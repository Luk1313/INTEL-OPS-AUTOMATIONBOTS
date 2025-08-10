DB_URL=sqlite:///intel.db

MISP_URL=https://tu-misp
MISP_KEY=changeme
MISP_VERIFY_SSL=true

SHODAN_API_KEY=changeme
CISA_KEV_URL=https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.csv


# ⚠️ Importante: No subas tu .env a repositorios públicos.
## 3️⃣ Inicializar base de datos
python - << 'PY'
import sqlite3, pathlib
pathlib.Path('intel.db').touch()
con = sqlite3.connect('intel.db')
con.executescript(open('sql/schema.sql','r',encoding='utf-8').read())
con.commit(); con.close()
print("Base de datos inicializada con éxito.")
PY


# ▶️ Uso Rápido
 ## 1) Ingesta de datos (CISA KEV)
uvicorn src.api.main:app --reload --port 8000
# Documentación Swagger: http://localhost:8000/docs

## 3) Iniciar Dashboard
streamlit run src/dashboard/app.py
# Interfaz: http://localhost:8501




