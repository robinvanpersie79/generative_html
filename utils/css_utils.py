import os
import subprocess


def css2stylus(filepath=None, html_text=None):
    if filepath:
        return subprocess.getoutput(f"""stylus --css < {filepath} """)

    else:
        fd, filepath = tempfile.mkstemp(suffix='.txt')
        try:
            with os.fdopen(fd, 'w') as tmp:
                tmp.write(str_)

            out = subprocess.getoutput(f"""stylus --css < {filepath} """)
        finally:
            os.remove(filepath)
        return out
