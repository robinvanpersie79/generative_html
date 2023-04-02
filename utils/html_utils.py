import os
import subprocess


def html2jade(filepath=None, html_text=None):
    if filepath:
        return subprocess.getoutput(f"""cat {filepath} | html2jade - """)

    else:
        fd, filepath = tempfile.mkstemp(suffix='.txt')
        try:
            with os.fdopen(fd, 'w') as tmp:
                tmp.write(str_)

            out = subprocess.getoutput(f"""cat {filepath} | html2jade -""")
        finally:
            os.remove(filepath)
        return out
