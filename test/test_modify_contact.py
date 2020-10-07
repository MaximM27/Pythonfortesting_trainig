from model.contact import Contact


def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(firstname="New firstname"))


def test_modify_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(lastname="test"))
    app.contact.modify_first_contact(Contact(lastname="New lastname"))

