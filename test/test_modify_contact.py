from model.contact import Contact
import random


def test_modify_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    cont = random.choice(old_contacts)
    cont_index = old_contacts.index(cont)
    new_contact = Contact(firstname="New firstname")
    new_contact.id = old_contacts[cont_index].id
    new_contact.firstname = old_contacts[cont_index].firstname
    new_contact.lastname = old_contacts[cont_index].lastname
    new_contact.middlename = old_contacts[cont_index].middlename
    app.contact.modify_contact_by_id(new_contact.id, new_contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts.remove(cont)
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

#def test_modify_first_contact_lastname(app):
 #   if app.contact.count() == 0:
 #       app.contact.add_contact(Contact(lastname="test"))
 #   old_contacts = app.contact.get_contact_list()
 #   app.contact.modify_first_contact(Contact(lastname="New lastname"))
  #  new_contacts = app.contact.get_contact_list()
 #   assert len(old_contacts) == len(new_contacts)

