*** Settings ***
Library    app.py

*** Test Cases ***
Login Should Succeed With Valid Credentials
    ${result}=    login    admin    password123
    Should Be True    ${result}

Login Should Fail With Wrong Username
    ${result}=    login    wrong    password123
    Should Be False    ${result}

Login Should Fail With Wrong Password
    ${result}=    login    admin    wrongpass
    Should Be False    ${result}

Login Should Fail With Empty Credentials
    ${result}=    login    ${EMPTY}    ${EMPTY}
    Should Be False    ${result}
