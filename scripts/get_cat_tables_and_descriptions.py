import httpx

headers = {
    'Accept': 'text/event-stream',
    'Authorization': 'Bearer jina_f43e37353e164d3e8be83e005c322f995CHs0jLHp4t-ETQX0GRGccW_vdQo',
    'X-Respond-With': 'readerlm-v2'
}

url = 'https://r.jina.ai/https://www.example.com'
response = httpx.get(url, headers=headers, timeout=60*10)

print(response.text)