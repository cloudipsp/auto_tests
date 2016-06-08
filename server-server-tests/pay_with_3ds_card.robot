*** Settings ***
Documentation     A test suite containing tests related to server-server complete purchase with 3ds card.

Test Template     Server-server full purchase with 3ds card Should Pass
Test Timeout      15 seconds
Default Tags      smoke    3ds
Resource          ../resource.robot

*** Variables ***
${specificatons}        PAY_SERVER2SERVER_3DS
${req_dict_step1}       request_step1
${resp_dict_step1}      response_3ds
${url_step1}            https://${API SERVER}/api/3dsecure_step1/
${req_dict_step2}       request_step2
${resp_dict_step2}      response_final
${url_step2}            https://${API SERVER}/api/3dsecure_step2/

***Test Cases ***        merchant_id           currency    content_type    credit_card
USD_JSON_Approved        ${TestMerchant}       USD         ${JSON}         @{3dsApproved}
USD_XML_Approved         ${TestMerchant}       USD         ${XML}          @{3dsApproved}
USD_FORM_Approved        ${TestMerchant}       USD         ${FORM}         @{3dsApproved}
UAH_JSON_Approved        ${TestMerchant}       UAH         ${JSON}         @{3dsApproved}
UAH_XML_Approved         ${TestMerchant}       UAH         ${XML}          @{3dsApproved}
UAH_FORM_Approved        ${TestMerchant}       UAH         ${FORM}         @{3dsApproved}
EUR_JSON_Approved        ${TestMerchant}       EUR         ${JSON}         @{3dsApproved}
EUR_XML_Approved         ${TestMerchant}       EUR         ${XML}          @{3dsApproved}
EUR_FORM_Approved        ${TestMerchant}       EUR         ${FORM}         @{3dsApproved}
RUB_JSON_Approved        ${TestMerchant}       RUB         ${JSON}         @{3dsApproved}
RUB_XML_Approved         ${TestMerchant}       RUB         ${XML}          @{3dsApproved}
RUB_FORM_Approved        ${TestMerchant}       RUB         ${FORM}         @{3dsApproved}
GBP_JSON_Approved        ${TestMerchant}       GBP         ${JSON}         @{3dsApproved}
GBP_XML_Approved         ${TestMerchant}       GBP         ${XML}          @{3dsApproved}
GBP_FORM_Approved        ${TestMerchant}       GBP         ${FORM}         @{3dsApproved}

*** Keywords ***
Server-server full purchase with 3ds card Should Pass
    [Arguments]    ${merchant_id}    ${currency}    ${content_type}    @{credit_card}
    Build required parameters dict    ${merchant_id}    ${currency}    ${specificatons}    ${req_dict_step1}    ${RESP_URL}  @{credit_card}
    Send request    ${content_type}    ${url_step1}
    Verify response status    ${specificatons}    ${resp_dict_step1}    ${content_type}
    Save md pareq and acs url for 3ds    ${content_type}
    Build required parameters dict    ${merchant_id}    ${currency}    ${specificatons}    ${req_dict_step2}    ${RESP_URL}
    Send request    ${content_type}    ${url_step2}
    Verify response status    ${specificatons}    ${resp_dict_step2}    ${content_type}
