# -*- coding: utf-8 -*-


class User:

    def __init__(self, company_name=None, user_name=None, user_surname=None, phone=None, email=None, password=None):
        self.company_name = company_name
        self.name = user_name
        self.user_surname = user_surname
        self.phone = phone
        self.email = email
        self.password = password

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (
            self.company_name, self.name, self.user_surname, self.phone, self.email, self.password)
