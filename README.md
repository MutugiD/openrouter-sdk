# openrouter‑sdk

A lightweight Python SDK for OpenRouter that automatically rotates free‑tier models to avoid rate limits and provides a drop‑in HTTP client wrapper.

## Features

- Automatic detection and rotation of free‑model variants on rate‑limit errors (429/402).
- Pluggable rotation policies (round‑robin, least‑used, weighted).
- Transparent retry/backoff on transient failures.
- Simple, dependency‑wrapped HTTP client interface.
- Structured logging and optional metrics hooks.

## Prerequisites

- Python 3.7 or newer
- Git

## Installation

### Linux/macOS

```bash
# Clone the repo
git clone https://github.com/MutugiD/openrouter-sdk.git
cd openrouter-sdk

# (Optional) create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install SDK in editable mode
pip install -e .
```

### Windows (PowerShell)

```powershell
# Clone the repo
git clone https://github.com/your-org/openrouter-sdk.git
cd openrouter-sdk

# (Optional) create a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install SDK in editable mode
pip install -e .
```

## Setup

1. **Configure your API key**
   - Set the environment variable:
     - Linux/macOS: `export OPENROUTER_API_KEY="your_key_here"`
     - Windows: `setx OPENROUTER_API_KEY "your_key_here"`

2. **(Optional) Customize model rotation**
   Edit or create a `config.yaml` at the project root:

   ```yaml
   api_key: "${OPENROUTER_API_KEY}"
   models:
     - model_id: "gpt-3.5-turbo:free"
       daily_limit: 50
       rate_limit_per_minute: 20
     - model_id: "gpt-4o-mini:free"
       daily_limit: 50
       rate_limit_per_minute: 20
   rotation_policy: "round_robin"
   ```

## Quickstart

```python
from sdk import RequestDispatcher

# Initialize dispatcher (reads OPENROUTER_API_KEY automatically)
client = RequestDispatcher(
    api_key="${OPENROUTER_API_KEY}",
    models=["gpt-3.5-turbo:free", "gpt-4o-mini:free"]
)

# Make a request
response = client.dispatch("GET", "/api/v1/auth/key")
print(response.json())
```

## Packaging

To build distributable packages:

```bash
# Source root of openrouter-sdk
# Install build tools
pip install --upgrade build twine

# Build source and wheel
python -m build

# Upload to PyPI
python -m twine upload dist/*
```

## Running Tests

```bash
# From repo root
pytest
```

## Docker

- **Run tests in container**
  ```bash
docker build -t openrouter-sdk-test .
docker run --rm openrouter-sdk-test
```
- **Development container**
  ```bash
docker build -f Dockerfile.dev -t openrouter-sdk-dev .
```

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Write tests and docstrings.
4. Run `pre-commit run --all-files`.
5. Submit a pull request.

---

*Project maintained by [MutugiD]*

