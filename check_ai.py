import requests
import json
from pprint import pprint


def retry(article):
    url = "https://contentatscale.ai/ai-content-detector/"
    payload = "content=" + article + "&action=checkaiscore"
    headers = {
        'authority': 'contentatscale.ai',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '_ga_7XNS620Y7W=GS1.1.1674808321.1.0.1674808321.0.0.0; _ga=GA1.1.1053155832.1674808322; _tt_enable_cookie=1; _ttp=yXBAeVJ3aNisiiFbbAtt21qmrLZ; ext_name=ojplmecpdpgccookcobabopnaifgidhf',
        'dnt': '1',
        'origin': 'https://contentatscale.ai',
        'referer': 'https://contentatscale.ai/ai-content-detector/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200 and json.loads(response.text)["status"] != 'Failure':
        json_data = json.loads(response.text)

        if json_data["score"] > 70:
            return {'isHuman': True}
        else:
            return {'isHuman': False}
    else:
        return False


def is_article_valid(article):
    url = "https://app.copyleaks.com/api/v1/dashboard/anonymous/ai-scan/submit/text"
    payload = json.dumps({
        "text": article
    })
    headers = {
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'DNT': '1',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-platform': '"macOS"'
    }
    # return  retry(article)
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code != 200:
        print("Retrying")
        res = retry(article)
        if res:
            return res
    if response.status_code == 200:
        json_data = json.loads(response.text)
        return json_data
    else:
        print("Res Code is ", response.status_code, response)
        return False


#
# art = "The term \"blockchain technology\" means: A digital ledger called blockchain technology is used to record and verify transactions across a decentralized computer network. It is frequently utilized to create decentralized systems that are resistant to tampering and fraud. It is a secure and transparent method of storing data.\nA Blockchain is essentially a computer network that stores a digital record of transactions. There are a set of transactions in each block of the chain; once a block is added to the chain, it cannot be changed or removed. All transactions are recorded in a way that cannot be altered and is permanent.\n\nThe fact that the data that is stored on a blockchain is protected by cryptography to ensure that it can only be accessed by those with the appropriate permissions is the most significant feature of the technology. Because of this, it is extremely difficult to hack or manipulate blockchain, making it an ideal technology for the safe transfer and storage of sensitive data.\n\nAdditionally, blockchain technology enables the development of decentralized systems, in which data are under the control of multiple parties. Instead, the data is spread out over the network, and multiple parties verify transactions. Transparency and trust among participants are increased as a result of this, which eliminates the need for intermediaries and central authorities.\n\nAn introduction to Supply Chain Management: The process of planning, executing, and controlling the flow of goods, services, and information from suppliers to customers is known as supply chain management (SCM). From acquiring raw materials to delivering the final product to the customer, it entails managing the entire life cycle of a product. Procurement, production, logistics, and distribution are all included in this.\nBusinesses must have efficient supply chain management in order to remain competitive in today's global marketplace. It enables businesses to optimize the flow of goods and services, cut expenses, and boost productivity. In addition, supply chain management is essential for ensuring that products are delivered to customers on time, in sufficient quantities, and at high quality levels.\n\nThe lack of traceability and transparency in the supply chain is a major obstacle. Inefficiencies, increased costs, and even fraud may result from this. By providing an immutable, transparent record of all transactions that can be easily traced, blockchain technology offers a solution to these issues.\n"
#
# if is_article_valid(art) and is_article_valid(art)['isHuman']:
#     print("dd")
# else:
#     print("Noo")
