from test_data import *

def json_search(key, input_object):
    ret_val = []
    if isinstance(input_object, dict): # Iterate dictionary
        for k, v in input_object.items(): # searching key in the dict
            if k == key:
                temp = {k: v}
                ret_val.append(temp)
            if isinstance(v, dict): # the value is another dict so repeat
                ret_val.extend(json_search(key, v)) # Sửa ở đây: gộp kết quả đệ quy vào ret_val
            elif isinstance(v, list): # it's a list
                for item in v:
                    if not isinstance(item, (str, int)): # if dict or list repeat
                        ret_val.extend(json_search(key, item)) # Sửa ở đây
    else: # Iterate a list because some APIs return JSON object in a list
        for val in input_object:
            if not isinstance(val, (str, int)):
                ret_val.extend(json_search(key, val)) # Sửa ở đây
    return ret_val

if __name__ == '__main__':
    print(json_search("issueSummary", data))
