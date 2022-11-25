import subprocess

nome_rede = str(input('Insira o nome da rede: '))
allData = subprocess.check_output(
    ["netsh", "wlan", "show", "profiles"],
    encoding="cp860")

data = subprocess.check_output(
    ["netsh", "wlan", "show", "profile", nome_rede, "key", "=", "clear"],
    encoding="cp860")
print(allData)

for row in data.split("\n"):
    if "Conteúdo da Chave" in row:
        pos = row.find(":")
        senha = row[pos+2:]
        print("A senha desta rede é: ", senha)