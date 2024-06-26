import os
import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2


def merge_pdfs(pdf1, pdf2, output_path):
    pdf_merger = PyPDF2.PdfMerger()
    pdf_merger.append(pdf1)
    pdf_merger.append(pdf2)
    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)


def select_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path


def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    return file_path


def continue_prompt():
    root = tk.Tk()
    root.withdraw()
    return messagebox.askyesno("Continuar", "Completado! \nContinuar generando más uniones PDF?")


def main():
    continue_generation = True
    while continue_generation:
        folder_path = select_folder()
        if not folder_path:
            continue_generation = continue_prompt()
            continue

        unique_pdf = select_file()
        if not unique_pdf:
            continue_generation = continue_prompt()
            continue

        output_folder = os.path.join(
            folder_path, os.path.basename(folder_path))
        os.makedirs(output_folder, exist_ok=True)

        for filename in os.listdir(folder_path):
            if filename.endswith(".pdf") and filename != os.path.basename(unique_pdf):
                pdf_path = os.path.join(folder_path, filename)
                output_path = os.path.join(output_folder, filename)
                merge_pdfs(pdf_path, unique_pdf, output_path)
                print(f'Completado: {output_path}')

        continue_generation = continue_prompt()

if __name__ == "__main__":
    main()
