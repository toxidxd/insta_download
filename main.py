import instaloader
import random

proxies = {
   'https': 'https://IP:port',
    }

L = instaloader.Instaloader(request_timeout=random.randint(300, 900))


# L.login(USER, PASSW) # login for private account
ins_prof = input("Input instagram profile name: ")

# L.download_profile(ins_prof, profile_pic_only=True)
L.download_profile(ins_prof)

