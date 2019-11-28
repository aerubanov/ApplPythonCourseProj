import wolframalpha
from tokens import WOLFRAM_API_TOKEN
import pickle

client = wolframalpha.Client(WOLFRAM_API_TOKEN)


class WolfQueryException(Exception):
    pass


def api_query(query_string):
    res = client.query(query_string)
    # ----- for debug ------------------------------------
    # with open('wolfram_resp_exmp.obj', 'rb') as f:
    #    res = pickle.load(f)
    # ----------------------------------------------------
    if res['@success'] == 'false':
        raise WolfQueryException(f'Wolfram response @success == false on query {query_string}')
    text = '\n'.join(['%s:: %s' % (key, value) for (key, value) in res.details.items()])
    img_urls = [item['img']['@src'] for item in res['pod'][1]['subpod']]
    return text, img_urls
