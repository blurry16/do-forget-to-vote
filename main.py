import requests
from time import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0"
}
MCNAME = ""
if MCNAME == "":
    raise Exception("MCNAME not set")

start_time = time()

try:
    requests.post(
        url="https://www.planetminecraft.com/server/cubeville/vote/",
        headers=HEADERS,
        data={"mcname": MCNAME, "servervote": "1"},
    )
    print(
        f"Finished with no exceptions for {round(time() - start_time, 1)} seconds. Enjoy ^w^!"
    )
except Exception as e:
    print(
        f"Exception {e} occurred. Try again later. ({round(time() - start_time, 1)} seconds elapsed)"
    )
