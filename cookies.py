import pip._vendor.requests as requests

with requests.Session() as http_session:
    requests.session().cookies.set("my_cookie", "my_val", domain="https://wikipedia.com")

    r = http_session.get("https://wikipedia.com")
    print(r.cookies)  