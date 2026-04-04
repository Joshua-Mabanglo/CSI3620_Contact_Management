import ContactNode

class ContactList:
    def __init__():
        head = None

    def insert(position, contact):
        currentPos = 1
        currentContact = head

        while(currentContact && position > currentPos):
            currentContact = head.next
            currentPos++

        if(position > currentPos && currentContact == None):
            return None

        new = contact

        if(position == 0):
            new.next = head
            currentContact.next = new
