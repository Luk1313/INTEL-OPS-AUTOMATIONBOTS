src/
├─ common/
│  ├─ config.py           # Configuración y carga de variables de entorno
│  └─ models.py           # Modelos Pydantic estilo STIX
├─ ingest/
│  ├─ cisa_kev_ingest.py  # Ingesta CISA KEV
│  ├─ misp_ingest.py      # Ingesta MISP
│  └─ shodan_ingest.py    # Ingesta Shodan
├─ normalize/
│  └─ stix_normalizer.py  # Normalización de datos
├─ api/
│  └─ main.py             # API FastAPI
└─ dashboard/
   └─ app.py              # Dashboard Streamlit
sql/
└─ schema.sql             # Esquema de base de datos
.github/workflows/
└─ scheduled.yml          # Ingesta automatizada CI/CD
.env.example              # Ejemplo de configuración
requirements.txt          # Dependencias
