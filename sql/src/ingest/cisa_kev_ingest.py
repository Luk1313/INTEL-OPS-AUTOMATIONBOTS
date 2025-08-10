import pandas as pd, io, requests, datetime as dt
from src.common.config import CISA_KEV_URL
from src.normalize.stix_normalizer import upsert_indicators

def fetch_cisa_kev():
    r = requests.get(CISA_KEV_URL, timeout=30)
    r.raise_for_status()
    df = pd.read_csv(io.StringIO(r.text))
    indicators=[]
    for _, row in df.iterrows():
        first = None
        try:
            first = dt.datetime.strptime(str(row.get("dateAdded","")), "%Y-%m-%d")
        except Exception:
            pass
        indicators.append({
            "ioc_type": "cve",
            "value": str(row["cveID"]),
            "first_seen": first,
            "last_seen": dt.datetime.utcnow(),
            "source": "cisa_kev",
            "confidence": 80,
            "tags": ["known-exploited", str(row.get("vendorProject",""))],
            "ttps": [],
            "metadata": {
                "description": row.get("shortDescription", ""),
                "requiredAction": row.get("requiredAction","")
            }
        })
    upsert_indicators(indicators)
    print(f"Ingeridos {len(indicators)} CVEs de CISA KEV.")

if __name__ == "__main__":
    fetch_cisa_kev()
