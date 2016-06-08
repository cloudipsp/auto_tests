*** Settings ***
Documentation     A resource file with reusable keywords and variables.

Resource          ../resource.robot

*** Keywords ***

Confirm 3ds
    [Arguments]    ${merchant_id}
    Wait until element is visible    ${3DS_SUBMIT_BUTTON}
    Click element     ${3DS_SUBMIT_BUTTON}

Checkout page should be opened
    Wait until element is visible    ${CARD_NUMBER_FIELD}    timeout=30.0

Check transaction status
    [Arguments]    ${message}
    Wait until element is visible    ${ORDER_STATUS}    timeout=30.0
    Element should contain    ${ORDER_STATUS}    ${message}

Get and set checkout url
    [Arguments]    ${merchant_id}    ${currency}    ${specificatons}    ${req_dict_step1}    ${RESP_URL}    ${content_type}    ${url}    @{credit_card}
    Build required parameters dict    ${merchant_id}    ${currency}    ${specificatons}    ${req_dict_step1}    ${RESP_URL}  @{credit_card}
    Send request    ${content_type}    ${url}
    ${url} =    Return checkout url    ${content_type}
    Set test variable    ${checkout_url}    ${url}

Response page should be displayed
    Wait until element is visible    ${TABLE_RESPONSE}    timeout=30.0

Input and submit checkout
    [Arguments]    ${merchant_id}    @{credit_card}
    Checkout page should be opened
    Click element   ${CARD_NUMBER}
    Clear element text   ${CARD_NUMBER_FIELD}
    Input text    ${CARD_NUMBER_FIELD}    @{credit_card}[0]
    Select from list    ${EXPIRE_MONTH}    by value          @{credit_card}[1]
    Select from list    ${EXPIRE_YEAR}    by value           @{credit_card}[2]
    Input text    ${CVV2}                                    @{credit_card}[3]
    Click button    ${CHECKOUT_BUTTON}








