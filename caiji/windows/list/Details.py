import tkinter as tk 
from tkinter import ttk 
from tkinter import scrolledtext 
def create_window():
    window = tk.Tk() 
    window.title("窗口标题") 
    window.state('zoomed')  # 将窗口最大化 
     # 创建标题标签 
    title_label = ttk.Label(window, text="标题", font=("Arial", 18)) 
    title_label.grid(row=0, column=0, padx=10, pady=10, sticky="w") 
    title_label_a = ttk.Label(window, text="价格", font=("Arial", 18)) 
    title_label_a.grid(row=1, column=0, padx=10, pady=10, sticky="w") 
    title_label_b = ttk.Label(window, text="五点描述", font=("Arial", 18)) 
    title_label_b.grid(row=2, column=0, padx=10, pady=10, sticky="w") 
    title_label_c = ttk.Label(window, text="详细描述", font=("Arial", 18)) 
    title_label_c.grid(row=7, column=0, padx=10, pady=10, sticky="w") 
    title_label_d = ttk.Label(window, text="颜色", font=("Arial", 18)) 
    title_label_d.grid(row=8, column=0, padx=10, pady=10, sticky="w") 
    title_label_e = ttk.Label(window, text="尺寸", font=("Arial", 18)) 
    title_label_e.grid(row=9, column=0, padx=10, pady=10, sticky="w") 
     # 创建标题输入框 
    title_entry = ttk.Entry(window, font=("Arial", 10), width=200) 
    title_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w") 
    title_entry_a = ttk.Entry(window, font=("Arial", 10), width=10) 
    title_entry_a.grid(row=1, column=1, padx=10, pady=10, sticky="w") 
    title_entry_b = [] 
    for i in range(5): 
        entry = ttk.Entry(window, font=("Arial", 10), width=200) 
        entry.grid(row=i+2, column=1, padx=10, pady=10, sticky="w") 
        title_entry_b.append(entry) 
    title_entry_c = scrolledtext.ScrolledText(window, width=200, height=10, font=("Arial", 10)) 
    title_entry_c.grid(row=7, column=1, padx=10, pady=10, sticky="w") 
     # 创建颜色单选框 
    color_var = tk.StringVar() 
    color_var.set("黑色") 
    colors = ["黑色", "红色"] 
    color_radiobuttons = [] 
    for i, color in enumerate(colors): 
        radiobutton = ttk.Radiobutton(window, text=color, variable=color_var, value=color) 
        radiobutton.grid(row=8, column=i+1, padx=10, pady=10, sticky="w") 
        color_radiobuttons.append(radiobutton) 
     # 创建尺寸单选框 
    size_var = tk.StringVar() 
    size_var.set("S") 
    size_radiobuttons = [] 
    def update_size(event):
        selected_color = color_var.get() 
        if selected_color == "黑色": 
            sizes = ["S", "L", "M"] 
        elif selected_color == "红色": 
            sizes = ["S", "L"] 
        size_var.set(sizes[0]) 
        for radiobutton in size_radiobuttons: 
            if radiobutton.cget("text") in sizes: 
                radiobutton.configure(state="normal") 
            else: 
                radiobutton.configure(state="disabled") 
        if size_var.get() not in sizes: 
            size_var.set("") 
    for i, size in enumerate(["S", "L", "M"]):
        radiobutton = ttk.Radiobutton(window, text=size, variable=size_var, value=size) 
        radiobutton.grid(row=9, column=i+1, padx=10, pady=10, sticky="w") 
        size_radiobuttons.append(radiobutton) 
    for radiobutton in color_radiobuttons:
        radiobutton.bind("<Button-1>", update_size) 
     # 创建列表框架 
    list_frame = ttk.Frame(window) 
    list_frame.grid(row=10, column=0, columnspan=2, padx=10, pady=10, sticky="w") 
     # 创建列表 
    listbox = tk.Listbox(list_frame, font=("Arial", 10), width=100, height=10) 
    listbox.pack(side="left", fill="both", expand=True) 
     # 创建滚动条 
    scrollbar = ttk.Scrollbar(list_frame, command=listbox.yview) 
    scrollbar.pack(side="right", fill="y") 
    listbox.config(yscrollcommand=scrollbar.set) 
     # 添加示例数据到列表 
    for i in range(10): 
        listbox.insert(tk.END, f"数据{i+1}") 
    window.mainloop()
 # 运行窗口 
create_window()