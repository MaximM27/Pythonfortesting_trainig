# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.add_contact(Contact(firstname="First name", middlename="Middle Name", lastname="Last Name"))


def test_add_empty_contact(app):
    app.contact.add_contact(Contact(firstname="", middlename="", lastname=""))



