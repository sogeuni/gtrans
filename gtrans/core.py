import json
import re
from urllib.error import HTTPError
from urllib.parse import quote_plus, unquote
from urllib.request import urlopen, Request

user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

def translate(source_text, target_lang="auto", source_lang="auto"):
    base_url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=%s&tl=%s&dt=t&q=%s"

    source_text = quote_plus(source_text)
    url = base_url % (source_lang, target_lang, source_text)
    request = Request(url, headers=user_agent)

    try:
        response = urlopen(request)
    except HTTPError as e:
        print(e)
        return ""

    raw_response = response.read().decode("utf-8")
    raw_response = re.sub(r'([^(",")(\],\[)(\d,)])(,)', r'\1%2C', raw_response)
    raw_response = re.sub(r'([^"\]\d])((?=,))', r'\1""\2', raw_response)

    try:
        json_response = json.loads(raw_response)
    except:
        print("json parse error: " + raw_response)
        return ""

    result = ""
    for line in json_response[0]:
        result += unquote(line[0])

    return result
