# -*- coding: utf-8 -*-
import collections
import hashlib
import random
import string
import xml.etree.ElementTree as ET

str_conv = lambda obj, encoding='utf-8': obj.encode(encoding) if isinstance(obj, unicode) else str(obj)


def unicode_convert(value, encoding='utf-8'):
    if isinstance(value, str):
        return value.decode(encoding)
    if not isinstance(value, basestring):
        return unicode(value)
    return value


concat = lambda seq, separator=u'': unicode_convert(separator).join(unicode_convert(x) for x in seq if x is not None)


def dict_strip(d):
    if not isinstance(d, dict):
        return d
    for k, v in d.items():
        if isinstance(v, dict):
            d[k] = dict_strip(v)
        elif isinstance(v, str) or isinstance(v, unicode):
            d[k] = v.strip()
    return d


def unicode_convert_dict(dict_value, modify=False, only_strings=False, encoding='utf-8'):
    def _recursively_convert(val):
        dict_val = {}
        if isinstance(val, dict):
            dict_val = val.items()
        elif isinstance(val, list):
            dict_val = enumerate(val)
        for k, v in dict_val:
            if isinstance(v, (dict, list)):
                _recursively_convert(v)
            else:
                if only_strings:
                    if isinstance(v, str):
                        val[k] = unicode_convert(v, encoding)
                else:
                    val[k] = unicode_convert(v, encoding)

    if modify:
        _dict = dict_value
    else:
        import copy

        _dict = copy.deepcopy(dict_value)

    _recursively_convert(_dict)
    if not modify:
        return _dict


def str_convert_dict(dict_value, modify=False, only_strings=False, encoding='utf-8'):
    def _recursively_convert(val):
        dict_val = {}
        if isinstance(val, dict):
            dict_val = val.items()
        elif isinstance(val, list):
            dict_val = enumerate(val)
        for k, v in dict_val:
            if isinstance(v, (dict, list)):
                _recursively_convert(v)
            else:
                if only_strings:
                    if isinstance(v, str):
                        val[k] = str_conv(v, encoding)
                else:
                    val[k] = str_conv(v, encoding)

    if modify:
        _dict = dict_value
    else:
        import copy

        _dict = copy.deepcopy(dict_value)

    _recursively_convert(_dict)
    if not modify:
        return _dict


def randomStr(size=24, start_chars=None, chars=string.letters + string.digits):
    chars = unicode_convert(chars)
    _start_chars = ''

    if isinstance(start_chars, basestring):
        start_chars = unicode_convert(start_chars)

        if len(start_chars) < size:
            _start_chars = start_chars
    return _start_chars + ''.join(random.choice(chars) for i in xrange(size - len(_start_chars)))


def build_signature(params):
    params = collections.OrderedDict(sorted(params.items()))
    signature_str = 'test'.encode('utf8')
    for param in params:
        if params[param] != "" and param is not None:
            signature_str = signature_str + "|" + \
                            unicode_convert(params[param])
    return hashlib.sha1(str_conv(signature_str)).hexdigest()


def build_xml(request_params, type):
    post_data = ET.Element(type)
    for k, v in request_params.items():
        if v is None:
            v = ""
        if ET.iselement(v):
            post_data.append(v)
        elif isinstance(v, str):
            ET.SubElement(post_data, k).text = unicode_convert(v)
        elif isinstance(v, int):
            ET.SubElement(post_data, k).text = str(v)
        else:
            ET.SubElement(post_data, k).text = v
    post_data = ('<?xml version="1.0" encoding="UTF-8"?>\n%s' %
                 ET.tostring(post_data))
    return post_data


def etree_to_dict(t):
    d = {t.tag: {} if t.attrib else ""}
    children = list(t)
    if children:
        dd = collections.defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.iteritems():
                dd[k].append(v)
        d = {t.tag: {k: v[0] if len(v) == 1 else v for k, v in dd.iteritems()}}
    if t.attrib:
        d[t.tag].update(('@' + k, v) for k, v in t.attrib.iteritems())
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
                d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d
