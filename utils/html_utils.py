import subprocess


def html2jade(filepath):
    return subprocess.getoutput(f"""cat {filepath} | html2jade - """)
