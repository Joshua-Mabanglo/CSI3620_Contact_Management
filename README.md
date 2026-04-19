# Contact Management System

CSI 3620 - Data Structures and Algorithms
Josh Mabanglo, Anthony Rurka, and Tessa Rachelle Esman

## Overview:

This project implements a Contact Management System that allows users to store, search, update, and manage contact information efficiently.

The system supports:
Adding contacts
Deleting contacts
Updating contact information
Searching by name, phone number, or email
Displaying contacts in alphabetical order

## Data Structures Used

    Binary Search Tree (BST)
        - Stores contacts sorted by name
        - Enables efficient alphabetical ordering
        - Supports
            - Insert
            - Search by name
            - Delete
            - In-order traversal (sorted display)
    Hash Tables
        - Implemented using Python dictionaries
        - Provides fast lookup by:
            - Phone number
            - Email address
        - Enables near constant-time search: O(1)
    CSV File Storage
        - Used for persistent storage of contacts
        - Ensures data is retained between program runs
        - Supports:
            - Initial load on startup
            - Append on add/update
            - Full rewrite on delete/update

## Features:

    Add Contact: Stores contact in
        - BST (for sorting)
        - Hash table (for fast lookup)
        - CSV file (for persistence)
    Delete Contact: Removes contact from
        - BST
        - Hash table
        - CSV file (via file rewrite)
    Update Contact:
        - Implemented using a delete + reinsert strategy
        - Ensures consistency across all data structures
        - Updates:
            - BST
            - Hash table
            - CSV file
    Search Contacts:
        - By name useing BST (O(log n) average)
        - By phone/email using hash table (O(1))
    Display Sorted Contacts
        - Uses BST in-order traversal
        - Outputs contacts in alphabetical order

## Design Decisions

- BST was chosen to maintain automatic alphabetical sorting without needing separate sorting algorithms
- Hash tables were used to optimize search performance for phone and email lookups
- CSV storage provides a simple and effective persistence layer
- Update implemented as delete + reinsert to maintain structural integrity across all systems

## How to Run:

1. Ensure all project files are in the same directory:
   - Main.py
   - Contact.py
   - ContactBST.py
   - ContactHashTable.py
   - Contacts.csv
   - ContactNode.py
   - ContactList.py
2. Run the program in VS Code terminal with bash command: python Main.py
3. Use the menu to interact with the system.

# Testing Notes:

-
-
-

## Work Distribution by member:

Joshua Mabanglo: - - -

Anthony Rurka:
Hash Table (Search Functionality)
Designed and implemented the hash table module in ContactHashTable.py
Built the insert logic using phone number and email as keys
Added search functions to look up contacts by:
Phone number
Email
Set up the structure so contacts can be found directly instead of looping through everything
Used hashing to make searching faster and more efficient

System Integration Work
Connected the hash table into the main program (Main.py)
Made sure every new contact gets added into the hash table when it’s created
Added menu options so users can search by phone or email
Hooked up the search functions to user input so results display right away
Kept the hash table updated during normal program use

Data Consistency & Coordination
Worked on keeping the hash table in sync with the rest of the system
Made sure contacts are stored properly when they’re added
Planned for syncing deletes and updates with the BST and linked list
Helped keep the data consistent across different structures

Algorithm & Design Contributions
Used hashing to store and retrieve data more efficiently
Focused on improving search speed compared to basic list searching
Set up the structure so it works well alongside the BST
Helped with overall design decisions around how data should be handled

Application Behavior Improvements
Added search functionality to make the program more useful
Improved the menu by adding clear search options
Made it so users get results instantly when searching


Tessa Rachelle Esman

- Binary Search Tree
  - Designed and implemented the BST module in ContactBST.py
  - Developed BST insertion logic using alphabetical comparison of contact names
  - Implemented in-order traversal to display contacts in sored (alphabetical) order
  - Built BST search functionality for efficient lookup by contact name
  - Implemented full BST delete operation, handling:
    - Leaf nodes
    - Nodes with one child
    - Nodes with two children (inorder successor replacement)
  - Designed and implemented BST-based sorting system without relying on built-in sorting functions
- System Integration work
  - Integrated BST into the main application workflow (Main.py)
  - Ensured all new contacts are inserted into the BST during runtime
  - Connected BST display functionality to a user-driven menu option
  - Implemented BST search option in the user interface
  - Integrated BST delete functionality with the main program flow
- Data Consistency & Coordination
  - Coordinated BST operations with other system components to maintain consistency
  - Ensure contacts removed from BST are also removed from:
    - Hash Table
    - CSV storage
  - Helped implement the update feature using BST delete + reinsert strategy
- Algorithm & Design Contributions
  - Applied recursive algorithms for BST operations (insert, search, delete, traversal)
  - Designed system to maintain O(log n) average-case performance for name-based operations
  - Ensured case-sensitive comparisons for consistent sorting and searching
  - Contributed to overall data structure selection and system design decisions
- Application Behavior Improvements
  - Helped transition program from a single-run script to a loop-based interactive application
  - Improved output formatting for BST dispay to ensure readability
  - Refined menu structure and user flow

## Summary:

This project demonstrates the use of multiple data structures working together to create an efficient and functional application. It shows:

- Algorithm efficiency
- Data structure integration
- Persistent storage handling
- Modular program design
