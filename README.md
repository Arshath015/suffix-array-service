# suffix-array-service  
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)  
[![Python: 3.9+](https://img.shields.io/badge/Python-3.9%2B-green.svg)](https://www.python.org/downloads/)

One‑liner: A lightweight HTTP‑style service for on‑the‑fly suffix‑array and LCP construction.

## Table of Contents
- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Theoretical Background](#theoretical-background)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Endpoint Reference](#endpoint-reference)
- [Testing](#testing)
- [Limitations](#limitations)
- [Roadmap](#roadmap)
- [License](#license)

## Overview
The **suffix-array-service** exposes a single logical endpoint that accepts a plain‑text string and returns both its suffix array and the corresponding longest common prefix (LCP) array. The service is packaged as a pure‑Python library; the HTTP‑style handler is deliberately decoupled from any real network stack so that it can be invoked directly in‑process.

## Tech Stack
- Python 3.9+
- `numpy` for efficient integer array handling
- `pydantic` for request/response validation
- Standard library (`http.server` style interface) for the API façade

## Architecture
```text
suffix-array-service/
├─ api/
│  └─ routes.py          # HTTP‑style request handler
├─ core/
│  ├─ sa.py              # Suffix array construction
│  └─ lcp.py             # LCP array computation
├─ examples/
│  └─ client_example.py # Demonstrates a request/response cycle
├─ tests/
│  ├─ test_sa.py        # Unit tests for suffix array
│  └─ test_lcp.py       # Unit tests for LCP array
├─ docs/
│  └─ endpoint_reference.md # Endpoint table and semantics
├─ requirements.txt
└─ README.md
```

## Theoretical Background
A *suffix array* (SA) is a sorted list of all suffixes of a string, represented by their starting indices. Constructing the SA in O(n log n) time can be achieved with the classic doubling algorithm, which repeatedly sorts suffixes by the first 2^k characters using a stable key‑pair sort. Although linear‑time algorithms exist (e.g., SA‑IS), the doubling method offers a clear trade‑off between simplicity and performance for typical input sizes.

The *longest common prefix* (LCP) array stores, for each adjacent pair of suffixes in the SA, the length of their longest common prefix. Kasai's algorithm computes the LCP in linear time by leveraging the inverse suffix array and a sliding window that reuses previously computed prefix lengths.

Both structures are fundamental in string matching, substring queries, and bio‑informatics. By exposing them via a service, downstream components can off‑load the heavy lifting of string preprocessing while retaining deterministic, testable behavior.

## Installation
```bash
git clone https://github.com/yourorg/suffix-array-service.git
cd suffix-array-service
pip install -r requirements.txt
```

## Usage
```python
from api.routes import SuffixArrayHandler
from pydantic import BaseModel

payload = {"text": "banana"}
response = SuffixArrayHandler().handle_request(payload)
print(response)
# {'suffix_array': [5, 3, 1, 0, 4, 2], 'lcp_array': [0, 1, 3, 0, 0, 2]}
```

## API Reference
### `SuffixArrayHandler.handle_request(payload: dict) -> dict`
- **payload** – JSON‑compatible dict with a single key `"text"` containing the input string.
- **returns** – Dict with keys `"suffix_array"` (list[int]) and `"lcp_array"` (list[int]).

### `core.sa.build_suffix_array(s: str) -> numpy.ndarray`
Computes the suffix array using the doubling algorithm.

### `core.lcp.build_lcp_array(s: str, sa: numpy.ndarray) -> numpy.ndarray`
Computes the LCP array via Kasai's method.

## Endpoint Reference
See `docs/endpoint_reference.md` for a concise table of request/response fields.

## Testing
Run the test suite with:
```bash
pytest -q
```
The suite covers typical cases, edge cases (empty string, single character), and validates the relationship between SA and LCP.

## Limitations
- The current implementation assumes ASCII input; Unicode code points are treated as individual Python characters but may affect sorting order.
- Memory usage is O(n) for the arrays; extremely large strings (>10⁷ chars) may exhaust RAM.

## Roadmap
- Add optional linear‑time SA‑IS implementation.
- Support streaming input for very large texts.
- expose a real Flask/FastAPI wrapper for external consumption.

## License
MIT © 2026
