import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk
import random

# ==================== 数据层 ====================
# 环保文章数据库（扩展2个新条目）
articles = {
    "塑料污染治理": (
        "【最新数据】全球每分钟消耗100万个塑料瓶\n"
        "【创新方案】可降解材料成本下降40%\n"
        "【行动倡议】2025年全球禁用一次性塑料制品"
    ),
    "绿色品牌实践": (
        "星巴克纸质吸管替代方案\n"
        "可口可乐PlantBottle™包装技术\n"
        "宜家再生材料家具系列"
    ),
    "环保产业发展": {
        "content": (
            "【政策驱动】国家十四五规划明确环保产业投入增长20%\n"
            "【市场现状】2025年环保市场规模预计突破10万亿元\n"
            "【技术突破】AIoT智能监测系统提升污染预警效率"
        )
    },
    "生态修复案例": {
        "content": (
            "【成功实践】长江十年禁渔计划使鱼类资源恢复35%\n"
            "【技术创新】微生物降解技术处理土壤重金属污染\n"
            "【国际合作】一带一路生态廊道建设项目覆盖20国"
        )
    }
}

# 环保问答数据
quiz_data = [
    {
        "question": "下列哪种垃圾属于可回收物？",
        "options": ["A. 废电池", "B. 果皮", "C. 玻璃瓶", "D. 餐巾纸"],
        "answer": "C",
        "explanation": "玻璃瓶属于可回收物，可以通过回收再利用减少资源浪费。"
    },
    {
        "question": "关于节约用水，下列说法正确的是？",
        "options": ["A. 洗菜水可以用来浇花", "B. 漏水龙头不需要立即维修", "C. 洗澡时间越长越好", "D. 自来水取之不尽"],
        "answer": "A",
        "explanation": "洗菜的水可以用来浇花，这是一种很好的水资源循环利用方式。"
    },
    {
        "question": "以下哪种行为最环保？",
        "options": ["A. 使用一次性餐具", "B. 自带购物袋", "C. 每天开车上班", "D. 经常网购"],
        "answer": "B",
        "explanation": "自带购物袋可以减少塑料袋的使用，是一种环保的生活方式。"
    },
    {
        "question": "节能灯相比普通灯泡的优点是？",
        "options": ["A. 更亮", "B. 更省电", "C. 更便宜", "D. 更重"],
        "answer": "B",
        "explanation": "节能灯能耗低，使用寿命长，有助于节约能源。"
    },
    {
        "question": "下列哪项是绿色出行方式？",
        "options": ["A. 步行", "B. 开私家车", "C. 打出租车", "D. 摩托车"],
        "answer": "A",
        "explanation": "步行和骑自行车都是绿色出行方式，减少碳排放。"
    },
    {
        "question": "废旧电池应如何处理？",
        "options": ["A. 随意丢弃", "B. 与生活垃圾混合", "C. 投放到专用回收箱", "D. 埋在土里"],
        "answer": "C",
        "explanation": "废旧电池含有有害物质，应投放到专用回收箱。"
    },
    {
        "question": "下列哪种行为有助于减少空气污染？",
        "options": ["A. 烧垃圾", "B. 多乘坐公共交通", "C. 使用煤炭取暖", "D. 露天烧烤"],
        "answer": "B",
        "explanation": "乘坐公共交通可以减少汽车尾气排放，降低空气污染。"
    },
    {
        "question": "纸张回收的主要目的是？",
        "options": ["A. 节约木材资源", "B. 增加垃圾量", "C. 提高成本", "D. 制造塑料"],
        "answer": "A",
        "explanation": "回收纸张可以节约木材资源，保护森林。"
    },
    {
        "question": "下列哪种包装最环保？",
        "options": ["A. 塑料袋", "B. 一次性泡沫盒", "C. 可降解纸袋", "D. 金属罐"],
        "answer": "C",
        "explanation": "可降解纸袋易于分解，减少环境污染。"
    },
    {
        "question": "节约用电的好处包括？",
        "options": ["A. 降低电费", "B. 减少碳排放", "C. 保护环境", "D. 以上都是"],
        "answer": "D",
        "explanation": "节约用电既能省钱，又能减少碳排放，保护环境。"
    },
    {
        "question": "下列哪种行为属于低碳生活？",
        "options": ["A. 长时间开空调", "B. 随手关灯", "C. 用塑料袋购物", "D. 用一次性筷子"],
        "answer": "B",
        "explanation": "随手关灯可以减少能源浪费，是低碳生活的体现。"
    },
    {
        "question": "废旧衣物最好的处理方式是？",
        "options": ["A. 丢进垃圾桶", "B. 捐赠或回收", "C. 焚烧", "D. 埋在地下"],
        "answer": "B",
        "explanation": "捐赠或回收废旧衣物可以减少浪费，帮助他人。"
    },
    {
        "question": "下列哪种能源属于可再生能源？",
        "options": ["A. 石油", "B. 天然气", "C. 太阳能", "D. 煤炭"],
        "answer": "C",
        "explanation": "太阳能、风能、水能等都是可再生能源。"
    },
    {
        "question": "绿色食品的特点是？",
        "options": ["A. 无污染", "B. 高农药残留", "C. 添加剂多", "D. 价格低"],
        "answer": "A",
        "explanation": "绿色食品指生产过程中无污染、无有害添加剂。"
    },
    {
        "question": "下列哪种行为有助于保护水资源？",
        "options": ["A. 随意排放污水", "B. 节约用水", "C. 倒油进下水道", "D. 洗车用大量水"],
        "answer": "B",
        "explanation": "节约用水和防止水体污染有助于保护水资源。"
    },
    {
        "question": "下列哪种垃圾属于有害垃圾？",
        "options": ["A. 塑料瓶", "B. 废旧电池", "C. 果皮", "D. 纸箱"],
        "answer": "B",
        "explanation": "废旧电池含有有害物质，属于有害垃圾。"
    },
    {
        "question": "减少塑料使用的有效方法是？",
        "options": ["A. 多用一次性塑料袋", "B. 自带购物袋", "C. 用塑料瓶喝水", "D. 用塑料餐具"],
        "answer": "B",
        "explanation": "自带购物袋可以有效减少塑料袋的使用。"
    },
    {
        "question": "下列哪种行为有助于节能减排？",
        "options": ["A. 长时间开灯", "B. 合理使用空调", "C. 用煤炭取暖", "D. 用电热水器全天加热"],
        "answer": "B",
        "explanation": "合理使用空调可以减少能源消耗，降低排放。"
    },
    {
        "question": "绿色出行的方式包括？",
        "options": ["A. 步行", "B. 骑自行车", "C. 乘坐公共交通", "D. 以上都是"],
        "answer": "D",
        "explanation": "步行、骑自行车和乘坐公共交通都是绿色出行方式。"
    },
    {
        "question": "下列哪种行为有助于减少温室气体排放？",
        "options": ["A. 多开私家车", "B. 使用节能家电", "C. 烧煤取暖", "D. 乱丢垃圾"],
        "answer": "B",
        "explanation": "使用节能家电可以减少能源消耗，降低温室气体排放。"
    },
    {
        "question": "废旧手机应如何处理？",
        "options": ["A. 丢进普通垃圾桶", "B. 专业回收", "C. 埋在地下", "D. 随意丢弃"],
        "answer": "B",
        "explanation": "废旧手机含有有害物质，应交给专业回收机构处理。"
    },
    {
        "question": "下列哪种行为有助于保护野生动物？",
        "options": ["A. 购买野生动物制品", "B. 不随意捕捉野生动物", "C. 破坏栖息地", "D. 投喂野生动物"],
        "answer": "B",
        "explanation": "不随意捕捉和购买野生动物制品有助于保护野生动物。"
    },
    {
        "question": "下列哪种行为有助于减少纸张浪费？",
        "options": ["A. 双面打印", "B. 多用一次性纸杯", "C. 随意撕纸", "D. 用纸擦桌子"],
        "answer": "A",
        "explanation": "双面打印可以有效减少纸张浪费。"
    }
]

# 用户积分系统
user_points = 0

# ==================== 工具层 ====================
# 文件操作函数
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
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            messagebox.showinfo("成功", "内容已保存")
        except Exception as e:
            messagebox.showerror("错误", f"保存失败：{str(e)}")

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

# ==================== 界面层 ====================
# 创建主窗口
root = tk.Tk()
root.title("EcoGuide智能环保向导")
root.geometry("1000x700")
root.resizable(False, False)

# 应用主题（优先使用ttkthemes，否则回退到内置主题）
try:
    style = ThemedStyle(root)
    style.set_theme("arc")
except ImportError:
    style = ttk.Style()
    style.theme_use("clam")

# 颜色配置
colors = {
    "primary": "#2E7D32",
    "bg": "#E8F5E9"
}

# 工具栏
toolbar = ttk.Frame(root)
toolbar.pack(side=tk.TOP, fill=tk.X)

ttk.Button(toolbar, text="保存内容", command=save_article).pack(
    side=tk.LEFT, padx=5, pady=5)
ttk.Button(toolbar, text="打开文件", command=open_article).pack(
    side=tk.LEFT, padx=5, pady=5)

# 分页控件
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

# ===== 文章展示页 =====
article_tab = ttk.Frame(notebook)
notebook.add(article_tab, text="环保知识")

main_frame = ttk.PanedWindow(article_tab, orient=tk.HORIZONTAL)
main_frame.pack(fill=tk.BOTH, expand=True)

button_frame = ttk.Frame(main_frame)
main_frame.add(button_frame, weight=1)

content_frame = ttk.Frame(main_frame)
main_frame.add(content_frame, weight=3)

text_area = tk.Text(
    content_frame, wrap=tk.WORD, font=("微软雅黑", 12),
    bg=colors["bg"], fg=colors["primary"], relief="flat"
)
text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

for title in articles:
    ttk.Button(
        button_frame, text=title,
        command=lambda t=title: show_article(t)
    ).pack(pady=5, fill=tk.X)



# ===== 环保问答页 =====
quiz_tab = ttk.Frame(notebook)
notebook.add(quiz_tab, text="环保问答")

quiz_frame = ttk.Frame(quiz_tab)
quiz_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# 积分显示
points_label = ttk.Label(quiz_frame, text=f"当前积分：{user_points}", font=("微软雅黑", 12))
points_label.pack(pady=10)

# 问题显示区
question_label = ttk.Label(quiz_frame, text="准备好开始答题了吗？", font=("微软雅黑", 14))
question_label.pack(pady=20)

# 选项按钮框架
options_frame = ttk.Frame(quiz_frame)
options_frame.pack(pady=20)

option_buttons = []
for i in range(4):
    btn = ttk.Button(options_frame, text="", width=40)
    btn.pack(pady=5)
    option_buttons.append(btn)

# 解释文本区
explanation_text = tk.Text(quiz_frame, wrap=tk.WORD, height=4, font=("微软雅黑", 12))
explanation_text.pack(fill=tk.X, padx=20, pady=10)
explanation_text.config(state=tk.DISABLED)

# 开始按钮
start_button = ttk.Button(quiz_frame, text="开始答题", width=20)
start_button.pack(pady=10)

# ==================== 交互逻辑 ====================
# 显示文章函数
def show_article(title):
    data = articles[title]
    if isinstance(data, dict):  # 兼容新旧数据结构
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, data["content"])
    else:
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, data)

# 问答游戏逻辑
current_question = None

def start_quiz():
    global current_question
    # 随机选择一个问题
    current_question = random.choice(quiz_data)
    
    # 显示问题
    question_label.config(text=current_question["question"])
    
    # 设置选项按钮
    for i, (btn, option) in enumerate(zip(option_buttons, current_question["options"])):
        btn.config(text=option, command=lambda x=chr(65+i): check_answer(x))
    
    # 清空解释文本
    explanation_text.config(state=tk.NORMAL)
    explanation_text.delete(1.0, tk.END)
    explanation_text.config(state=tk.DISABLED)
    
    # 禁用开始按钮
    start_button.config(state=tk.DISABLED)

def check_answer(selected_answer):
    global user_points
    
    if current_question and selected_answer == current_question["answer"]:
        # 答对加分
        user_points += 10
        points_label.config(text=f"当前积分：{user_points}")
        
        # 显示正确提示
        messagebox.showinfo(title="答对了！", message="恭喜你答对了，获得10积分！")
        
        # 检查是否达到100分
        if user_points >= 100:
            messagebox.showinfo("恭喜", "太棒了！你已经获得100积分！\n让我们去看看环保知识吧！")
            notebook.select(0)  # 切换到第一个标签页（环保知识）
            return  # 不再继续答题
    else:
        # 答错提示
        messagebox.showinfo(title="答错了", message=f"很遗憾答错了，正确答案是：{current_question['answer']}")
    
    # 显示解释
    explanation_text.config(state=tk.NORMAL)
    explanation_text.delete(1.0, tk.END)
    explanation_text.insert(tk.END, current_question["explanation"])
    explanation_text.config(state=tk.DISABLED)
    
    # 1.5秒后自动切换到下一题
    root.after(1500, start_quiz)

# 绑定开始按钮事件
start_button.config(command=start_quiz)

# 退出确认对话框
def on_closing():
    if messagebox.askokcancel("退出", "要保存当前内容吗？"):
        save_article()
    root.destroy()

# 启动主循环
root.mainloop()