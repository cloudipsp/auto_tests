*** Settings ***
Documentation     A test suite containing tests related to recurring api transactions with token.
...               Card with 3ds.

Suite Setup       Open Browser For Empty Page
Suite Teardown    Close Browser
Default Tags      3ds    approved
Test Template     Checkout With 3ds Should Pass
Resource          checkout_resources.robot



*** Variables ***
${specificatons}     PURCHASE_FIELDS_REDIRECT
${req_dict_step1}    request
${resp_dict_step1}   response
${url}               https://${API SERVER}/api/checkout/url/
${checkout_url}      ${EMPTY}

***Test Cases***      currency        merchant_id            message        content_type       credit_card
USD_JSON_Approved     USD             ${TestMerchant}       approved        ${JSON}          @{3dsApproved}
USD_XML_Approved      USD             ${TestMerchant}       approved        ${XML}           @{3dsApproved}
USD_FORM_Approved     USD             ${TestMerchant}       approved        ${FORM}          @{3dsApproved}
UAH_JSON_Approved     UAH             ${TestMerchant}       approved        ${JSON}          @{3dsApproved}
UAH_XML_Approved      UAH             ${TestMerchant}       approved        ${XML}           @{3dsApproved}
UAH_FORM_Approved     UAH             ${TestMerchant}       approved        ${FORM}          @{3dsApproved}
EUR_JSON_Approved     EUR             ${TestMerchant}       approved        ${JSON}          @{3dsApproved}
EUR_XML_Approved      EUR             ${TestMerchant}       approved        ${XML}           @{3dsApproved}
EUR_FORM_Approved     EUR             ${TestMerchant}       approved        ${FORM}          @{3dsApproved}
RUB_JSON_Approved     RUB             ${TestMerchant}       approved        ${JSON}          @{3dsApproved}
RUB_XML_Approved      RUB             ${TestMerchant}       approved        ${XML}           @{3dsApproved}
RUB_FORM_Approved     RUB             ${TestMerchant}       approved        ${FORM}          @{3dsApproved}
GBP_JSON_Approved     GBP             ${TestMerchant}       approved        ${JSON}          @{3dsApproved}
GBP_XML_Approved      GBP             ${TestMerchant}       approved        ${XML}           @{3dsApproved}
GBP_FORM_Approved     GBP             ${TestMerchant}       approved        ${FORM}          @{3dsApproved}
*** Keywords ***
Checkout With 3ds Should Pass
    [Arguments]    ${currency}    ${merchant_id}    ${message}    ${content_type}    @{credit_card}
    Get and set checkout url  ${merchant_id}    ${currency}    ${specificatons}    ${req_dict_step1}    ${RESP_URL}    ${content_type}    ${url}    @{credit_card}
    Go to    ${checkout_url}
    Input and submit checkout    ${merchant_id}    @{credit_card}
    Confirm 3ds    ${merchant_id}
    Response page should be displayed
    Check transaction status   ${message}
