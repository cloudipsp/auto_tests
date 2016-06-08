*** Settings ***
Documentation     A resource file with test credit cards. Imported once in resource.robot

*** Variables ***
#Name                   Card Number         Exp Month  Exp Year  Cvv2
@{3dsApproved}          4444555566661111    01         24        238
@{no3dsApproved}        4444555511116666    01         24        238
@{3dsDeclined}          4444111166665555    01         24        238
@{no3dsDeclined}        4444111155556666    01         24        238
