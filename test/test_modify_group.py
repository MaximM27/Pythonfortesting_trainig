from model.group import Group


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create_g(Group(name="test"))
    app.group.modify_first_group(Group(name="New Group"))


def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create_g(Group(header="test"))
    app.group.modify_first_group(Group(header="New Header"))

