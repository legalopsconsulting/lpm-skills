"""
send_briefing.py
----------------
Sends the most recent .docx briefing file as an email attachment
via Microsoft Graph API using client credentials (no user interaction).

Called by the Claude Code Routine after the briefing .docx is produced.

Usage:
    python send_briefing.py --file PATH_TO_DOCX [--subject "Custom subject"]

Environment variables (set in Routine cloud environment):
    GRAPH_TENANT_ID     - Azure AD tenant ID
    GRAPH_CLIENT_ID     - App registration client ID
    GRAPH_CLIENT_SECRET - App registration client secret
    BRIEFING_RECIPIENT  - Email address to send to
"""

import argparse
import base64
import json
import os
import sys
from datetime import datetime
from pathlib import Path

import requests


# ── Config ─────────────────────────────────────────────────────────────────────

TENANT_ID     = os.environ.get("GRAPH_TENANT_ID",     "c713000a-4c2e-4719-ac5d-e605d323ede2")
CLIENT_ID     = os.environ.get("GRAPH_CLIENT_ID",     "51030c5f-cbbe-421d-bd0f-87c0d0a3779a")
CLIENT_SECRET = os.environ.get("GRAPH_CLIENT_SECRET", "72d6b397-c000-4dfa-81b0-24aeae98ec9d")
SENDER        = os.environ.get("BRIEFING_SENDER",     "scott@LegalOpsConsultingLimited.onmicrosoft.com")
RECIPIENT     = os.environ.get("BRIEFING_RECIPIENT",  "scott@legalopsconsulting.co.uk")
GRAPH_BASE    = "https://graph.microsoft.com/v1.0"


# ── Auth ───────────────────────────────────────────────────────────────────────

def get_token():
    """Client credentials flow — no user interaction required."""
    url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
    data = {
        "grant_type":    "client_credentials",
        "client_id":     CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope":         "https://graph.microsoft.com/.default",
    }
    r = requests.post(url, data=data)
    r.raise_for_status()
    token = r.json().get("access_token")
    if not token:
        raise ValueError(f"Token request failed: {r.text}")
    return token


# ── Send ───────────────────────────────────────────────────────────────────────

def send_briefing(docx_path: Path, subject: str, token: str):
    """Send the .docx as an email attachment via Graph sendMail."""
    with open(docx_path, "rb") as f:
        content_b64 = base64.b64encode(f.read()).decode()

    payload = {
        "message": {
            "subject": subject,
            "body": {
                "contentType": "Text",
                "content": (
                    f"LPM Monday Portfolio Briefing — {datetime.now().strftime('%d %B %Y')}\n\n"
                    "Produced automatically by the LPM Monday Sweep Routine.\n"
                    "Source: Outlook (7-day sweep) + SharePoint matter folders.\n\n"
                    "Open the attached .docx for the full briefing."
                )
            },
            "toRecipients": [
                {"emailAddress": {"address": RECIPIENT}}
            ],
            "attachments": [
                {
                    "@odata.type":  "#microsoft.graph.fileAttachment",
                    "name":         docx_path.name,
                    "contentType":  "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    "contentBytes": content_b64,
                }
            ]
        },
        "saveToSentItems": "false"
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type":  "application/json"
    }

    r = requests.post(
        f"{GRAPH_BASE}/users/{SENDER}/sendMail",
        headers=headers,
        json=payload
    )

    if r.status_code == 202:
        print(f"✓ Briefing sent to {RECIPIENT}")
        print(f"  Subject: {subject}")
        print(f"  Attachment: {docx_path.name} ({docx_path.stat().st_size // 1024} KB)")
    else:
        print(f"✗ Send failed: {r.status_code} — {r.text}")
        sys.exit(1)


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Send LPM briefing .docx via Graph API")
    parser.add_argument("--file",    required=False, help="Path to .docx file to send")
    parser.add_argument("--subject", required=False, help="Email subject line")
    args = parser.parse_args()

    # Find the .docx — explicit path or most recent in working directory
    if args.file:
        docx_path = Path(args.file)
        if not docx_path.exists():
            print(f"✗ File not found: {docx_path}")
            sys.exit(1)
    else:
        candidates = sorted(Path(".").glob("*.docx"), key=lambda p: p.stat().st_mtime, reverse=True)
        if not candidates:
            print("✗ No .docx file found in working directory")
            sys.exit(1)
        docx_path = candidates[0]
        print(f"  Using most recent .docx: {docx_path.name}")

    # Subject
    date_str = datetime.now().strftime("%d %B %Y")
    subject = args.subject or f"LPM Monday Briefing — {date_str}"

    # Check client secret
    if not CLIENT_SECRET:
        print("✗ GRAPH_CLIENT_SECRET environment variable not set")
        print("  Add it in the Routine's cloud environment variables")
        sys.exit(1)

    print(f"Sending briefing via Graph API...")
    token = get_token()
    send_briefing(docx_path, subject, token)


if __name__ == "__main__":
    main()
