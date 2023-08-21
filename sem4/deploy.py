from sshcheckers import upload_files,ssh_checkout
def deploy():
    res = []
    upload_files("0.0.0.0", "user2", "0000", "/home/user/p7zip-full.deb", "/home/user2/p7zip-full.deb")
    res.append(ssh_checkout("0.0.0.0", "user2", "0000", "echo '0000' | sudo -S dpkg -i /home/user2/p7zip-full.deb",
                            "Настраивается пакет"))
    res.append(ssh_checkout("0.0.0.0", "user2", "0000", "echo '0000' | sudo -S dpkg -s p7zip-full",
                            "Status: install ok installed"))
    return all(res)

if deploy():
    print("Деплой  успешен")
else:
    print("Деплой не успешен")

