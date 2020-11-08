import re
from model.contact import Contact


def test_contact_data_on_home_page(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_data_base = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contact_from_home_page)):
        for j in range(len(contact_from_data_base)):
            if i == j:
                assert contact_from_home_page[i].firstname == del_spaces(contact_from_data_base[j].firstname)
                assert contact_from_home_page[i].lastname == del_spaces(contact_from_data_base[j].lastname)
                assert contact_from_home_page[i].address == del_spaces(contact_from_data_base[j].address)
                assert contact_from_home_page[i].all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_data_base[j])
                assert contact_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_data_base[j])

#def test_contact_data_on_home_page(app, db):
    #contacts_count = db.get_contact_list()
   #index = randrange(len(contacts_count))
    #contact_from_home_page = app.contact.get_contact_list()[index]
    #contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    #assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    #assert contact_from_home_page.lastname == contact_from_edit_page.lastname
   #assert contact_from_home_page.address == contact_from_edit_page.address
    #assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    #assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def del_spaces(s):
    s = s.rstrip(" ")
    s = s.lstrip(" ")
    s = s.replace("  ", " ")
    s = s.replace('\r\n', '\n')
    return s



def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone,
                                        contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))


def contact_name_like_on_home_page(contact):
    return list(map(lambda x: del_spaces(x), contact))


#def contact_lastname_like_on_home_page(contact):
    #return list(map(lambda x: del_spaces(x), contact.lastname))


#def contact_address_like_on_home_page(contact):
    #return list(map(lambda x: del_spaces(x), contact.address))

