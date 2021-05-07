

class Tee(object):

    def __init__(self, *files):
        self.files = files

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        for f in self.files:
            f.close()

    def write(self, output):
        for f in self.files:
            f.write(output)

    def writelines(self, output):
        for f in self.files:
            f.writelines(output)