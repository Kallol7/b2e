"""Convert Benglai Text to English Phonetic Using Bengali IPA API. ( Source: https://ipa.bangla.gov.bd/ )"""

import requests
import json
import re

# Change the headers if necessary
b2e_default_headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,bn;q=0.8",
    "Connection": "keep-alive",
    "Dnt": "1",
    "Host": "ipa.bangla.gov.bd",
    "Referer": "https://ipa.bangla.gov.bd/",
    "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "Sec-Ch-Ua-Mobile": "?1",
    "Sec-Ch-Ua-Platform": "Android",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

ipa_to_eng = {
    "ɔ": "o",
    "ʱ": "h",
    "ɟ": "j",
    "ʲ": "y",
    "ʃ": "s",
    "d̪": "d",
    "ʰ": "h",
    "t̪": "t",
    "ʷ": "w",
    "o͡": "o",
    "u̯": "u",
    "a͡": "a",
    "o̯": "o",
    "i̯": "i",
    "æ": "e",
    "e͡": "e",
    "ŋ": "n",
    "ɽ": "r",
    "ã": "a",
    "ph": "f"
}

def b2e(text=None, headers=None, default_headers=False, ipa=False):
    """Convert Benglai Text to English Phonetic Using Bengali IPA API. ( Source: https://ipa.bangla.gov.bd/ )

    Args:
        text: string
        headers: dictionary [Optional]
        default_headers: bool, use default_headers if True, also overrides headers [Optional]
        

    Returns:
        string, Bengali text converted to English phonetic
        
        If b2e(text,ipa=True) is called, returns IPA string instead
    """


    if text is None:
        text = input("Enter link: ")
    
    if default_headers:
        headers = b2e_default_headers
    
    requests.packages.urllib3.disable_warnings()
    resp_str = json.loads(requests.get(f"https://ipa.bangla.gov.bd/post_text_bangla_ipa?bangla_ipa={text}",headers=headers, verify=False).text)["data"][0]
    
    if ipa:
        return resp_str
    
    for key,value in ipa_to_eng.items():
        resp_str = re.sub(key, value, resp_str)
    return resp_str

if __name__=="main":
    b2e()
