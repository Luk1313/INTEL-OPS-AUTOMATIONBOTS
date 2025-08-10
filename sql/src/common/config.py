import os
from dotenv import load_dotenv
load_dotenv()

DB_URL = os.getenv("DB_URL", "sqlite:///intel.db")

MISP_URL = os.getenv("MISP_URL")
MISP_KEY = os.getenv("MISP_KEY")
MISP_VERIFY_SSL = os.getenv("MISP_VERIFY_SSL", "true").lower() == "true"

SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")
CISA_KEV_URL = os.getenv("CISA_KEV_URL")
