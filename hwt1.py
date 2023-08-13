import subprocess
import string


def func_check(command: str, text: str) -> bool:
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout

    if result.returncode == 0:

        if text in out:
            return True
        else:
            return False
    else:
        print('FAIL CODE !=0')
        return False


# function with mode
def func_check_mode(command: str, text: str, mode: bool = False) -> bool:
    if not mode:
        func_check(command, text)
    else:

        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
        out = result.stdout

        if result.returncode == 0:
            for p in string.punctuation:
                if p in out:
                    out = out.replace(p, " ")

            if text in out:
                return True
            else:
                return False
        else:
            print('FAIL CODE !=0')
            return False


if __name__ == '__main__':
    print(func_check('ls', 'main'))
    print(func_check_mode('cat /etc/os-release', "Ubuntu", True))
