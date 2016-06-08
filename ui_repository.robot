*** Settings ***
Documentation     Variables used in all tests. Imported one time in resource.txt

*** Variables ***
# Checkout page
${CHECKOUT_BUTTON}                                       css=.btn-lime
${CVV2}                                                  id=cvv2
${EXPIRE_YEAR}                                           id=expire_year
${EXPIRE_MONTH}                                          id=expire_month
${CARD_NUMBER}                                           name=card_number
${CARD_NUMBER_FIELD}                                     id=credit_card_number
${3DS_SUBMIT_BUTTON}                                     xpath=//button[@type='submit']

#Response page
${ORDER_STATUS}                                          css=.field_order_status .value
${TABLE_RESPONSE}                                        id=table_response

