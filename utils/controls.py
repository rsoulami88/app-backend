def find_in_request(obj, values):
    keys = list(obj.keys())
    for value in values:
        if value not in keys:
            return False
    return True
