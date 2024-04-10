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