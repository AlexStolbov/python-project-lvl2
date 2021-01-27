import json


def generate_diff(file_original, file_changed):
    origin = load_file(file_original)
    modified = load_file(file_changed)
    origin_keys = list(origin.keys())
    modified_keys = list(modified.keys())
    all_keys = sorted(set(origin_keys + modified_keys))
    res = ['{']
    for key in all_keys:
        if key not in origin_keys:
            res.append('+ {}: {}'.format(key, modified[key]))
        elif key not in modified_keys:
            res.append('- {}: {}'.format(key, origin[key]))
        else:
            if origin[key] == modified[key]:
                res.append('  {}: {}'.format(key, origin[key]))
            else:
                res.append('- {}: {}'.format(key, origin[key]))
                res.append('+ {}: {}'.format(key, modified[key]))
    res.append('}')
    return '\n'.join(res)


def load_file(file_path):
    return json.load(open(file_path))
