import requests 

def check_user_get_methods():
    response = requests.get("http://127.0.0.1:8000/all_users", headers={'username':"jediMaster", 'password':"R2D2_for_President"})
    if response.status_code == 200:
        for user in response.json()['results']:
            params = {"user_id" : user['user_id']}
            response = requests.get("http://127.0.0.1:8000/user", params=params,headers={'username':"jediMaster", 'password':"R2D2_for_President"})
            if response.status_code != 200:
                print("Error getting user with ID " + user['user_id'])
    else:
        print("Error getting all users")
    


check_user_get_methods()



