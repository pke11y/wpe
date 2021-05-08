from pathlib import Path
import hashlib
import string

class DirFileHash(object):

    def __init__(self, dirname):
        self.dirname = dirname

    def __getitem__(self, filename):
        filepath = Path(self.dirname) / filename
        if Path(self.dirname).is_dir() and filepath.exists():
            m = hashlib.md5()
            content = getattr(string, filename).encode()
            m.update(content)
            return m.hexdigest()
        return None



