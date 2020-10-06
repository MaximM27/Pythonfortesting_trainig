# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create_g(Group(name="groupgroup", header="groupgroup", footer="groupgroup"))


def test_add_empty_group(app):
    app.group.create_g(Group(name="", header="", footer=""))

