import os
import tkinter as tk
from tkinter import filedialog, messagebox

# 功能函数


def add_txt_extension(file_path):
    if not os.path.exists(file_path):
        return

    file_name, file_extension = os.path.splitext(file_path)

    if file_extension == ".txt":
        return

    new_file_path = file_path + ".txt"
    os.rename(file_path, new_file_path)


def del_txt_extension(file_path):
    if not os.path.exists(file_path):
        return

    file_name, file_extension = os.path.splitext(file_path)

    if file_extension != ".txt":
        return

    new_file_path = file_name
    os.rename(file_path, new_file_path)


# GUI 主界面


def main():

    def select_file():
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            entry_file_path.delete(0, tk.END)
            entry_file_path.insert(0, folder_selected)

    def change_extension():
        file_path1 = entry_file_path.get() + "/MessageTransfer.sys"
        file_path2 = entry_file_path.get() + "/MessageTransfer_x86.sys"
        if os.path.exists(file_path1) and os.path.exists(file_path2):
            add_txt_extension(file_path1)
            add_txt_extension(file_path2)
            messagebox.showinfo("提示", "修改成功，需要重启以生效")
            if messagebox.askyesno("确认", "是否立即重启？"):
                os.system("shutdown -r -t 0")
        else:
            messagebox.showerror("错误", "文件不存在")

    def restore_extension():
        file_path1 = entry_file_path.get() + "/MessageTransfer.sys.txt"
        file_path2 = entry_file_path.get() + "/MessageTransfer_x86.sys.txt"
        if os.path.exists(file_path1) and os.path.exists(file_path2):
            del_txt_extension(file_path1)
            del_txt_extension(file_path2)
            messagebox.showinfo("提示", "修改成功，需要重启以生效")
            if messagebox.askyesno("确认", "是否立即重启？"):
                os.system("shutdown -r -t 0")
        else:
            messagebox.showerror("错误", "文件不存在")

    # 创建主窗口
    root = tk.Tk()
    root.title("完美世界对战平台VirtualBox适配工具")
    root.geometry("400x200")

    # 文件路径输入框
    tk.Label(root, text="文件夹路径（选择完美世界对战平台的plugin文件夹）").pack(pady=10)
    frame = tk.Frame(root)
    frame.pack()
    entry_file_path = tk.Entry(frame, width=40)
    entry_file_path.pack(side=tk.LEFT, padx=5)
    btn_browse = tk.Button(frame, text="浏览", command=select_file)
    btn_browse.pack(side=tk.LEFT)

    # 添加后缀名按钮
    btn_add = tk.Button(root, text="修改",
                        command=change_extension)
    btn_add.pack(pady=10)

    # 删除后缀名按钮
    btn_del = tk.Button(root, text="还原",
                        command=restore_extension)
    btn_del.pack(pady=10)

    # 运行主循环
    root.mainloop()


if __name__ == "__main__":
    main()
