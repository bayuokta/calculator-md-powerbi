import tkinter as tk
from tkinter import messagebox

def calculate_mandays():
    try:
        easy_mandays_dataset = float(easy_entry_dataset.get())
        medium_mandays_dataset = float(medium_entry_dataset.get()) * 2
        easy_visual_chart = float(entry_easy_visual_chart.get()) * (30/480)
        easy_visual_grid = float(entry_easy_visual_grid.get()) * (10/480)
        medium_visual_chart = float(entry_medium_visual_chart.get()) * (20/480)
        medium_visual_grid = float(entry_medium_visual_grid.get()) * (240/480)
        page = float(entry_page.get()) * (3/480)
        additional_page = float(entry_additional_page.get()) * (240/480)

        total_mandays = easy_mandays_dataset + medium_mandays_dataset + easy_visual_chart + easy_visual_grid + medium_visual_chart + medium_visual_grid + page + additional_page
        messagebox.showinfo("Hasil", f"Total Mandays: {total_mandays}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid di semua field!")

def validate_input(input_text):
    return input_text.isdigit() or input_text == ""

# Membuat dan Mengkonfigurasi jendela utama
window = tk.Tk()
window.title("Calculator Mandays Power BI")
window.resizable(0,0)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 200
window_height = 440
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Membuat frame untuk kategori Dataset
dataset_frame = tk.LabelFrame(window, text="Dataset", padx=10, pady=10)
dataset_frame.pack(padx=10, pady=10)

easy_label_dataset = tk.Label(dataset_frame, text="Easy\t")
easy_label_dataset.grid(row=0, column=0)

validate_entry = window.register(validate_input)
easy_entry_dataset = tk.Entry(dataset_frame, width=10, validate="key", validatecommand=(validate_entry, "%P"))
easy_entry_dataset.grid(row=0, column=1)

medium_label_dataset = tk.Label(dataset_frame, text="Medium\t")
medium_label_dataset.grid(row=1, column=0)

medium_entry_dataset = tk.Entry(dataset_frame, width=10, validate="key", validatecommand=(validate_entry, "%P"))
medium_entry_dataset.grid(row=1, column=1)

# Membuat frame untuk kategori Visual
visual_frame = tk.LabelFrame(window, text="Visual", padx=10, pady=10)
visual_frame.pack(padx=10, pady=10)

# Membuat frame untuk kategori Easy Visual
visual_frame_easy = tk.LabelFrame(visual_frame, text="Easy Visual", padx=2, pady=2)
visual_frame_easy.pack(padx=2, pady=2)

label_easy_visual_chart = tk.Label(visual_frame_easy, text="Chart")
label_easy_visual_chart.grid(row=0, column=0)

entry_easy_visual_chart = tk.Entry(visual_frame_easy, width=10, validate="key", validatecommand=(validate_entry, "%P"))
entry_easy_visual_chart.grid(row=0, column=1)

label_easy_visual_grid = tk.Label(visual_frame_easy, text="Grid")
label_easy_visual_grid.grid(row=1, column=0)

entry_easy_visual_grid = tk.Entry(visual_frame_easy, width=10, validate="key", validatecommand=(validate_entry, "%P"))
entry_easy_visual_grid.grid(row=1, column=1)

# Membuat frame untuk kategori Medium Visual
visual_frame_medium = tk.LabelFrame(visual_frame, text="Medium Visual", padx=2, pady=2)
visual_frame_medium.pack(padx=2, pady=2)

label_medium_visual_chart = tk.Label(visual_frame_medium, text="Chart")
label_medium_visual_chart.grid(row=0, column=0)

entry_medium_visual_chart = tk.Entry(visual_frame_medium, width=10, validate="key", validatecommand=(validate_entry, "%P"))
entry_medium_visual_chart.grid(row=0, column=1)

label_medium_visual_grid = tk.Label(visual_frame_medium, text="Grid")
label_medium_visual_grid.grid(row=1, column=0)

entry_medium_visual_grid = tk.Entry(visual_frame_medium, width=10, validate="key", validatecommand=(validate_entry, "%P"))
entry_medium_visual_grid.grid(row=1, column=1)

# Tambahkan frame untuk kategori Page
page_frame = tk.LabelFrame(window, text="Page", padx=10, pady=10)
page_frame.pack(padx=10, pady=10)

label_page = tk.Label(page_frame, text="---\t")
label_page.grid(row=0, column=0)

entry_page = tk.Entry(page_frame, width=10, validate="key", validatecommand=(validate_entry, "%P"))
entry_page.grid(row=0, column=1)

label_additional = tk.Label(page_frame, text="Opt\t")
label_additional.grid(row=1, column=0)

entry_additional_page = tk.Entry(page_frame, width=10, validate="key", validatecommand=(validate_entry, "%P"))
entry_additional_page.grid(row=1, column=1)

# Membuat tombol untuk menghitung mandays
calculate_button = tk.Button(window, text="Calculate", command=calculate_mandays)
calculate_button.pack(pady=10)

# Menjalankan aplikasi
window.mainloop()
