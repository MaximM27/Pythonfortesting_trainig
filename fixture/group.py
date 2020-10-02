class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        # return to group page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create_g(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit edition
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        # submit group edition
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def open_groups_page(self):
        # open groups page
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()