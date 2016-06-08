*** Settings ***
Documentation     Variables used in all tests. Imported one time in resource.robot

*** Variables ***
${API SERVER}               api.fondy.eu
${RESP_URL}                 https://${API SERVER}/test/responsepage/
${SERVER}                   fondy.eu
${BROWSER}                  FireFox
${JSON}                     application/json
${XML}                      application/xml
${FORM}                     application/x-www-form-urlencoded
