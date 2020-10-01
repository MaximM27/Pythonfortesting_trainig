# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.add_contact(Contact(firstname="First name", middlename="Middle Name", lastname="Last Name"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login("admin", "secret")
    app.contact.add_contact(Contact(firstname="", middlename="", lastname=""))
    app.session.logout()


