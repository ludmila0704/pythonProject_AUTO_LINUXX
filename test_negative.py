from checker import checkout_negative

tst = "/home/user/tst"
out = "/home/user/out"
folder = "/home/user/folder1"
badarx = "/home/user/badarx"


def test_step1():
    # в tst лежат test1 test2

    assert checkout_negative("cd {}; 7z e arx2.7z -o{} -y".format(badarx, folder), "ERRORS"), 'test1 FAIL'


def test_step2():
    # test3 #
    # проверяем целпстность архива
    assert checkout_negative("cd {}; 7z t arx2.7z".format(badarx), "ERRORS"), 'test2 FAIL'
