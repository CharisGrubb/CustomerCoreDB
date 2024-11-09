import requests 


response = requests.get("http://127.0.0.1:8000/user", headers={'username':"jediMaster", 'password':"R2D2_for_President"})
