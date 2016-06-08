*** Settings ***
Documentation     A test suite containing tests related to recurring api transactions with token.
...               Card with 3ds.

Suite Setup       Open Browser For Empty Page
Suite Teardown    Close Browser
Default Tags      no3ds    declined
Test Template     Checkout With no3ds Should Fail
Resource          checkout_resources.robot



*** Variables ***
${specificatons}     PURCHASE_FIELDS_REDIRECT
${req_dict_step1}    request
${resp_dict_step1}   response
${url}            https://${API SERVER}/api/checkout/url/
${checkout_url}    ${EMPTY}

***Test Cases***      currency        merchant_id            message        content_type       credit_card
USD_JSON_Declined     USD             ${TestMerchant}       decline         ${JSON}          @{no3dsDeclined}
USD_XML_Declined      USD             ${TestMerchant}       decline         ${XML}           @{no3dsDeclined}
USD_FORM_Declined     USD             ${TestMerchant}       decline         ${FORM}          @{no3dsDeclined}
UAH_JSON_Declined     UAH             ${TestMerchant}       decline         ${JSON}          @{no3dsDeclined}
UAH_XML_Declined      UAH             ${TestMerchant}       decline         ${XML}           @{no3dsDeclined}
UAH_FORM_Declined     UAH             ${TestMerchant}       decline         ${FORM}          @{no3dsDeclined}
EUR_JSON_Declined     EUR             ${TestMerchant}       decline         ${JSON}          @{no3dsDeclined}
EUR_XML_Declined      EUR             ${TestMerchant}       decline         ${XML}           @{no3dsDeclined}
EUR_FORM_Declined     EUR             ${TestMerchant}       decline         ${FORM}          @{no3dsDeclined}
RUB_JSON_Declined     RUB             ${TestMerchant}       decline         ${JSON}          @{no3dsDeclined}
RUB_XML_Declined      RUB             ${TestMerchant}       decline         ${XML}           @{no3dsDeclined}
RUB_FORM_Declined     RUB             ${TestMerchant}       decline         ${FORM}          @{no3dsDeclined}
GBP_JSON_Declined     GBP             ${TestMerchant}       decline         ${JSON}          @{no3dsDeclined}
GBP_XML_Declined      GBP             ${TestMerchant}       decline         ${XML}           @{no3dsDeclined}
GBP_FORM_Declined     GBP             ${TestMerchant}       decline         ${FORM}          @{no3dsDeclined}
*** Keywords ***
Checkout With no3ds Should Fail
    [Arguments]    ${currency}    ${merchant_id}    ${message}    ${content_type}    @{credit_card}
    Get and set checkout url  ${merchant_id}    ${currency}    ${specificatons}    ${req_dict_step1}    ${RESP_URL}    ${content_type}    ${url}    @{credit_card}
    Go to    ${checkout_url}
    Input and submit checkout    ${merchant_id}    @{credit_card}
    Response page should be displayed
    Check transaction status   ${message}
