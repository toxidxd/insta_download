import instaloader


proxies = {
   'https': 'https://IP:port',
    }

L = instaloader.Instaloader()


# L.login(USER, PASSW) # login for private account
ins_prof = input("Input instagram profile name: ")

L.download_profile(ins_prof, profile_pic_only=True)

