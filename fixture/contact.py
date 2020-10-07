class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_contact(self, Contact):
        # add contact
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(Contact)
        wd.find_element_by_name("submit").click()
        self.app.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first_contact(self, Contact):
        wd = self.app.wd
        self.select_edit_contact()
        self.fill_contact_form(Contact)
        self.select_update_contact()
        self.app.return_to_home_page()

    def select_update_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def select_edit_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//img[@alt='Edit'])").click()

    def return_to_home_page(self):
        # retutn to home page
        wd = self.app.wd
        if not(wd.current_url_endswith("addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home page").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, Contact):
        wd = self.app.wd
        self.change_field_value("firstname", Contact.firstname)
        self.change_field_value("middlename", Contact.middlename)
        self.change_field_value("lastname", Contact.lastname)

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        self.select_edit_contact()
        self.fill_contact_form(new_contact_data)
        self.select_update_contact()
        self.app.return_to_home_page()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))



