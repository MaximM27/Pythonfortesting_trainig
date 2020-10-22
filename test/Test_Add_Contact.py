# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(maxlen):
    symbols = string.ascii_letters + " "*5
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="",
                    lastname="")] + [Contact(firstname=random_string(5), middlename=random_string(10),
                    lastname=random_string(10)) for i in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




