
#   {{ file | cat_file }}
#

def cat_file(file):
    with open(file) as f:
        return f.read()


class FilterModule(object):
    def filters(self):
        return {'cat_file': cat_file}
