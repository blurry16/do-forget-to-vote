import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0"
}
MCNAME = "Your Minecraft nickname goes here."

try:
    requests.post(
        url="https://www.planetminecraft.com/server/cubeville/vote/",
        headers=HEADERS,
        data={"mcname": MCNAME, "servervote": "1"},
    )
    print("Finished with no exceptions. Enjoy ^w^!")
except Exception as e:
    print(f"Exception {e} occurred. Try again later.")
