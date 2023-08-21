from checkout import checkout_positive
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_step1(make_folders, clear_folders, make_files, write_stat_log):
    # test1
    res1 = checkout_positive(
        "cd {}; 7z a -t{} {}/arx1.{}".format(data["folder_in"], data["archive_type"], data["folder_out"],
                                             data["archive_type"]), "Everything is Ok"), "Test1 Fail"
    res2 = checkout_positive("ls {}".format(data["folder_out"]), "arx.{}".format(data["archive_type"])), "Test1 Fail"
    assert res1 and res2, "Test Fail"


def test_step2(clear_folders, make_files, write_stat_log):
    # test2
    res = []
    res.append(checkout_positive(
        "cd {}; 7z a -t{} {}/arx1.{}".format(data["folder_in"], data["archive_type"], data["folder_out"],
                                             data["archive_type"]), "Everything is Ok"))
    res.append(checkout_positive(
        "cd {}; 7z e arx1.{} -o{} -y".format(data["folder_out"], data["archive_type"], data["folder_ext"]),
        "Everything is Ok"))
    for item in make_files:
        res.append(checkout_positive("ls {}".format(data["folder_ext"]), item))
    assert all(res)


def test_step3(write_stat_log):
    # test3
    assert checkout_positive(
        "cd {}; 7z t -t{} {}/arx1.{}".format(data["folder_in"], data["archive_type"], data["folder_out"],
                                             data["archive_type"]), "Everything is Ok"), "Test3 Fail"


def test_step4(write_stat_log):
    # test4
    assert checkout_positive(
        "cd {}; 7z u -t{} {}/arx1.{}".format(data["folder_in"], data["archive_type"], data["folder_out"],
                                             data["archive_type"]), "Everything is Ok"), "Test4 Fail"


def test_step5(clear_folders, make_files, write_stat_log):
    # test5
    res = []
    res.append(checkout_positive(
        "cd {}; 7z a -t{} {}/arx1.{}".format(data["folder_in"], data["archive_type"], data["folder_out"],
                                             data["archive_type"]), "Everything is Ok"))
    for item in make_files:
        res.append(checkout_positive(
            "cd {}; 7z l -t{} arx1.{}".format(data["folder_out"], data["archive_type"], data["archive_type"]), item))
    assert all(res)


def test_step6(clear_folders, make_files, write_stat_log):
    res = []
    res.append(checkout_positive(
        "cd {}; 7z a -t{} {}/arx1.{}".format(data["folder_in"], data["archive_type"], data["folder_out"],
                                             data["archive_type"]), "Everything is Ok"))
    res.append(checkout_positive(
        "cd {}; 7z x -t{} arx1.{} -o{} -y".format(data["folder_out"], data["archive_type"], data["archive_type"],
                                                  data["folder_ext"]), "Everything is Ok"))

    for item in make_files:
        res.append(checkout_positive("ls {}".format(data["folder_ext"]), item))
    assert all(res)


def test_step7(write_stat_log):
    assert checkout_positive(
        "7z d -t{} {}/arx1.{}".format(data["archive_type"], data["folder_out"], data["archive_type"]),
        "Everything is Ok"), "Test7 Fail"
