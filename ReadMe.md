# Mozambique Energy Pipeline

A batch ETL pipeline built on World Bank energy and mining data for Mozambique (1970–2025), structured using a medallion architecture and containerized with Docker.

## Architecture

```
CSV (World Bank) → Bronze (raw parquet) → Silver (pivoted, cleaned) → Gold (DuckDB)
```

- **Bronze** — raw ingestion, timestamped parquet, schema preserved as-is
- **Silver** — filtered to post-1990, pivoted from long to wide format, columns standardized to snake_case, negative energy imports flagged
- **Gold** — derived metrics written to DuckDB: urban/rural electricity access gap, net energy exporter flag

## Tech Stack

- Python, Pandas
- DuckDB
- Docker
- Pytest

## Project Structure

```
├── src/
│   ├── extraction.py
│   ├── transformation.py
│   └── loading.py
├── tests/
│   ├── conftest.py
│   └── unit_test.py
├── Data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
├── main.py
├── Dockerfile
└── requirements.txt
```

## Run with Docker

```bash
docker build -t moz_energy_pipeline .
docker run -v ${PWD}/Data:/app/Data moz_energy_pipeline
```

## Run locally

```bash
pip install -r requirements.txt
python main.py
```

## Run tests

```bash
pytest tests/unit_test.py -v
```

## Data Source

World Bank — Energy & Mining indicators for Mozambique  
https://data.worldbank.org