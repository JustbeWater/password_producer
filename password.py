import itertools
import threading
from UI import Log_Listbox
from tkinter import END

# 根据位数生成密码
def generate_passwords(lengths:list, charset):
    # 传入存储多个长度的列表和使用的字符集
    # 生成指定长度和字符集的所有可能密码，使用生成器逐个生成
    for length in lengths:
        for combination in itertools.product(charset, repeat=length):
            yield ''.join(combination)

# 根据掩码生成密码
def generate_passwords_by_mask(mask, charset):
    # 根据掩码生成所有可能的密码
    positions = [i for i, char in enumerate(mask) if char == '?']
    fixed_chars = [char for char in mask if char != '?']
    
    for combination in itertools.product(charset, repeat=len(positions)):
        password = list(fixed_chars)
        for i, char in zip(positions, combination):
            password.insert(i, char)
        yield ''.join(password)

def generate_and_save(mode, log_listbox:Log_Listbox, lengths, mask, charset, filename='passwords.txt'):
    if mode:
        password_generator = generate_passwords(lengths, charset)
    else:
        password_generator = generate_passwords_by_mask(mask, charset)

    # 将密码生成器生成的密码逐个写入文件
    with open(filename, 'w') as file:
        for password in password_generator:
            file.write(f"{password}\n")
            log_listbox.insert_and_see(f"{password}\n")
    log_listbox.insert_and_see(f"密码列表已保存到 {filename}.")

def start_in_back(mode, log_listbox, lengths, mask, charset, filename='password.txt'):
    if mode:
        # 增加长度判断，如果没有长度则不执行
        if sum(lengths):
            # 在后台线程中启动密码生成
            threading.Thread(target=generate_and_save, 
                args=(mode, log_listbox, lengths, mask, charset, filename), 
                daemon=True).start()
    else:
        if len(mask):
            # 在后台线程中启动密码生成
            threading.Thread(target=generate_and_save, 
                args=(mode, log_listbox, lengths, mask, charset, filename), 
                daemon=True).start()
