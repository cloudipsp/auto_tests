*** Settings ***
Documentation     A resource file with reusable keywords.

Resource          variables.robot
Resource          cards.robot
Resource          merchants.robot
Resource          ui_repository.robot
Library           Selenium2Library
Library           helper/utils.py
Library           requester.py

*** Keywords ***
Open Browser For Empty Page
    [Arguments]
    Open Browser    about:blank
    Maximize Browser Window