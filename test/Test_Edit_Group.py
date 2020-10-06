from model.group import Group

def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="group1", header="group2", footer="group3"))


