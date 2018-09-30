import json
import re
import time
from datetime import datetime
from urllib import request


__nr_server = "https://nr.nebulas.io/api/"


def __url(suffix):
    return __nr_server + suffix + "/"


def get_daily_all_nr(date):
    """
    Returns the nr value of all addresses in a day

    Args:
        date: Date in string format. For example: "20180601"

    Returns:
        A dict type result,
        For example:
        {
          'code': 0,
          'data': [{"in_outs": "0.000100", "out_val": "0.000000", "in_val": "0.000100", "degrees": "1", "score": "0.000000", "in_degree": "1", "weight": "0.000037", "median": "0.000000", "out_degree": "0", "address": "n1SQofkdzvyTMzFWBPAZbDMPGb9Vj6PeRst", "date": "20180601"}],
          'msg': ""
        }
        The code field is 0 for success,
        and the msg field indicates error message when an error occurs.
        The meaning of each field in data:
        {
          "in_outs": "0.000100",                             // transfer in-outs
          "out_val": "0.000000",                             // transfer out nas
          "in_val": "0.000100",                              // transfer in nas
          "degrees": "1",                                    // in-outs degrees
          "score": "0.000000",                               // nr score
          "in_degree": "1",                                  // in degree
          "weight": "0.000037",                              // in-outs weight
          "median": "0.000000",                              // median stake
          "out_degree": "0",                                 // out degree
          "address": "n1SQofkdzvyTMzFWBPAZbDMPGb9Vj6PeRst",  // main-net address
          "date": "20180601"                                 // date
        }
    """
    str_date = None
    if isinstance(date, str):
        if not re.match(r'^\d{8}$', date):
            return {"code": -1, "data": None, "msg": "Date format error."}
        str_date = date
    elif isinstance(date, datetime):
        str_date = date.strftime("%Y%m%d")
    elif isinstance(date, int) or isinstance(date, float):
        str_date = time.strftime("%Y%m%d", time.localtime(date))
    url = __url("daily_all_nr/" + str_date)
    try:
        req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        content = request.urlopen(req).read()
        return json.loads(content)
    except Exception as e:
        return {"code": -1, "data": None, "msg": repr(e)}
