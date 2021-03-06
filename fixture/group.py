from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        # return to group page
        wd = self.app.wd
        if not(wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
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
        self.group_cache = None

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        self.select_edit_group()
        self.fill_group_form(group)
        self.select_update_group()
        self.return_to_groups_page()

    def select_update_group(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def select_edit_group(self):
        wd = self.app.wd
        wd.find_element_by_name("edit").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        self.select_edit_group()
        self.fill_group_form(new_group_data)
        self.select_update_group()
        self.return_to_groups_page()
        self.group_cache = None

    def open_groups_page(self):
        # open groups page
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        # select group by index
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        self.select_edit_group()
        self.fill_group_form(new_group_data)
        self.select_update_group()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_group_by_id(self, id, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        self.select_edit_group()
        self.fill_group_form(new_group_data)
        self.select_update_group()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        # select group by index
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def add_contact_by_id_to_group(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//select[@name='to_group']//option[@value='%s']" % id).click()
        wd.find_element_by_css_selector("input[value='Add to']").click()
        wd.find_element_by_css_selector("a[href='./?group=%s']" % id).click()

    def select_group_by_id_in_addressbook_up(self, id):
        wd = self.app.wd
        wd.find_element_by_name("group")
        wd.find_element_by_css_selector("option[value='%s']" % id).click()

    def get_contact_list_from_all_groups(self):
        wd = self.app.wd
        wd.find_element_by_name("group").click()
        wd.find_element_by_xpath("//option[text()= '[all]']").click()

    def remove_contact_by_id_from_group(self, id):
        wd = self.app.wd
        wd.find_element_by_name("remove").click()
        wd.find_element_by_css_selector("a[href='./?group=%s']" % id).click()