# -*- coding: utf-8 -*-
import collections
import string
import urllib

import requests

from helper._settings import TEST_PARES
from helper.utils import randomStr, build_xml, build_signature
from helper import specifications_settings
from response import *


class requester(object):
    merchant_id = None
    request_params = {}
    order_id = ''
    md = ''
    acs_url = ''

    def build_required_parameters_dict(self, merchant_id, currency, spec, spec_dict, response_url=None, *args,
                                       **kwargs):
        self.merchant_id = merchant_id
        request_params_specs = getattr(
            specifications_settings, spec)[spec_dict]
        # for requests with cards
        if args:
            kwargs['card_number'] = args[0]
            kwargs['expiry_date'] = int(str(args[1]) + str(args[2]))
            kwargs['cvv2'] = args[3]
        request_params = {}
        for param in request_params_specs:
            if param in kwargs.iterkeys():
                request_params[param] = kwargs[param]
            elif param == "signature":
                request_params[param] = ''
            elif param == "currency":
                request_params[param] = currency
            elif param == "payment_systems":
                request_params[param] = 'card'
            elif param == "response_url":
                request_params[param] = response_url
            elif param == "merchant_id":
                request_params[param] = merchant_id
            elif param == "lifetime":
                request_params[param] = 60
            elif param == "delayed":
                request_params[param] = "n"
            elif param == "order_desc":
                request_params[param] = 'test' + randomStr(size=7, chars=string.digits)
            elif param == "order_id":
                request_params[param] = self.order_id
            # for 3ds requests
            elif param == "pares":
                request_params[param] = TEST_PARES
            elif param == "md":
                request_params[param] = self.md
            # any other parameters
            elif param == "server_callback_url":
                continue
            elif request_params_specs[param]["type"] == "string":
                request_params[param] = randomStr(
                    request_params_specs[param]["size"], param).encode('utf-8')
            elif request_params_specs[param]["type"] == "url":
                request_params[param] = "https://" + randomStr(
                    request_params_specs[param]["size"] - 12, param).encode('utf-8') + ".com"
            elif request_params_specs[param]["type"] == "int":
                request_params[param] = randomStr(request_params_specs[param]["size"], "",
                                                  string.digits)
            elif request_params_specs[param]["type"] == "amount":
                request_params[param] = randomStr(
                    5, "", string.digits)
            elif request_params_specs[param]["type"] == "boolean":
                request_params[param] = randomStr(
                    1, "", "YN")

        self.request_params = request_params

    def build_request(self, content_type, request_params):
        if content_type == 'application/xml':
            request_data = build_xml(request_params, 'request')
        elif content_type == 'application/json':
            request_data = json.dumps({'request': request_params})
        elif content_type == 'application/x-www-form-urlencoded':
            request_data = urllib.urlencode(request_params)

        return request_data

    def send_request(self, content_type, url=None, data=None, protocol=False, **kwargs):
        requests.packages.urllib3.disable_warnings()
        print "*HTML* sending request"
        print "*HTML* content_type=%r, url=%r, data=%r, kwargs=%r" % (content_type, url, data, kwargs)
        if data is None:
            data = self.request_params
        if self.order_id == '':
            data['order_id'] = 'test' + randomStr(
                10, "", string.ascii_letters)
        else:
            data['order_id'] = self.order_id

        data['signature'] = ""
        data['signature'] = build_signature(self.request_params)
        self.save_order_id_from_server(data['order_id'])
        post_data = self.build_request(content_type, data)
        print "*HTML* POSTREQUEST  %s" % (post_data)
        self.response = requests.post(
            url, headers={'Content-Type': content_type}, data=post_data, verify=False).text
        print "*HTML* POSTRESPONSE  %s" % (self.response)
        return self.response

    def verify_response_status(self, spec, spec_dict, content_type, response=None, request_params=None,
                               status='approved'):
        try:
            if response == None:
                response = self.response
            print "*HTML* response  %s" % (response)
            if request_params == None:
                if self.request_params:
                    request_params = self.request_params
            print "*HTML* REq_par  %s" % (request_params)
            response_params_specs = getattr(
                specifications_settings, spec)[spec_dict]
            print "*HTML* REsponse_par_spec  %s" % (response_params_specs)
            errors_list = []
            error = False
            response_params = parse_response(self.response, content_type)
            print "*HTML* REsp_par  %s" % (response_params)
            for param in response_params_specs:
                if response_params[param] is not None:
                    if response_params_specs[param]["type"] == "string":
                        if len(response_params[param]) > response_params_specs[param]["size"]:
                            errors_list.append('Error: size of param ' + param + ' is ' + str(
                                len(response_params[param])) + ' but max is ' + str(
                                response_params_specs[param]["size"]))
                            error = True
                    elif response_params_specs[param]["type"] == "int":
                        if len(str(response_params[param])) > response_params_specs[param]["size"]:
                            errors_list.append('Error: size of param ' + param + ' is ' + str(
                                len(str(response_params[param]))) + ' but max is ' + str(
                                response_params_specs[param]["size"]))
                            error = True
                        if response_params[param] != "" and not str(response_params[param]).isdigit():
                            errors_list.append(
                                'Error: param ' + param + ' is not integer')
                            error = True
                else:
                    errors_list.append('Error: param ' + param + ' is missing')
                    error = True
                if request_params.get(param) is not None and request_params.get(
                        param) != "" and param != 'signature' and response_params.get(param) is not None:
                    if (response_params_specs[param]["type"] == "string" and request_params.get(
                            param) != response_params.get(
                        param)) or (
                                    response_params_specs[param]["type"] == "amount" and int(
                                request_params.get(param)) != int(
                                response_params.get(param))):
                        request = 'request:' + str(request_params.get(param))
                        response = 'response:' + str(response_params.get(param))
                        order_id = 'order_id:' + \
                                   str(response_params.get('order_id'))
                        errors_list.append(
                            'Error: param ' + param + ' is not equal in request and '
                                                      'response\n request=%s\n response=%s order_id=%s' % (
                                request, response, order_id))
                        error = True

            if response_params_specs.get('signature') is not None:
                params_sign = {param: response_params.get(param, "") for param in response_params_specs if
                               param != 'signature'}
                params = collections.OrderedDict(sorted(response_params.items()))
                params_sign['signature'] = build_signature(params_sign)
                if params_sign['signature'] != params["signature"]:
                    errors_list.append('Error: signature invalid in response ')
                    error = True

            if response_params.get('order_status') and response_params.get('order_status') != status:
                errors_list.append('Error: invalid status in response ')
                error = True
        except Exception as e:
            errors_list.append("final %s" % e.message)
            error = True
        finally:
            if error:
                raise Exception("*HTML* Errors:\n %s" % errors_list)
            else:
                print "*HTML* test passed OK"

    def save_order_id_from_server(self, order_id):
        self.order_id = order_id
        print "*HTML* Order_id %s" % (self.order_id)

    def return_order_id(self):
        return self.order_id
        print "*HTML* Order_id %s" % (self.order_id)

    def clear_order_id(self):
        self.order_id = ''

    def save_md_pareq_and_acs_url_for_3ds(self, content_type):
        self.md = parse_response(self.response, content_type)['md']
        self.acs_url = parse_response(self.response, content_type)['acs_url']
        self.pareq = parse_response(self.response, content_type)['pareq']

    def return_checkout_url(self, content_type='application/json'):
        checkout_url = parse_response(
            self.response, content_type)['checkout_url']
        return checkout_url
