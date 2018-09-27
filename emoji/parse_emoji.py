
import json
import os


path = os.path.dirname(__file__) + "/"


def line_generator():
    with open(path + 'emoji-test.txt', 'rt') as f:
        return f.readlines()


def parse_file():
    codepoints = {}

    group = "Unknown"
    subgroup = "Unknown"

    for line in line_generator():
        line = line.strip()

        if line.startswith('# group: '):
            group = line[9:]
        elif line.startswith('# subgroup: '):
            subgroup = line[12:]
        elif line.startswith('#'):
            continue
        elif "non-fully-qualified" in line:
            continue
        elif line:
            code = line.split(';')[0].rstrip()
            grp = codepoints.get(group, {})
            codepoints[group] = grp
            sbgrp = grp.get(subgroup, [])
            codepoints[group][subgroup] = sbgrp

            codepoint = "".join([chr(int(c, 16)) for c in code.split(" ")])
            sbgrp.append(codepoint)
    #print(codepoints)

    for g in codepoints.keys():
        for sg in codepoints[g].keys():
            print("{:20}{}".format(g, sg))

    with open(path + "emoji-test.json", "wt") as f:
        json.dump(codepoints, f)


if __name__ == "__main__":
    parse_file()
