*** Settings ***
Suite Setup     Create Posts Session
Resource        ../../resources/variables.resource
Resource        ../../resources/keywords.resource

*** Test Cases ***
GET All Posts Should Return 200
    [Documentation]    Validate GET /posts returns HTTP 200
    ${res}=    Get All Posts
    Should Be Equal As Integers    ${res.status_code}    200

Validate Posts Schema
    [Documentation]    Validate the Posts response schema
    ${res}=    Get All Posts
    ${body}=    Get Posts Json
    ${first}=    Get From List    ${body}    0
    Validate Json Schema    ${first}    ${POSTS_SCHEMA}
