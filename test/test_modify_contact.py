from model.contact import Contact
from random import randrange


def test_modify_contact(app, db):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    cont = Contact(firstname="New firstname")
    cont.id = old_contacts[index].id
    cont.firstname = old_contacts[index].firstname
    cont.lastname = old_contacts[index].lastname
    cont.middlename = old_contacts[index].middlename
    app.contact.modify_contact_by_index(index, cont)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = cont
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_first_contact_lastname(app):
 #   if app.contact.count() == 0:
 #       app.contact.add_contact(Contact(lastname="test"))
 #   old_contacts = app.contact.get_contact_list()
 #   app.contact.modify_first_contact(Contact(lastname="New lastname"))
  #  new_contacts = app.contact.get_contact_list()
 #   assert len(old_contacts) == len(new_contacts)

