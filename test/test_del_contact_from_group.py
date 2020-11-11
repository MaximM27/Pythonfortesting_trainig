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
