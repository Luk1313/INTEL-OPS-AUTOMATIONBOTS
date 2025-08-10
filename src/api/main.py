from fastapi import FastAPI, Query
from sqlalchemy import create_engine, text
from src.common.config import DB_URL

app = FastAPI(title="IntelOps API", version="1.0.0")
engine = create_engine(DB_URL, future=True)

@app.get("/health")
def health(): return {"ok": True}

@app.get("/indicators")
def list_indicators(ioc_type: str | None = None, source: str | None = None, limit: int = 100):
    q = "SELECT ioc_type,value,first_seen,last_seen,source,confidence,tags,ttps,metadata FROM indicators"
    cond, args = [], {}
    if ioc_type: cond.append("ioc_type=:t"); args["t"]=ioc_type
    if source:  cond.append("source=:s");   args["s"]=source
    if cond: q += " WHERE " + " AND ".join(cond)
    q += " ORDER BY last_seen DESC LIMIT :l"; args["l"]=limit
    with engine.begin() as con:
        rows = con.execute(text(q), args).mappings().all()
        return {"count": len(rows), "results": [dict(r) for r in rows]}

@app.get("/search")
def search(value: str = Query(..., min_length=3)):
    with engine.begin() as con:
        rows = con.execute(text(
            "SELECT * FROM indicators WHERE value LIKE :v ORDER BY last_seen DESC LIMIT 200"
        ), {"v": f"%{value}%"}).mappings().all()
        return {"count": len(rows), "results": [dict(r) for r in rows]}
