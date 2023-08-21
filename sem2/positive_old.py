from checker import checkout
from checker import get_crc32

tst = "/home/user/tst"
out = "/home/user/out"
folder = "/home/user/folder1"
folder2 = "/home/user/folder2"


def test_step1():
    # в tst лежат test1 test2
    # создаем архив и проверяем наличие
    res1 = checkout("cd {}; 7z a {}/arx2".format(tst, out), "Everything is Ok")
    res2 = checkout("ls {}".format(out), "arx2.7z")
    assert res1 and res2, 'test1 FAIL'


def test_step2():
    # test2
    # разахивирукм архив в folder1
    res1 = checkout("cd {}; 7z e arx2.7z -o{} -y".format(out, folder), "Everything is Ok")
    res2 = checkout("ls {}".format(folder), "test1")
    res3 = checkout("ls {}".format(folder), "test2")
    assert res1 and res2 and res3, 'test2 FAIL'


def test_step3():
    # test3 #
    # проверяем целпстность архива
    assert checkout("cd {}; 7z t arx2.7z".format(out), "Everything is Ok"), 'test3 FAIL'


def test_step4():
    # test4
    # проверяем возможность обновить архив
    assert checkout("cd {}; 7z u {}/arx2.7z".format(tst, out), "Everything is Ok"), 'test4 FAIL'


def test_step6():
    # в tst test1 test2

    res1 = checkout("cd {}; 7z l arx2.7z".format(out), "test1")
    res2 = checkout("cd {}; 7z l arx2.7z".format(out), "test2")
    assert res1 and res2, 'test6 FAIL'


def test_step7():
    #
    # проверить с ключом x
    res1 = checkout("cd {}; 7z x arx2.7z -o{} -y".format(out, folder2), "Everything is Ok")
    res2 = checkout("ls {}".format(folder2), "test1")
    res3 = checkout("ls {}".format(folder2), "test2")
    assert res1 and res2 and res3, 'test2 FAIL'


def test_step8():
    # test
    # проверить тест команды расчета хеша
    assert checkout("7z h {}/arx2.7z".format(out), get_crc32(out)), 'test8 FAIL'


def test_step5():
    # test5
    # удаляем содержимое архива
    assert checkout("cd {}; 7z d arx2".format(out), "Everything is Ok")

