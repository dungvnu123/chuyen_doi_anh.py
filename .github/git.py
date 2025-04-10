import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def images_to_pdf(images, pdf_name):
    try:
        pdf = Image.open(images[0])
        image_list = [Image.open(img) for img in images[1:]]
        pdf.save(pdf_name, "PDF", resolution=100.0, save_all=True, append_images=image_list)
        messagebox.showinfo("Thành công", f"File PDF đã được lưu tại {pdf_name}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")

def browse_images():
    images = filedialog.askopenfilenames(title="Chọn các ảnh", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if images:
        pdf_name = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if pdf_name:
            images_to_pdf(images, pdf_name)


root = tk.Tk()
root.title("Chuyển ảnh thành PDF")


btn_browse = tk.Button(root, text="Chọn ảnh để chuyển đổi", command=browse_images)
btn_browse.pack(pady=20)


root.mainloop()
