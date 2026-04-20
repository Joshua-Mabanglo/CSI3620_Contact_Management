import Contact
import ContactHashTable

test = Contact.Contact("Matthew Nate", "111-222-3333", "MNate@gmail.com")
testTable = ContactHashTable.ContactHashTable()

def test_insert():
    # Insert Matthew into the table
    testTable.insert(test)

    # confirm that Matthew was added
    assert len(testTable.phone_table) == 1


def test_search_by_phone():
    # Empty the table object
    testTable = ContactHashTable.ContactHashTable()

    # Insert Matthew back into the table
    testTable.insert(test)

    # confirm that Matthew can be found by email
    assert testTable.search_by_phone("111-222-3333") == test


def test_search_by_email():
    # Empty the table object
    testTable = ContactHashTable.ContactHashTable()

    # Insert Matthew back into the table
    testTable.insert(test)

    # confirm that Matthew can be found by email
    assert testTable.search_by_email("MNate@gmail.com") == test


def test_delete():
    # Empty the table object
    testTable = ContactHashTable.ContactHashTable()

    # Insert Matthew back into the table, then delete
    testTable.insert(test)
    testTable.delete(test)

    # confirm that Matthew was deleted
    assert testTable.search_by_email("MNate@gmail.com") == None


