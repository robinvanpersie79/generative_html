import subprocess


def css2stylus(filepath):
    return subprocess.getoutput(f"""stylus --css < {filepath} """)
