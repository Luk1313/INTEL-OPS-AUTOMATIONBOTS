# INTEL-OPS-AUTOMATION

**INTEL-OPS-AUTOMATION** es una plataforma modular para **automatizar la ingestión, normalización, almacenamiento y visualización** de inteligencia de amenazas (**Threat Intelligence**), integrando fuentes como **CISA KEV**, **MISP** y **Shodan**, con capacidad de expansión a nuevas fuentes y formatos.

Incluye:
- **Ingestores** para múltiples fuentes públicas y privadas.
- **Normalización STIX-like** para homogenizar indicadores.
- **API interna** basada en **FastAPI**.
- **Dashboard interactivo** con **Streamlit**.
- **Automatización CI/CD** para ingestión periódica.
- **Estructura escalable** para integrarse con SOC, SIEM y entornos Red/Blue Team.

---

## 📌 Propósitos del Proyecto

1. **Centralización de inteligencia**: Reunir en una sola base de datos indicadores de amenazas (IoCs), vulnerabilidades críticas y eventos relevantes.
2. **Normalización de datos**: Estandarizar la información en formatos comunes como STIX 2.1 para facilitar su reutilización.
3. **Automatización operativa**: Reducir la intervención manual mediante procesos programados de ingestión y limpieza de datos.
4. **Interoperabilidad**: Permitir que otras aplicaciones y equipos consuman datos a través de la API interna.
5. **Visualización estratégica**: Mostrar métricas, tendencias y correlaciones para apoyar la toma de decisiones.
6. **Escalabilidad**: Ampliar el sistema a nuevas fuentes y dashboards sin reescribir la arquitectura.
7. **Integración con respuesta**: Facilitar la conexión con sistemas de orquestación y respuesta (SOAR) para activar alertas automáticas.

---

## 🔍 Observaciones y Alcance

- El proyecto **no reemplaza** un SIEM o un sistema de monitoreo en tiempo real, pero puede alimentarlos.
- Puede usarse como **laboratorio de Threat Intelligence** para entrenar a equipos de SOC, Red Team o analistas de ciberseguridad.
- Compatible con entornos **on-premise** y en la nube (AWS, Azure, GCP).
- Se recomienda **migrar a PostgreSQL/TimescaleDB** en producción.
- La automatización CI/CD es opcional, pero clave para mantener datos frescos.
- El uso de **APIs externas** implica cumplir las políticas de cada proveedor.
- Se debe definir un **plan de retención y depuración** de datos para evitar sobrecarga.

---

## 🛠 Métodos de Uso

### Uso Diario (Operacional)
1. Ejecutar ingestores de fuentes clave.
2. Revisar indicadores recientes en el dashboard.
3. Filtrar por fuente, tipo de IoC, severidad y fecha.
4. Exportar información para equipos de respuesta o inteligencia.

### Uso Semanal (Analítico)
1. Revisar tendencias de amenazas (top vulnerabilidades, ataques por vector).
2. Correlacionar datos con incidentes internos o reportes de seguridad.
3. Generar reportes ejecutivos para dirección o clientes.

### Uso Mensual (Estrategia)
1. Revisar patrones a largo plazo.
2. Incorporar nuevas fuentes o ajustar filtros de ingestión.
3. Integrar la API con otros sistemas de detección y respuesta.
4. Evaluar desempeño y cobertura de las fuentes utilizadas.

---

## 🏁 Fin de Uso / Cierre de Proyecto

Cuando el sistema se detenga o se decida cerrar:
- Exportar todos los datos relevantes a un formato estándar (CSV, JSON, STIX).
- Revocar credenciales y API keys de todas las integraciones.
- Borrar datos sensibles según las políticas de la organización.
- Documentar las lecciones aprendidas y ajustes requeridos para futuras implementaciones.
- Archivar la configuración y scripts para referencia futura.

---

## 🏗 Arquitectura

```plaintext
[SOURCES]
  ├─ CISA KEV (CSV público)
  ├─ MISP (PyMISP)
  └─ Shodan API
        │
        ▼
[INGESTORS] → [NORMALIZER (STIX-like) + UPSERT] → [DB]
                                                  │
                                    ┌─────────────┴─────────────┐
                                    ▼                           ▼
                               [REST API]                  [DASHBOARD]
                                FastAPI                     Streamlit

---

## 🏗 Arquitectura

```plaintext
[SOURCES]
  ├─ CISA KEV (CSV público)
  ├─ MISP (PyMISP)
  └─ Shodan API
        │
        ▼
[INGESTORS] → [NORMALIZER (STIX-like) + UPSERT] → [DB]
                                                  │
                                    ┌─────────────┴─────────────┐
                                    ▼                           ▼
                               [REST API]                  [DASHBOARD]
                                FastAPI                     Streamlit


