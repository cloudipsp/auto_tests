*** Settings ***
Documentation     A test suite containing tests related to recurring api transactions with token.
...               Card with 3ds.

Suite Setup       Open Browser For Empty Page
Suite Teardown    Close Browser
Default Tags      no3ds    approved
Test Template     Checkout With no3ds Should Pass
Resource          checkout_resources.robot



*** Variables ***
${specificatons}     PURCHASE_FIELDS_REDIRECT
${req_dict_step1}    request
${resp_dict_step1}   response
${url}            https://${API SERVER}/api/checkout/url/
${checkout_url}    ${EMPTY}

***Test Cases***      currency        merchant_id            message        content_type       credit_card
USD_JSON_Approved     USD             ${TestMerchant}       approved        ${JSON}          @{no3dsApproved}
USD_XML_Approved      USD             ${TestMerchant}       approved        ${XML}           @{no3dsApproved}
USD_FORM_Approved     USD             ${TestMerchant}       approved        ${FORM}          @{no3dsApproved}
UAH_JSON_Approved     UAH             ${TestMerchant}       approved        ${JSON}          @{no3dsApproved}
UAH_XML_Approved      UAH             ${TestMerchant}       approved        ${XML}           @{no3dsApproved}
UAH_FORM_Approved     UAH             ${TestMerchant}       approved        ${FORM}          @{no3dsApproved}
EUR_JSON_Approved     EUR             ${TestMerchant}       approved        ${JSON}          @{no3dsApproved}
EUR_XML_Approved      EUR             ${TestMerchant}       approved        ${XML}           @{no3dsApproved}
EUR_FORM_Approved     EUR             ${TestMerchant}       approved        ${FORM}          @{no3dsApproved}
RUB_JSON_Approved     RUB             ${TestMerchant}       approved        ${JSON}          @{no3dsApproved}
RUB_XML_Approved      RUB             ${TestMerchant}       approved        ${XML}           @{no3dsApproved}
RUB_FORM_Approved     RUB             ${TestMerchant}       approved        ${FORM}          @{no3dsApproved}
GBP_JSON_Approved     GBP             ${TestMerchant}       approved        ${JSON}          @{no3dsApproved}
GBP_XML_Approved      GBP             ${TestMerchant}       approved        ${XML}           @{no3dsApproved}
GBP_FORM_Approved     GBP             ${TestMerchant}       approved        ${FORM}          @{no3dsApproved}
*** Keywords ***
Checkout With no3ds Should Pass
    [Arguments]    ${currency}    ${merchant_id}    ${message}    ${content_type}    @{credit_card}
    Get and set checkout url  ${merchant_id}    ${currency}    ${specificatons}    ${req_dict_step1}    ${RESP_URL}    ${content_type}    ${url}    @{credit_card}
    Go to    ${checkout_url}
    Input and submit checkout    ${merchant_id}    @{credit_card}
    Response page should be displayed
    Check transaction status   ${message}