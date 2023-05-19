
def read_config(config_file):
    d = dict()
    with open(config_file) as file:
        for line in file:
            (key, val) = line.split('=')
            d[key] = val.strip()

    return d
