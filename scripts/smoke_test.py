import requests, time

urls = ['http://127.0.0.1:5000/', 'http://127.0.0.1:5000/analyze-page', 'http://127.0.0.1:5000/check']
for u in urls:
    ok = False
    for i in range(20):
        try:
            r = requests.get(u, timeout=5)
            print(u, '->', r.status_code, 'bytes=', len(r.content))
            ok = True
            break
        except Exception as e:
            time.sleep(0.5)
    if not ok:
        print(u, '-> FAILED')
