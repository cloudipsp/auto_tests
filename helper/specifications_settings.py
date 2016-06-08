# -*- coding: utf-8 -*-

PAY_SERVER2SERVER_3DS = {
    'request_step1': {
        "order_id": {
            "required": True,
            "type": "string",
            "size": 1024
        },
        "merchant_id": {
            "required": True,
            "type": "int",
            "size": 12
        },
        "order_desc": {
            "required": True,
            "type": "string",
            "size": 1024
        },
        "signature": {
            "required": True,
            "type": "string",
            "size": 40
        },
        "amount": {
            "required": True,
            "type": "amount",
            "size": 12
        },
        "currency": {
            "required": True,
            "type": "string",
            "size": 3
        },
        "version": {
            "default": "1.0",
            "required": False,
            "type": "string",
            "size": 10
        },
        "server_callback_url": {
            "required": False,
            "type": "url",
            "size": 2048
        },
        "lifetime": {
            "required": False,
            "type": "int",
            "size": 6
        },
        "merchant_data": {
            "required": False,
            "type": "string",
            "size": 2048
        },
        "preauth": {
            "default": False,
            "type": "boolean",
            "required": False
        },
        "sender_email": {
            "required": False,
            "type": "email",
            "size": 50
        },
        "lang": {
            "required": False,
            "type": "string",
            "size": 2
        },
        "product_id": {
            "required": False,
            "type": "string",
            "size": 1024
        },
        "verification": {
            "default": False,
            "type": "boolean",
            "required": False
        },
        "card_number": {
            "required": True,
            "type": "string",
            "size": 19
        },
        "cvv2": {
            "required": True,
            "type": "string",
            "size": 3
        },
        "expiry_date": {
            "required": True,
            "type": "date",
            "size": 4
        },
        "client_ip": {
            "required": True,
            "type": "string",
            "size": 15
        },
    },
    'request_step2': {
        "order_id": {
            "required": True,
            "type": "string",
            "size": 1024
        },
        "merchant_id": {
            "required": True,
            "type": "int",
            "size": 12
        },
        "pares": {
            "required": True,
            "type": "string",
            "size": 20480
        },
        "md": {
            "required": True,
            "type": "string",
            "size": 1024
        },
        "version": {
            "default": "1.0",
            "required": False,
            "type": "string",
            "size": 10
        },
        "signature": {
            "required": True,
            "type": "string",
            "size": 40
        },
    },
    'response_3ds': {
        "response_status": {
            "type": "string",
            "required": True,
            "size": 50
        },
        "acs_url": {
            "type": "string",
            "required": True,
            "size": 2048
        },
        "pareq": {
            "type": "string",
            "required": True,
            "size": 20480
        },
        "md": {
            "default": "",
            "type": "string",
            "required": True,
            "description_en": "",
            "description_ru": "",
            "size": 1024
        },
    },
    'response_final': {
        "order_id": {
            "type": "string",
            "size": 1024
        },
        "merchant_id": {
            "type": "int",
            "size": 12
        },
        "amount": {
            "type": "amount",
            "size": 12
        },
        "currency": {
            "type": "string",
            "size": 3
        },
        "order_status": {
            "type": "string",
            "size": 50
        },
        "response_status": {
            "type": "string",
            "size": 50
        },
        "signature": {
            "type": "string",
            "size": 40
        },
        "tran_type": {
            "type": "string",
            "size": 50
        },
        "sender_cell_phone": {
            "type": "string",
            "size": 20
        },
        "sender_account": {
            "type": "string",
            "size": 50
        },
        "masked_card": {
            "type": "string",
            "size": 19
        },
        "card_bin": {
            "type": "int",
            "size": 6
        },
        "card_type": {
            "type": "string",
            "size": 50
        },
        "rrn": {
            "type": "string",
            "size": 50
        },
        "approval_code": {
            "type": "string",
            "size": 6
        },
        "response_code": {
            "type": "int",
            "size": 4
        },
        "response_description": {
            "type": "string",
            "size": 1024
        },
        "reversal_amount": {
            "type": "amount",
            "size": 12
        },
        "settlement_amount": {
            "type": "amount",
            "size": 12
        },
        "settlement_currency": {
            "type": "string",
            "size": 3
        },
        "order_time": {
            "type": "time",
            "size": 19
        },
        "settlement_date": {
            "type": "time",
            "size": 10
        },
        "eci": {
            "type": "string",
            "size": 2
        },
        "fee": {
            "type": "amount",
            "size": 12
        },
        "payment_system": {
            "type": "string",
            "size": 50
        },
        "sender_email": {
            "type": "email",
            "size": 254
        },
        "payment_id": {
            "type": "int",
            "size": 19
        },
        "actual_amount": {
            "type": "amount",
            "size": 12
        },
        "actual_currency": {
            "type": "string",
            "size": 3
        },
        "product_id": {
            "type": "string",
            "size": 1024
        },
        "merchant_data": {
            "type": "string",
            "size": 2048,
        },
        "verification_status": {
            "type": "string",
            "size": 48,
        },
        "rectoken": {
            "type": "string",
            "size": 48,
        },
        "rectoken_lifetime": {
            "type": "time",
            "size": 19,
        },
    },
}

PURCHASE_FIELDS_REDIRECT = {
    "request": {
        "order_id": {
            "type": "string",
            "required": True,
            "size": 1024
        },
        "merchant_id": {
            "type": "int",
            "required": True,
            "size": 12
        },
        "order_desc": {
            "type": "string",
            "required": True,
            "size": 1024
        },
        "signature": {
            "type": "string",
            "required": True,
            "size": 40
        },
        "amount": {
            "type": "amount",
            "required": True,
            "size": 12
        },
        "currency": {
            "type": "string",
            "required": True,
            "size": 3
        },
        "version": {
            "default": "1.0",
            "type": "string",
            "required": False,
            "size": 10
        },
        "response_url": {
            "type": "url",
            "required": False,
            "size": 2048
        },
        "server_callback_url": {
            "type": "url",
            "required": False,
            "size": 2048
        },
        "payment_systems": {
            "type": "string",
            "required": False,
            "size": 1024
        },
        "default_payment_system": {
            "type": "string",
            "required": False,
            "size": 25
        },
        "lifetime": {
            "default": "36000",
            "type": "int",
            "required": False,
            "size": 6
        },
        "merchant_data": {
            "type": "string",
            "required": False,
            "size": 2048
        },
        "preauth": {
            "default": False,
            "type": "boolean",
            "required": False
        },
        "sender_email": {
            "type": "string",
            "required": False,
            "size": 50
        },
        "delayed": {
            "default": True,
            "type": "boolean",
            "required": False
        },
        "lang": {
            "type": "string",
            "required": False,
            "size": 2
        },
        "product_id": {
            "type": "string",
            "required": False,
            "size": 1024
        },
        "required_rectoken": {
            "default": False,
            "type": "boolean",
            "required": False
        },
        "verification": {
            "default": False,
            "type": "boolean",
            "required": False
        },
        "verification_type": {
            "default": "amount",
            "type": "string",
            "required": False,
            "size": 25
        },
        "rectoken": {
            "type": "string",
            "required": False,
            "size": 40
        },
        "design_id": {
            "type": "string",
            "required": False,
            "size": 6
        },
        "subscription": {
            "default": False,
            "type": "boolean",
            "required": False
        },
        "subscription_callback_url": {
            "type": "url",
            "required": False,
            "size": 2048
        }
    },
    "response": PAY_SERVER2SERVER_3DS['response_final'],
}
