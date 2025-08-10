# INTEL-OPS-AUTOMATION

Automatización de **ingestión**, **normalización** y **visualización** de inteligencia de amenazas (Threat Intel) desde fuentes como **CISA KEV**, **MISP** y **Shodan**.  
Incluye API propia (FastAPI) y un dashboard rápido (Streamlit) para explorar indicadores.

---

## 🧭 Objetivo

- Unificar la **recolección de IoCs/Eventos** desde múltiples fuentes.
- **Normalizar y deduplicar** con un esquema STIX-like.
- Exponer una **API interna** para búsquedas y consumo por otros sistemas.
- Proveer un **dashboard** para análisis exploratorio y reporting.
- Dejar lista la base para **escalado** (PostgreSQL/Timescale, Redis, Docker, CI/CD).

---

## 🧱 Arquitectura (visión general)

