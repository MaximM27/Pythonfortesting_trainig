from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture
import random


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_in_group(app):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create_g(Group(name="test"))
    contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
    groups = sorted(db.get_group_list(), key=Group.id_or_max)
    c_list = []
    for c in range(len(contacts)):
        #get group list for each contact
        g_list = db.get_not_groups_of_contact(Contact(id=contacts[c].id))
        if len(g_list) != 0:
            #if contact is in all groups it added's to new list
            c_list.append(Contact(lastname=contacts[c].lastname, firstname=contacts[c].firstname, id=contacts[c].id))
    if len(c_list) == 0:
        app.contact.add_contact(Contact(firstname="new added contact"))
        c_list = db.get_contact_list()
        rand_contact = random.choice(c_list)
        rand_group = random.choice(groups)
        app.group.get_contact_list_from_all_groups()
        app.contact.select_contact_by_id(rand_contact.id)
        app.group.add_contact_by_id_to_group(rand_group.id)
        assert sorted(del_spaces_in_contact_data(db.get_contacts_in_group(Group(id=rand_group.id))),
                      key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list_from_group_page(), key=Contact.id_or_max)
    else:
        rand_contact = random.choice(c_list)
        group_list = db.get_not_groups_of_contact(Contact(id=rand_contact.id))
        rand_group = random.choice(group_list)
        app.group.get_contact_list_from_all_groups()
        app.contact.select_contact_by_id(rand_contact.id)
        app.group.add_contact_by_id_to_group(rand_group.id)
        assert sorted(del_spaces_in_contact_data(db.get_contacts_in_group(Group(id=rand_group.id))),
                      key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list_from_group_page(), key=Contact.id_or_max)


def del_spaces(s):
    s = s.rstrip(" ")
    s = s.lstrip(" ")
    s = s.replace("  ", " ")
    return s


def del_spaces_in_contact_data(contact_list):
    contact_list_correct = []
    for c in contact_list:
        id = c.id
        firstname = del_spaces(c.firstname)
        lastname = del_spaces(c.lastname)
        contact_list_correct.append(Contact(id=id, firstname=firstname, lastname=lastname))
    return list(contact_list_correct)


#def add_contact_to_group(app, contact, group):
 #   app.group.get_contact_list_from_all_groups()
  #  app.contact.select_contact_by_id(contact.id)
   # app.group.add_contact_by_id_to_group(group.id)
