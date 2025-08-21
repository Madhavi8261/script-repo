*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://www.google.com
${BROWSER}    Chrome

*** Test Cases ***
Open Google Home Page
    [Documentation]    Open Google.com in Chrome browser
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    5s
    Close Browser
