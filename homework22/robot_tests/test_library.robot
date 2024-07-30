*** Settings ***
Library           homework22/robot_resources/library_keywords.py
Library           BuiltIn
Library           OperatingSystem

*** Test Cases ***
Test Take Book Positive
    [Documentation]    Test that a user can successfully take a book.
    ${book}=    Create Book    Learning Python    134527    1200    Mark Lutz
    ${user}=    Create User    user_id_1
    ${result}=    Take Book    ${user}    134527
    Log Message    Testing book take: expected ${result} to be True
    Should Be True    ${result}    Failed to take the book with ISBN 134527
    ${is_taken}=    Check If Book In Taken Books    ${book}    134527
    Should Be True    ${is_taken}    Book with ISBN 134527 should be in taken books
    Log Message    Successfully verified user can take book with ISBN 134527

Test Take Book Already Taken
    [Documentation]    Test that a user cannot take a book that is already taken.
    ${book}=    Create Book    Learning Python    134527    1200    Mark Lutz
    ${user1}=    Create User    user_id_1
    ${user2}=    Create User    user_id_2
    Take Book    ${user1}    134527
    ${result}=    Take Book    ${user2}    134527
    Log Message    Testing book take: expected ${result} to be False
    Should Be Equal As Strings    ${result}    False    Failed to prevent User 2 from taking the book with ISBN 134527 already taken by User 1
    Log Message    Successfully verified user cannot take already taken book with ISBN 134527

Test Reserve Book Positive
    [Documentation]    Test that a user can successfully reserve a book.
    ${book}=    Create Book    Learn Python 3    234569    1000    Zed A. Shaw
    ${user}=    Create User    user_id_1
    ${result}=    Reserve Book    ${user}    234569
    Log Message    Testing book reserve: expected ${result} to be True
    Should Be True    ${result}    Failed to reserve the book with ISBN 234569
    ${is_reserved}=    Check If Book In Reserved Books    ${book}    234569
    Should Be True    ${is_reserved}    Book with ISBN 234569 should be in reserved books
    Log Message    Successfully verified user can reserve book with ISBN 234569

Test Release Book Positive
    [Documentation]    Test that a user can successfully release a reserved book.
    ${book}=    Create Book    Think Python    239874    900    Allen Downey
    ${user}=    Create User    user_id_1
    Reserve Book    ${user}    239874
    ${result}=    Release Book    ${user}    239874
    Log Message    Testing book release: expected ${result} to be True
    Should Be True    ${result}    Failed to release the reserved book with ISBN 239874
    ${is_reserved}=    Check If Book In Reserved Books    ${book}    239874
    Should Be Equal As Strings    ${is_reserved}    False    Book with ISBN 239874 should not be in reserved books
    Log Message    Successfully verified user can release reserved book with ISBN 239874

Test Return Book Positive
    [Documentation]    Test that a user can successfully return a book.
    ${book}=    Create Book    Think Python    239874    900    Allen Downey
    ${user}=    Create User    user_id_1
    Take Book    ${user}    239874
    ${result}=    Return Book    ${user}    239874
    Log Message    Testing book return: expected ${result} to be True
    Should Be True    ${result}    Failed to return the book with ISBN 239874
    ${is_taken}=    Check If Book In Taken Books    ${book}    239874
    Should Be Equal As Strings    ${is_taken}    False    Book with ISBN 239874 should not be in taken books
    Log Message    Successfully verified user can return book with ISBN 239874

Test Invalid Book Operations
    [Documentation]    Test that a user cannot perform operations on a non-existent book.
    ${user}=    Create User    user_id_1
    ${result}=    Take Book    ${user}    111111
    Log Message    Testing invalid book take: expected ${result} to be False
    Should Be Equal As Strings    ${result}    False    Failed to prevent taking non-existent book with ISBN 111111
    ${result}=    Reserve Book    ${user}    111111
    Log Message    Testing invalid book reserve: expected ${result} to be False
    Should Be Equal As Strings    ${result}    False    Failed to prevent reserving non-existent book with ISBN 111111
    ${result}=    Return Book    ${user}    111111
    Log Message    Testing invalid book return: expected ${result} to be False
    Should Be Equal As Strings    ${result}    False    Failed to prevent returning non-existent book with ISBN 111111
    ${result}=    Release Book    ${user}    111111
    Log Message    Testing invalid book release: expected ${result} to be False
    Should Be Equal As Strings    ${result}    False    Failed to prevent releasing non-existent book with ISBN 111111
    Log Message    Successfully verified invalid book operations
