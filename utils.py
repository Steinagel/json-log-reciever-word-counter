import json
import itertools

def ListLines(file, range_json, prop='r'):
    new_lines = []
    count = 0
    with open(file, prop) as text_file:
        data = []
        lines = text_file.readlines(  )
        max = len(lines)

        with open(range_json) as json_file:
            data = json.load(json_file)
        for x, line in enumerate(itertools.islice(lines, data["current"], max)):
            new_lines.append(line)
            count = x

        data["current"] = max if (data["current"]>=max) else data["current"]+count+1
        with open(range_json, 'w') as json_file:
            json.dump(data, json_file)

    return ((len(new_lines)>0), new_lines)
