from model.group import Group


def test_modify_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="New Group"))
    app.session.logout()


def test_modify_first_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header="New Header"))
    app.session.logout()
