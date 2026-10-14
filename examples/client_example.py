import os
from api.routes import SuffixArrayHandler

def main() -> None:
    handler = SuffixArrayHandler()
    payload = {"text": "mississippi"}
    response = handler.handle_request(payload)
    out_dir = os.path.join(os.path.dirname(__file__), "..", "results")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "output.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"Input: {payload['text']}\n")
        f.write(f"Suffix Array: {response['suffix_array']}\n")
        f.write(f"LCP Array: {response['lcp_array']}\n")
    print(f"Result written to {out_path}")

if __name__ == "__main__":
    main()
