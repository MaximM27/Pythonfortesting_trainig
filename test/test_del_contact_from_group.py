from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_del_contact_from_group(app):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create_g(Group(name="test"))
    contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
    groups = sorted(db.get_group_list(), key=Group.id_or_max)
    for c in range(1, 2):
        for g in range(len(contacts)):
            c_list = db.get_contacts_in_group(Group(id=groups[g].id))
            if contacts[c] in c_list:
                app.group.select_group_by_id_in_addressbook_up(groups[g].id)
                app.contact.select_contact_by_id(contacts[c].id)
                app.group.remove_contact_by_id_from_group(groups[g].id)
                #assert lists from bd and from ui
                assert sorted(del_spaces_in_contact_data(db.get_contacts_in_group(Group(id=groups[g].id))), key=Contact.id_or_max) == \
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