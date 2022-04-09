*** Settings ***
Resource  ../../../Resources/crimekeywords.robot

*** Test Cases ***
page load test case
    [Documentation]  Page loading
    [Tags]  crime
    open browser  ${url}  chrome
    maximize browser window

#admin login test case
#    [Documentation]  Admin logging
#    [Tags]  crime
#    admin login
#
#search test case
#    [Documentation]  Searching crime
#    [Tags]  crime
#    search data
#
#admin logout test case
#    [Documentation]  admin logging out
#    [Tags]  crime
#    click element  xpath=/html/body/nav/div/div/ul/li[3]/a
#    sleep  1s

user register test case
    [Documentation]  User register
    [Tags]  crime
    user reg

user login test case
    [Documentation]  User logging in
    [Tags]  crime
    user login

user crime reg test case
    [Documentation]  User complaining crime
    [Tags]  crime
    user crimereg

user edit profile test case
    [Documentation]  User editing profile
    [Tags]  crime
    edit profile

user logout test case
    [Documentation]  User logging out
    [Tags]  crime
    click element  xpath=/html/body/nav/div/div/ul/li[3]/a
    sleep  2s

guest reg test case
    [Documentation]  Guest reg
    [Tags]  crime
    guest reg

guest exit test case
    [Documentation]  Guest exiting
    [Tags]  crime
    click element  xpath=/html/body/nav/div/div/ul/li[2]/a
    sleep  2s
    close browser