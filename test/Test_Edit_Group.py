from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="group1", header="group2", footer="group3"))
    app.session.logout()

