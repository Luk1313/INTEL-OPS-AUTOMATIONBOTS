import json
from sqlalchemy import create_engine, text
from src.common.models import Indicator
from src.common.config import DB_URL

engine = create_engine(DB_URL, future=True)

def upsert_indicators(items):
    with engine.begin() as con:
        for it in items:
            ind = Indicator(**it)
            con.execute(text("""
                INSERT INTO indicators
                (ioc_type, value, first_seen, last_seen, source, confidence, tags, ttps, metadata)
                VALUES (:ioc_type, :value, :first_seen, :last_seen, :source, :confidence, :tags, :ttps, :metadata)
                ON CONFLICT(ioc_type, value, source) DO UPDATE SET
                  last_seen=excluded.last_seen,
                  confidence=CASE WHEN excluded.confidence>indicators.confidence
                                  THEN excluded.confidence ELSE indicators.confidence END,
                  metadata=excluded.metadata
            """), {
                "ioc_type": ind.ioc_type,
                "value": ind.value,
                "first_seen": ind.first_seen.isoformat() if ind.first_seen else None,
                "last_seen": ind.last_seen.isoformat() if ind.last_seen else None,
                "source": ind.source,
                "confidence": ind.confidence,
                "tags": json.dumps(ind.tags),
                "ttps": json.dumps(ind.ttps),
                "metadata": json.dumps(ind.metadata)
            })
