from typing import Dict, Any
import json
from pydantic import BaseModel, ValidationError
import numpy as np

from core.sa import build_suffix_array
from core.lcp import build_lcp_array

class SuffixRequest(BaseModel):
    """Request model for the suffix‑array endpoint."""
    text: str

class SuffixResponse(BaseModel):
    suffix_array: list[int]
    lcp_array: list[int]

class SuffixArrayHandler:
    """A Flask‑style handler that processes a dict payload and returns a dict response.

    No actual network traffic occurs; the method can be called directly in tests or
    examples. The implementation validates input with pydantic and delegates the
    heavy lifting to the core modules.
    """

    def handle_request(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        try:
            req = SuffixRequest(**payload)
        except ValidationError as exc:
            raise ValueError(f"Invalid request payload: {exc}")

        s = req.text
        sa = build_suffix_array(s)
        lcp = build_lcp_array(s, sa)
        resp = SuffixResponse(suffix_array=sa.tolist(), lcp_array=lcp.tolist())
        return json.loads(resp.json())
