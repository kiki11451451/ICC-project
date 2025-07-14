import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from ttkthemes import ThemedStyle  # 需安装ttkthemes库 [[6]]
import random

# 创建主窗口
root = tk.Tk()
root.title("GreenHub 环保交互站")
root.geometry("800x500")
root.resizable(False, False)

# 应用主题（参考知识库3的界面优化理念）
style = ThemedStyle(root)
style.set_theme("arc")  # 使用现代感主题[[3]]

# 颜色主题
colors = {
    "primary": "#2E7D32",   # 绿色主色调
    "secondary": "#A5D6A7",
    "text": "#2E7D32",
    "bg": "#E8F5E9"
}

# 环保文章数据库（扩展知识库8的数据可视化概念）
articles = {
    "塑料污染治理": {
        "content": (
            "【最新数据】全球每分钟消耗100万个塑料瓶\n"
            "【创新方案】可降解材料成本已下降40%\n"
            "【行动倡议】2025年全球禁用一次性塑料制品\n"
            "【企业实践】麦当劳推出纸吸管替代方案"
        ),
        "image": "plastic.png"
    }
}

# 保存文章内容函数（参考知识库4的实用功能）
def save_article():
    content = text_area.get(1.0, tk.END)
    if not content.strip():
        messagebox.showwarning("提示", "没有可保存的内容")
        return
    
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        messagebox.showinfo("成功", "内容已保存")

# 新增：读取文件函数 [[2]][[4]]
def open_article():
    file_path = filedialog.askopenfilename(
        title="选择文本文件",
        filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("错误", f"无法读取文件：{str(e)}")

# 随机背景色函数（动态效果）
def change_bg_color():
    color = random.choice(list(colors.values()))
    root.configure(bg=color)
    bg_color_btn.configure(style="Random.TButton")

# 显示文章函数（增强交互）
def show_article(title):
    data = articles[title]
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, data["content"])
    
    try:
        img = tk.PhotoImage(file=data["image"])
        image_label.configure(image=img)
        image_label.image = img
    except:
        image_label.configure(text="图片暂缺", fg=colors["primary"])

# 退出确认对话框
def on_closing():
    if messagebox.askokcancel("退出", "要保存当前内容吗？"):
        save_article()
    root.destroy()

# 创建顶部工具栏
toolbar = ttk.Frame(root)
toolbar.pack(side=tk.TOP, fill=tk.X)

# 工具栏按钮（新增open_article绑定 [[2]]）
save_btn = ttk.Button(toolbar, text="保存内容", command=save_article)
save_btn.pack(side=tk.LEFT, padx=5, pady=5)

open_btn = ttk.Button(toolbar, text="打开文件", command=open_article)
open_btn.pack(side=tk.LEFT, padx=5, pady=5)

bg_color_btn = ttk.Button(toolbar, text="随机背景", command=change_bg_color)
bg_color_btn.pack(side=tk.LEFT, padx=5, pady=5)

# 创建左右分区框架（参考知识库3的模块化设计）
main_frame = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
main_frame.pack(fill=tk.BOTH, expand=True)

# 左侧按钮区域
button_frame = ttk.Frame(main_frame)
main_frame.add(button_frame, weight=1)

# 右侧内容区域
content_frame = ttk.Frame(main_frame)
main_frame.add(content_frame, weight=3)

# 图片展示区
image_label = ttk.Label(content_frame)
image_label.pack(pady=10)

# 文章展示区
text_area = tk.Text(content_frame, wrap=tk.WORD, font=("微软雅黑", 12),
                   bg=colors["bg"], fg=colors["text"], relief="flat")
text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# 添加按钮（带悬停效果）
for title in articles:
    btn = ttk.Button(button_frame, text=title,
                    command=lambda t=title: show_article(t))
    btn.pack(pady=5, fill=tk.X)

# 绑定关闭事件
root.protocol("WM_DELETE_WINDOW", on_closing)

# 启动主循环
root.mainloop()