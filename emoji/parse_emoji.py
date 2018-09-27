
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
            continue
        elif line.startswith('# subgroup: '):
            subgroup = line[12:]
        elif line.startswith('#'):
            continue
        elif "non-fully-qualified" in line:
            continue
        elif line:
            code = line.split(';')[0].rstrip()
            sbgrp = codepoints.get(subgroup, [])
            codepoints[subgroup] = sbgrp

            codepoint = "".join([chr(int(c, 16)) for c in code.split(" ")])

            description = line.split('#')[1].strip().split()[1:]
            name = " ".join(description)

            sbgrp.append((codepoint, name))

    print(codepoints)

    with open(path + "emoji-test.json", "wt") as f:
        json.dump(codepoints, f, ensure_ascii=False)


if __name__ == "__main__":
    parse_file()
