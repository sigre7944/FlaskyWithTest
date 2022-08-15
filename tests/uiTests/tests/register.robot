*** Settings ***
Documentation   This file contains tests for the registering workflow.
Resource  ../resources/common.robot
Test Setup  Begin Web Test
Test Teardown  End Web Test

*** Test Cases ***
Register through web portal
    [Documentation]     Tests that UI user can register through web portal.
    ${RANDOM_TEXT} =    Generate Random String    9    [LETTERS]
    Register New User From Frontpage    ${RANDOM_TEXT}

    Login From Front Page   ${RANDOM_TEXT}    ${RANDOM_TEXT}
    Wait Until Page Contains        User Information
