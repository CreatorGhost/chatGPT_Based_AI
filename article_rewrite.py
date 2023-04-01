import re

import requests
import json


def rewrite_article(spin_cap, text):
    url = "https://backend-spinbot-wrapper-prod.azurewebsites.net/spin/rewrite-text"

    payload = json.dumps({
        "text": text,
        "x_spin_cap_words": spin_cap
    })
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'DNT': '1',
        'Origin': 'https://articlerewritertool.com',
        'Referer': 'https://articlerewritertool.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        text = re.sub(r"\\n", "\n", response.text)
        return text
    else:
        return False
