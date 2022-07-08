properties = {
    "data":{
        "profiles":[
            {
                "name":"Ram",
                "rank":1,
                "contact":["987633","97623"]
            },
            {
                "name":"Sita",
                "rank":2,
                "contact":["9372523","986322"]
            }
        ]
    }
}

profiles = properties.get("data").get("profiles")
for profile in profiles:
    print("**************")
    print(f"Name: {profile.get('name')}")
    print(f"Rank: {profile.get('rank')}")
    for idx, contact in enumerate(profile.get("contact"),1):
        print(f"Contact{idx}: {contact}")