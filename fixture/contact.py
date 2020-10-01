class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_contact(self, Contact):
        # add contact
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contact.lastname)
        wd.find_element_by_name("submit").click()
        self.app.return_to_home_page()

    def return_to_home_page(self):
        # retutn to home page
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()