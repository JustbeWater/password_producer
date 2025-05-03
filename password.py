import itertools
import threading

def generate_passwords(lengths:list, charset):
    # 传入存储多个长度的列表和使用的字符集
    # 生成指定长度和字符集的所有可能密码，使用生成器逐个生成
    for length in lengths:
        for combination in itertools.product(charset, repeat=length):
            yield ''.join(combination)

def generate_and_save(lengths, charset, filename='passwords.txt'):
    password_generator = generate_passwords(lengths, charset)
    # 将密码生成器生成的密码逐个写入文件
    with open(filename, 'w') as file:
        for password in password_generator:
            file.write(f"{password}\n")
    print(f"密码列表已保存到 {filename}.")

def start_in_back(lengths, charset, filename='password.txt'):
    # 在后台线程中启动密码生成
    threading.Thread(target=generate_and_save, args=(lengths, charset, filename), daemon=True).start()