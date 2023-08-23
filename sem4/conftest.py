import random
import string
from datetime import datetime
import yaml
import pytest
from sshcheckers import ssh_checkout,ssh_getout

with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folders():
    return ssh_checkout(data["host"], data["user"], "0000",
                        "mkdir {} {} {""} {}".format(data["folder_in"], data["folder_out"], data["folder_ext"],
                                                     data["folder_badarx"]),
                        "")


@pytest.fixture()
def clear_folders():
    return ssh_checkout(data["host"], data["user"], "0000",
                        "rm -rf {}/* {}/* {}/* {}/*".format(data["folder_in"], data["folder_out"], data["folder_ext"],
                                                            data["folder_badarx"]), "")


@pytest.fixture()
def make_files():
    list_off_files = []
    for i in range(data["count_files"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if ssh_checkout(data["host"], data["user"], "0000",
                        "cd {}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(data["folder_in"],
                                                                                               filename,
                                                                                               data["size_file"]),
                        ""):
            list_off_files.append(filename)
    return list_off_files


@pytest.fixture()
def make_subfolder():
    testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not ssh_checkout(data["host"], data["user"], "0000",
                        "cd {}; mkdir {}".format(data["folder_in"], subfoldername), ""):
        return None, None
    if not ssh_checkout(data["host"], data["user"], "0000",
                        "cd {}/{}; dd if=/dev/urandom of={} bs={} count=1 iflag=fullblock".format(data["folder_in"],
                                                                                                  subfoldername,
                                                                                                  testfilename), ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename


@pytest.fixture()
def make_badarx():
    ssh_checkout(data["host"], data["user"], "0000",
                 "cd {}; 7z a {}/badarx.7z".format(data["folder_in"], data["folder_badarx"]), "Everything is Ok")
    ssh_checkout(data["host"], data["user"], "0000",
                 "truncate -s 1 {}/badarx.7z".format(data["folder_badarx"]), "Everything is Ok")
    yield "badarx"
    ssh_checkout(data["host"], data["user"], "0000",
                 "rm -f {}/badarx.7z".format(data["folder_badarx"]), "")


@pytest.fixture()
def write_stat_log():
    ssh_checkout(data["host"], data["user"], "0000",'echo test_start: date: {},count_files:{}, size_files:{} >>{}/log.txt;'
                      'cat /home/user2/proc/loadavg >>{}/log.txt'.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                               data["count_files"], data["size_file"],
                                                               data["folder_log_user2"], data["folder_log_user2"]), "")

@pytest.fixture()
def start_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def save_log(start_time,name):
    ssh_getout(data["host"], data["user"], "0000","journalctl --since '{}' >>{}".format(start_time,name))
