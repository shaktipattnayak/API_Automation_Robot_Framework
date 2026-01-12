*** Settings ***
Library    ../libraries/api_library.py
Library    Collections

*** Keywords ***
Create Posts Session
    No Operation

Get All Posts
    ${resp}=    Get Posts
    RETURN    ${resp}

Get Post By ID
    [Arguments]    ${id}
    ${resp}=    Get Post    ${id}
    RETURN    ${resp}
