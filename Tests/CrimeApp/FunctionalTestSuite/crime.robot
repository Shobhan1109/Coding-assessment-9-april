*** Settings ***
Resource  ../../../Resources/crimekeywords.robot

*** Test Cases ***
page load test case
    [Documentation]  Page loading
    [Tags]  crime
    open browser  ${url}  chrome
    maximize browser window

admin login test case
    [Documentation]  Admin logging
    [Tags]  crime


