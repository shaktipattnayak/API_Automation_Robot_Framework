*** Settings ***
Suite Setup     Create Posts Session
Resource        ../resources/variables.resource
Resource        ../resources/keywords.resource

*** Test Cases ***
GET Invalid Post ID Returns 404
    [Documentation]    Validate GET /posts/{id} returns 404 for invalid ID
    ${res}=    Get Post By ID    99999
    Should Be Equal As Integers    ${res.status_code}    404
