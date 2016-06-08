# -*- coding: utf-8 -*-
import json
import xml.etree.ElementTree as ET
from urlparse import parse_qs

from helper.utils import etree_to_dict


def parse_response(response_params, content_type):
    if content_type == 'application/json':
        response_params = json.loads(response_params)['response']
    elif content_type == 'application/xml':
        response_params = etree_to_dict(ET.XML(response_params))['response']
    elif content_type == 'application/x-www-form-urlencoded':
        body = parse_qs(response_params, 1)
        response_params = {}
        for k, v in body.items():
            response_params[k] = v[0]
    return response_params
