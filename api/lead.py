"""POST /api/lead — append a lead to the Marketing Leads Google Sheet.

Accepts JSON: { source, name, email, handle?, details? }
"""
from http.server import BaseHTTPRequestHandler
import json
import os
import datetime

import gspread
from google.oauth2.service_account import Credentials

SHEET_ID = "1QlC5RAZqEltSeifX28B3d6B-fmt56b10RCR3WiHGa0M"
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
]


def _build_client():
    raw = os.environ.get("GSHEETS_SA_JSON_CONTENT")
    if not raw:
        raise RuntimeError("GSHEETS_SA_JSON_CONTENT env var is not set")
    info = json.loads(raw)
    creds = Credentials.from_service_account_info(info, scopes=SCOPES)
    return gspread.authorize(creds)


def _send(handler, status, body):
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json")
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
    handler.send_header("Access-Control-Allow-Headers", "Content-Type")
    handler.end_headers()
    handler.wfile.write(json.dumps(body).encode("utf-8"))


class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        _send(self, 204, {})

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", 0))
            payload = json.loads(self.rfile.read(length) or "{}")
        except Exception:
            return _send(self, 400, {"ok": False, "error": "invalid_json"})

        name = (payload.get("name") or "").strip()
        email = (payload.get("email") or "").strip()
        if not name or not email:
            return _send(self, 400, {"ok": False, "error": "name_and_email_required"})

        source = (payload.get("source") or "unknown").strip()[:64]
        handle = (payload.get("handle") or "").strip()[:120]
        details = (payload.get("details") or "").strip()[:4000]
        ua = (self.headers.get("User-Agent") or "")[:300]
        timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        try:
            gc = _build_client()
            sh = gc.open_by_key(SHEET_ID)
            ws = sh.sheet1
            ws.append_row(
                [timestamp, source, name, email, handle, details, ua],
                value_input_option="USER_ENTERED",
            )
        except Exception as exc:
            return _send(self, 500, {"ok": False, "error": "sheet_write_failed", "detail": str(exc)[:200]})

        return _send(self, 200, {"ok": True})
