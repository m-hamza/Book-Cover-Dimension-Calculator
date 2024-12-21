import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

def calculate_dimensions():
    # دریافت قطع کتاب
    book_cut = book_cut_var.get()
    dimensions = book_cuts.get(book_cut, None)
    if not dimensions:
        messagebox.showerror("خطا", "لطفاً یک قطع معتبر انتخاب کنید.")
        return

    # دریافت ورودی‌های کاربر
    try:
        pages = int(pages_entry.get())
        paper_weight = int(paper_weight_var.get())
    except ValueError:
        messagebox.showerror("خطا", "لطفاً مقادیر عددی معتبر برای تعداد صفحات و وزن کاغذ وارد کنید.")
        return

    # محاسبه ابعاد کتاب و ضخامت عطف
    width, height = dimensions
    spine_thickness = round((pages / 2) * (paper_weight / 1000), 2)
    
    # نمایش نتایج
    result_text.set(f"\n\nقطع کتاب: {book_cut}\nعرض (یک طرف): {width} میلی‌متر\nارتفاع: {height} میلی‌متر\nعرض (دو طرف): {width * 2 + spine_thickness} میلی‌متر\nضخامت عطف: {spine_thickness} میلی‌متر\n\nحاشیه‌های امن:\nچپ/راست: 10 میلی‌متر\nبالا/پایین: 10 میلی‌متر")

def show_guidelines():
    guidelines = (
        "راهنمای طراحی در فتوشاپ/ایلاستریتور:\n"
        "1. رزولوشن را روی 300 DPI تنظیم کنید.\n"
        "2. از عرض و ارتفاع محاسبه‌شده به میلی‌متر استفاده کنید.\n"
        "3. حاشیه‌های امن (10 میلی‌متر) برای متن و گرافیک اضافه کنید.\n\n"
        "راهنمای طراحی در ایندیزاین:\n"
        "1. یک سند جدید با ابعاد سفارشی ایجاد کنید.\n"
        "2. برش (Bleed) را روی 3 میلی‌متر در همه طرف‌ها تنظیم کنید.\n"
        "3. از ضخامت عطف محاسبه‌شده برای صحافی استفاده کنید.")
    messagebox.showinfo("راهنمای طراحی", guidelines)

def open_starteach():
    webbrowser.open("https://starteach.ir/")

# قطع‌های کتاب (به میلی‌متر) بر اساس اطلاعات لینک ارائه‌شده
book_cuts = {
    "وزیری": (165, 235),
    "رحلی": (210, 297),
    "رقعی": (148, 210),
    "خشتی": (200, 200),
    "پالتویی": (110, 220),
    "جیبی": (105, 145),
    "لارج فرمت": (240, 340),
    "رحلی کوچک": (170, 240)
}

# پنجره اصلی
root = tk.Tk()
root.title("محاسبه ابعاد جلد کتاب")
root.option_add('*Font', 'Tahoma 12')

# قاب برای ورودی‌ها
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky="EW")

# انتخاب قطع کتاب
ttk.Label(frame, text="انتخاب قطع کتاب:", anchor="e").grid(row=0, column=0, sticky="E")
book_cut_var = tk.StringVar()
book_cut_menu = ttk.Combobox(frame, textvariable=book_cut_var, values=list(book_cuts.keys()), state="readonly", justify="right")
book_cut_menu.grid(row=0, column=1, sticky="EW")
book_cut_menu.set("انتخاب قطع کتاب")

# ورودی تعداد صفحات
ttk.Label(frame, text="تعداد صفحات:", anchor="e").grid(row=1, column=0, sticky="E")
pages_entry = ttk.Entry(frame, justify="right")
pages_entry.grid(row=1, column=1, sticky="EW")

# انتخاب وزن کاغذ
ttk.Label(frame, text="وزن کاغذ (گرم بر متر مربع):", anchor="e").grid(row=2, column=0, sticky="E")
paper_weight_var = tk.StringVar()
paper_weight_menu = ttk.Combobox(frame, textvariable=paper_weight_var, values=[70, 80, 100], state="readonly", justify="right")
paper_weight_menu.grid(row=2, column=1, sticky="EW")
paper_weight_menu.set("انتخاب وزن کاغذ")

# دکمه محاسبه
calculate_button = ttk.Button(frame, text="محاسبه", command=calculate_dimensions)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# نمایش نتیجه
result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text, justify="right", padding="10")
result_label.grid(row=1, column=0, sticky="E")

# دکمه راهنما
guidelines_button = ttk.Button(root, text="راهنمای طراحی", command=show_guidelines)
guidelines_button.grid(row=2, column=0, pady=10)

# دکمه استارتیچ
starteach_button = ttk.Button(root, text="بازدید از استارتیچ", command=open_starteach)
starteach_button.grid(row=3, column=0, pady=10)

# اجرای برنامه
root.mainloop()
