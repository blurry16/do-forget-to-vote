import requests
from fake_useragent import UserAgent
import time

HEADERS = {"User-Agent": UserAgent().random}
MCNAME = "blurry16"

nt = time.time()

try:
    requests.post(
        url="https://www.planetminecraft.com/server/cubeville/vote/",
        headers=HEADERS,
        data={"mcname": MCNAME, "servervote": "1"},
    )
except Exception as e:
    print(f"Exception {e} occurred")

print(f"Finished for {round(time.time() - nt, 1)} seconds.")
