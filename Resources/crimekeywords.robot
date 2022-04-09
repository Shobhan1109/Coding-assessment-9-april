*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${url}  http://127.0.0.1:5000/


*** Keywords ***
admin login
    sleep  2s
    click element  xpath=/html/body/a[1]/center/button
    sleep  1s
    input text  name:uname  admin
    sleep  1s
    input text  name:upass  12345
    sleep  1s
    click button  xpath=/html/body/div/div/dic/form/table/tbody/tr[3]/td[2]/button
    sleep  2s

search data
    sleep  1s
    click element  xpath=/html/body/nav/div/div/ul/li[2]/a
    sleep  1s
    input text  name:date  11/09/2000
    sleep  1s
    click element  xpath=/html/body/div/div[1]/div/form/table/tbody/tr[3]/td[2]/button
    sleep  2s
user reg
    click element  xpath=/html/body/a[2]/center/button
    sleep  1s
    click element  xpath=/html/body/div/div/dic/form/a
    sleep  1s
    input text  name:name  user7
    input text  name:address  Bangalore
    input text  name:email  user7@mail.com
    input text  name:mobile  87496859685
    input text  name:pwd  12345
    input text  name:cfnpwd  12345
    sleep  2s
    click button  xpath=/html/body/div/div/dic/form/table/tbody/tr[8]/td[2]/button
    sleep  1s
    click element  xpath=/html/body/div/div/dic/form/a
    sleep  1s

user login
    input text  name:email  user7@mail.com
    sleep  1s
    input text  name:pass  12345
    sleep  1s
    click button  xpath=/html/body/div/div/dic/form/table/tbody/tr[3]/td[2]/button
    sleep  2s

user crimereg
    click element  xpath=/html/body/nav/div/div/ul/li[1]/a
    input text  name:description  Murder made up accident
    sleep  1s
    input text  name:remark  2 died
    sleep  1s
    click button  xpath=/html/body/div/div/dic/form/table/tbody/tr[4]/td[2]/button
    sleep  2s

edit profile
    click element  xpath=/html/body/nav/div/div/ul/li[2]/a
    sleep  1s
    input text  name:name  user1
    sleep  1s
    click button  xpath=/html/body/div/div/div/form/table/tbody/tr[3]/td[2]/button
    sleep  1s
    input text  name:name  user1
    input text  name:address  Mangalore
    input text  name:email  user1@mail.com
    input text  name:mobile  9685748596
    input text  name:pwd  12345
    input text  name:cfnpwd  12345
    sleep  1s
    click button  xpath=/html/body/div/div/dic/form/table/tbody/tr[8]/td[2]/button
    sleep  1s

guest reg
    click element  xpath=/html/body/a[3]/center/button
    sleep  1s
    input text  name:description  Cybercrime
    sleep  1s
    input text  name:remark  Demanding money
    sleep  2s
    click button  xpath=/html/body/div/div/dic/form/table/tbody/tr[4]/td[2]/button
    sleep  1s