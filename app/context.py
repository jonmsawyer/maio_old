import maio

def pre_populate_context_dict(cd={}):
    if not isinstance(cd, dict):
        cd = {}
    cd['VERSION'] = maio.VERSION
    return cd

def post_populate_context_dict(cd={}):
    if not isinstance(cd, dict):
        cd = {}
    return cd

