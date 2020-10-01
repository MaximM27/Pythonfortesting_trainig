from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.edit_first_contact(Contact(firstname="First name22", middlename="Middle Name22", lastname="Last Name22"))
    app.session.logout()
