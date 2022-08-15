*** Settings ***
Documentation   This file contains tests for the log-in workflow.
Resource  ../resources/common.robot
Test Setup  Begin Web Test
Test Teardown  End Web Test


*** Test Cases ***
Access "User Information" Page
    [Documentation]    Tests that users can view own information after logging in.
    ${RANDOM_TEXT} =    Generate Random String    9    [LETTERS]
    Register New User From Frontpage    ${RANDOM_TEXT}

    Login From Front Page     ${RANDOM_TEXT}    ${RANDOM_TEXT}
    Wait Until Page Contains        User Information
    Element Should Contain    //td[@id='username']    ${RANDOM_TEXT}
    Element Should Contain    //td[@id='firstname']    ${RANDOM_TEXT}
    Element Should Contain    //td[@id='lastname']     ${RANDOM_TEXT}
    Element Should Contain    //td[@id='phone']    ${RANDOM_TEXT}
