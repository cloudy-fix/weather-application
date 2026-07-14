# Weather Application

Simple Kivy desktop app that retrieves live weather data by city using the OpenWeather API.

## Features

- City-based weather lookup.
- Temperature, weather description, humidity, wind speed, and pressure display.
- Environment-driven API key configuration.
- Network timeout and API error handling.

## Setup

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
copy .env.example .env
```

Set `OPENWEATHER_API_KEY` in `.env` or in your shell environment before running.

## Run

```bash
python weather_app.py
```

## Production Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Operations Guide](docs/OPERATIONS.md)
- [Architecture Diagram](docs/diagrams/architecture.mmd)
- [Workflow Diagram](docs/diagrams/workflow.mmd)
- [Security Policy](SECURITY.md)
- [Contributing Guide](CONTRIBUTING.md)

