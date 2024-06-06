# This software stopped working properly.
Since 6/6/2024 PlanetMC added Captcha to their voting system. Now my code doesn't work because idk how to break captchas.  
This repository will be archived until this code will work again OR i find out how to break captchas.  
Please contact me in Discord (blurry16) or Telegram (@blurry16) if you know a way how to make it working again.  
If you post a do-forget-to-vote 2.0 please mention me somehow. Or don't. I don't really care.

# do-forget-to-vote
A script that uses planet mc (the only one captchaless) API to vote and get rid of "Don't forget to vote" message on Cubeville.

### Requirements
- python3
- requests library _(pip install requests)_
- Replace MCNAME constant in main.py file on your nickname (MCNAME is **CaSe-SeNsiTive**)

<details>
    <summary> Additionally </summary>
    In the new version I removed fake user-agent because there's no difference in the result but you had to install one more library. If you want to you can replace <code>HEADERS["User-Agent"]</code> value on your user-agent. I left already generated one for you though.
</details>