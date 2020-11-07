from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create_g(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_index = old_groups.index(group)
    new_group = Group(name="New New Group")
    new_group.id = old_groups[group_index].id
    app.group.modify_group_by_id(group.id, new_group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups.remove(old_groups[group_index])
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#def test_modify_first_group_header(app):
    #if app.group.count() == 0:
        #app.group.create_g(Group(header="test"))
    #old_groups = app.group.get_group_list()
    #app.group.modify_first_group(Group(header="New Header"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)

