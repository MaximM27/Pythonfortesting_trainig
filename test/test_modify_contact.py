from model.contact import Contact


def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    cont = Contact(firstname="New firstname")
    cont.id = old_contacts[0].id
    cont.firstname = old_contacts[0].firstname
    cont.lastname = old_contacts[0].lastname
    cont.middlename = old_contacts[0].middlename
    app.contact.modify_first_contact(cont)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = cont
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_first_contact_lastname(app):
 #   if app.contact.count() == 0:
 #       app.contact.add_contact(Contact(lastname="test"))
 #   old_contacts = app.contact.get_contact_list()
 #   app.contact.modify_first_contact(Contact(lastname="New lastname"))
  #  new_contacts = app.contact.get_contact_list()
 #   assert len(old_contacts) == len(new_contacts)

