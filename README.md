# faastapi_plugin_han_cock Plugin Scaffold

This scaffold provides a starting structure for building a plugin.

## Folder Structure

```
faastapi_plugin_han_cock/
├── core/
│   └── models.py       # Define your models or data classes here
├── tests/
│   └── test_faastapi_plugin_han_cock.py  # Example pytest
├── router.py           # API routes for your plugin (exposes APIRouter)
├── deps.txt            # Add plugin-specific dependencies here
├── requirements.txt    # Base dependencies (FastAPI, Pydantic)
├── __init__.py         # Exposes `router` for the plugin manager
└── README.md           # This file
```

## Setup

### 1) Create & Activate a Virtual Environment

**Linux / macOS**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell)**
```powershell
python -m venv venv
venv\Scripts\activate
```

### 2) Install Base Dependencies
```bash
pip install -r requirements.txt
```

### 3) Install Plugin-Specific Dependencies
Add any extra dependencies to `deps.txt`, then:
```bash
pip install -r deps.txt
```

### 4) Run Tests
If you run pytest from the parent directory *containing* this plugin folder:
```bash
pytest -q
```
Alternatively, ensure the parent directory of this plugin is on `PYTHONPATH`.

## Using the Router
Your plugin exposes `router` via `__init__.py`. Example in a FastAPI app:
```python
from faastapi_plugin_han_cock import router
app.include_router(router)
```
The base path is the plugin name, e.g. `/{self.plugin_name}`.
