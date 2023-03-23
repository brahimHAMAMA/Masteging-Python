# Create Dictionary Here

mylangs = {
    "one":{
        "lang":"HTML",
        "prog":"90%"
    },
    "two":{
        "lang":"css",
        "prog":"80%"
    },
    "three":{
        "lang":"python",
        "prog":"30%"
    }
}

print(f'{mylangs["one"]["lang"]} Progress Is {mylangs["one"]["prog"]}')
print(f'{mylangs["two"]["lang"]} Progress Is {mylangs["two"]["prog"]}')
print(f'{mylangs["three"]["lang"]} Progress Is {mylangs["three"]["prog"]}')
mylangs.update({"four":{"lang":"AI","prog":"20%"}})
print(mylangs)
print(f'{mylangs["four"]["lang"]} Progress Is {mylangs["four"]["prog"]}')

# Needed Output
    # "HTML Progress Is 90%"
    # "CSS Progress Is 80%"
    # "Python Progress Is 30%"
    # "AI Progress Is 20%"