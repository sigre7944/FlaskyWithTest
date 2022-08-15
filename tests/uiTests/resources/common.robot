*** Settings ***
Library  SeleniumLibrary
Library  String

*** Variables ***
${BROWSER} =  chrome
${WEBSITE} =  http://10.0.0.7:8080/

*** Keywords ***
Begin Web Test
    Open Browser  ${WEBSITE}  ${BROWSER}

End Web Test
    Close All Browsers

Register New User From Frontpage
    [Arguments]    ${SIGNUP_TEXT}
    Click Link    link:Register
    Wait Until Page Contains Element    //input[@value='Register']
    Input Text      //input[@id='username']     ${SIGNUP_TEXT}
    Input Text      //input[@id='password']     ${SIGNUP_TEXT}
    Input Text      //input[@id='firstname']     ${SIGNUP_TEXT}
    Input Text      //input[@id='lastname']     ${SIGNUP_TEXT}
    Input Text      //input[@id='phone']     ${SIGNUP_TEXT}
    Click Button    Register

Login From Front Page
    [Arguments]     ${USERNAME}    ${PASSWORD}
    Click Link    link:Log In
    Wait Until Page Contains Element    //input[@value='Log In']
    Input Text      //input[@id='username']     ${USERNAME}
    Input Text      //input[@id='password']     ${PASSWORD}
    Click Button    Log In
