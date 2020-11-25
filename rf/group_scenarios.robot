*** Settings ***
Library  rf.AddressBook.Address
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new group
    Create Group  name1 header1 footer1
