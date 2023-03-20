user ={
    "name":"brahim",
    "age":40,
    "country":"Alg",
    "skills": ["html","css"],
    "bool" : True
}
print(user)
print(user["name"])
print(user.get("name"))


lang = {
    "one":{
        "name": "css",
        "progress":"80%"
    },
    "two":{
        "name": "html",
        "progress":"90%"
    },
    "three":{
        "name": "js",
        "progress":"95%"
    }
}
print(lang)
print(lang["two"]["name"])
