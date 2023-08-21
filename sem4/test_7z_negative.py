from checkout import checkout_negative
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_step1(clear_folders, make_files, make_badarx,write_stat_log):
    # test1
    assert checkout_negative("cd {}; 7z e -t{} badarx.{} -o{} -y".format(data["folder_out"], data["archive_type"], data["archive_type"],data["folder_ext"]),
                             "ERROR"), "Test1 neg Fail"


def test_step2(write_stat_log):
    # test2
    assert checkout_negative("cd {}; 7z t badarx.7z".format(data["folder_out"]), "ERROR"), "Test2 neg Fail"

def test_step3(make_folders, clear_folders, make_files,write_stat_log):

    # test created not exist type archive
    res1 = checkout_negative("cd {}; 7z a  -t {}/arx1.{}".format(data["folder_in"], data["archive_nega_type"],data["folder_out"],data["archive_nega_type"]), "Everything is Ok"), "Test3 Fail"
    res2 = checkout_negative("ls {}".format(data["folder_out"]), "arx.{}".format(data["archive_nega_type"])), "Test3 nega Fail"
    assert res1 and res2, "Test Fail"