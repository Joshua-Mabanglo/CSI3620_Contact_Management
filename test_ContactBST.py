import Contact
import ContactBST

test = Contact.Contact("Matthew Nate", "111-222-3333", "MNate@gmail.com")
test2 = Contact.Contact("Alex Strong", "000-111-2222", "AStrong@gmail.com")
test3 = Contact.Contact("Chris Farmer", "123-456-7890", "CFarmer@gmail.com")
testBST = ContactBST.ContactBST()


def test_insert():
    # insert Matthew contact into BST
    testBST.insert(test)
    testRoot = testBST.root

    # confirm the Matthew contact is the root of the tree 
    # (since it's the first contact to be added)
    assert testRoot.contact == test


def test__insert_right():

    # add Matthew back into the tree
    testBST.insert(test)

    # insert another contact (Alex) into BST
    # (lower than the root contact)
    testBST._insert(testBST.root, test2)
    testRoot = testBST.root

    # confirm Matthew is the new right child 
    # of Alex (since Matthew > Alex alphabetically)
    assert testRoot.right.contact == test


def test__insert_left():
    # add Matthew and Alex back into the tree
    testBST.insert(test)
    testBST.insert(test2)

    # insert another contact (Chris) into BST
    # (higher than the root contact)
    testBST._insert(testBST.root, test3)
    testRoot = testBST.root

    # confirm Alex is the new lext child 
    # of Chris (since Alex < Chris alphabetically)
    assert testRoot.left.contact == test2


def test_search_found():
    # add Matthew, Alex, and Chris back into the tree
    testBST.insert(test)
    testBST.insert(test2)
    testBST.insert(test3)

    # confirm Matthew contact is found and returned
    assert testBST.search("Matthew Nate") == test


testBST.display_sorted()

def test_search_not_found():
    # add Matthew, Alex, and Chris back into the tree
    testBST.insert(test)
    testBST.insert(test2)
    testBST.insert(test3)


    # confirm Harry contact returns nothing
    assert testBST.search("Harry Style") == None


def test_delete():
    # Empty the BST
    testBST = ContactBST.ContactBST()
    
    # add Matthew and Alex back into the tree
    testBST.insert(test)
    testBST.insert(test2)

    # Delete Matthew
    testBST.delete("Matthew Nate")

    # confirm Matthew is deleted
    testBST.search("Matthew Nate") == None








    