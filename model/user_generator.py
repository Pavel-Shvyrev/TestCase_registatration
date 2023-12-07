# -*- coding: utf-8 -*-

import random
import string
from model.user import User


def random_string_email():
    symbols_local_email = "".join(
        [random.choice(string.ascii_letters + string.digits) for i in range(random.randrange(2, 10))])
    symbols_local_domen_email = "".join(
        [random.choice(string.ascii_letters + string.digits) for i in range(random.randrange(2, 10))])
    symbols_global_domen_email = "".join(
        [random.choice(string.ascii_letters + string.digits) for i in range(random.randrange(2, 10))])
    return symbols_local_email + "@" + symbols_local_domen_email + "." + symbols_global_domen_email


def random_string_names():
    symbols_names = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    return "".join([random.choice(symbols_names) for i in range(random.randrange(2, 10))])


def random_string_phone():
    symbols_phone = string.digits
    return "".join([random.choice(symbols_phone) for i in range(10)])


testdata = [
    User(company_name=random_string_names(), user_name=random_string_names(), user_surname=random_string_names(),
         phone=random_string_phone(), email=random_string_email(), password="fhewpokjdsf3434343E!!") for i in range(1)
]
