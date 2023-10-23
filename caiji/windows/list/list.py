import tkinter as tk
from tkinter import ttk
import caiji.mysql.mysql
import caiji.windows.ListRun.ParentDo
from caiji.windows.ListRun import ParentDo
def show_page(page_num):
    global items_per_page_combobox, text_widget, total_pages_label
    items_per_page = int(items_per_page_combobox.get())
    start = (page_num - 1) * items_per_page
    end = page_num * items_per_page
    ShuJU = ParentDo.get_data(items_per_page, page_num)
    text_widget.delete("1.0", tk.END)
    header = f"{'ID':<10}{'Seller_SKU':<15}{'Item_Name':<40}{'Standard_Price':<20}{'URL':<70}{'主体ID':<10}{'操作'}"
    text_widget.insert(tk.END, header + "\n""\n")
    for item in ShuJU:
        truncated_id = caiji.windows.ListRun.ParentDo.truncate_string(item['id'], 10)
        truncated_sku = caiji.windows.ListRun.ParentDo.truncate_string(item['Seller_SKU'], 15)
        truncated_name = caiji.windows.ListRun.ParentDo.truncate_string(item['Item_Name'], 40)
        truncated_price = caiji.windows.ListRun.ParentDo.truncate_string(item['Standard_Price'], 20)
        truncated_url = caiji.windows.ListRun.ParentDo.truncate_string(item['URL'], 40)
        truncated_mjid = caiji.windows.ListRun.ParentDo.truncate_string(item['MJ_id'], 10)
        row = f"{truncated_id:<10}|{truncated_sku:<15}|{truncated_name:<45}|{truncated_price:<12}|{truncated_url:<65}|{truncated_mjid:<10}"
        text_widget.insert(tk.END, row + "")
        button = ttk.Button(text="详情", command=lambda item=item: show_details(item))
        text_widget.window_create(tk.END, window=button)
        text_widget.insert(tk.END, "\n""\n")
def show_details(item):
    details_window = tk.Toplevel()
    details_window.title("详情")
    details_window.geometry("400x200")
    details_label = ttk.Label(details_window, text=f"ID: {item['id']}\nSeller_SKU: {item['Seller_SKU']}\nItem_Name: {item['Item_Name']}\nStandard_Price: {item['Standard_Price']}\nURL: {item['URL']}\nMJ_id: {item['MJ_id']}")
    details_label.pack(padx=20, pady=20)
def create_window():
    global items_per_page_combobox, text_widget, total_pages_label
    window = tk.Tk()
    window.title("数据列表")
    window.geometry("800x500")  # 设置窗口大小
    def update_items_per_page(event):
        show_page(1)
    def prev_page():
        current_page = int(page_label.cget("text"))
        if current_page > 1:
            show_page(current_page - 1)
            page_label.config(text=str(current_page - 1))
    def next_page():
        current_page = int(page_label.cget("text"))
        total_pages = (caiji.windows.ListRun.ParentDo.page() + int(items_per_page_combobox.get()) - 1) // int(items_per_page_combobox.get())
        if current_page < total_pages:
            show_page(current_page + 1)
            page_label.config(text=str(current_page + 1))
    list_frame = ttk.Frame(window)
    list_frame.pack(pady=10, fill="both", expand=True)
    text_widget = tk.Text(list_frame, height=10, font=("Courier New", 11))
    text_widget.pack(side="left", fill="both", expand=True)
    scrollbar = ttk.Scrollbar(list_frame, command=text_widget.yview)
    scrollbar.pack(side="right", fill="y")
    text_widget.config(yscrollcommand=scrollbar.set)
    page_frame = ttk.Frame(window)
    page_frame.pack(pady=10)
    prev_button = ttk.Button(page_frame, text="上一页", command=prev_page)
    prev_button.pack(side="left")
    page_label = ttk.Label(page_frame, text="1")
    page_label.pack(side="left")
    next_button = ttk.Button(page_frame, text="下一页", command=next_page)
    next_button.pack(side="left")
    items_per_page_combobox = ttk.Combobox(page_frame, values=["20", "50", "100", "200", "500"])
    items_per_page_combobox.current(0)
    items_per_page_combobox.pack(side="right")
    items_per_page_combobox.bind("<<ComboboxSelected>>", update_items_per_page)
    total_pages_label = ttk.Label(page_frame, text="")
    total_pages_label.pack(side="right")
    show_page(1)
    window.mainloop()
create_window()