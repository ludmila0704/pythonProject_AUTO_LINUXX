import subprocess

out = "/home/user/out"


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def checkout_negative(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    if (text in result.stdout or text in result.stderr) and result.returncode != 0:
        return True
    else:
        return False


def get_crc32(dir: str):
    res2_crc = subprocess.run("crc32 {}/arx2.7z".format(dir), shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if res2_crc.returncode == 0:
        return res2_crc.stdout[-1]
    else:
        return None
