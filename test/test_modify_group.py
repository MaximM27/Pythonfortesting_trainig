from model.group import Group
import random


def test_modify_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create_g(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group_data = Group(name="New New Group")
    app.group.modify_group_by_id(group.id, new_group_data)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_first_group_header(app):
    #if app.group.count() == 0:
        #app.group.create_g(Group(header="test"))
    #old_groups = app.group.get_group_list()
    #app.group.modify_first_group(Group(header="New Header"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)

