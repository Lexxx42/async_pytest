""" Fake DB. """
# TODO: create actual db here!

user1 = {
    "data": {
        "id": 1,
        "email": "hello_w@gmail.com",
        "first_name": "Lexx",
        "last_name": "Friedman",
        "avatar": "https://reqres.in/img/faces/1-image.jpg"
    },
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "Do a barrel roll!"
    }
}

user_2 = {
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}

USER_INFO_DB = {1: user1, 2: user_2}
