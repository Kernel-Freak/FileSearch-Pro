import os
import argparse
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from datetime import datetime, timedelta
import platform
from tkinter import PhotoImage

# ---------------- Core File Search Logic ---------------- #

def get_creation_time(path):
    try:
        stat = os.stat(path)
        return stat.st_ctime if platform.system() == "Windows" else stat.st_mtime
    except Exception:
        return None

def search_files(directory, start=None, end=None, extension=None,
                 min_size=None, max_size=None, name_substr=None):
    result = []
    start_timestamp = 0
    end_timestamp = datetime.now().timestamp()

    if start:
        try:
            start_date = datetime.strptime(start, "%d-%m-%Y")
            start_timestamp = start_date.timestamp()
        except:
            pass

    if end:
        try:
            end_date = datetime.strptime(end, "%d-%m-%Y") + timedelta(days=1) - timedelta(seconds=1)
            end_timestamp = end_date.timestamp()
        except:
            pass

    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            try:
                stat = os.stat(path)
                c_time = get_creation_time(path)
                m_time = stat.st_mtime
                f_size = stat.st_size

                if c_time is None:
                    continue

                match_date = (start_timestamp <= c_time <= end_timestamp or
                              start_timestamp <= m_time <= end_timestamp)

                match_ext = extension is None or path.lower().endswith(extension.lower())
                match_size = ((min_size is None or f_size >= min_size) and
                              (max_size is None or f_size <= max_size))
                match_name = name_substr is None or name_substr.lower() in file.lower()

                if match_date and match_ext and match_size and match_name:
                    creation_str = datetime.fromtimestamp(c_time).strftime("%d-%m-%Y %H:%M:%S")
                    mod_str = datetime.fromtimestamp(m_time).strftime("%d-%m-%Y %H:%M:%S")
                    result.append(
                        f"{path}\n  Created: {creation_str}\n  Modified: {mod_str}\n  Size: {f_size} bytes\n"
                    )
            except Exception as e:
                result.append(f"Error reading {path}: {e}")
    result.append(f"Total matching files: {len(result) - 1}")
    return result

# ---------------- GUI Mode ---------------- #

def run_gui():
    def browse():
        path = filedialog.askdirectory()
        if path:
            dir_entry.delete(0, tk.END)
            dir_entry.insert(0, path)

    def search():
        directory = dir_entry.get()
        ext = ext_entry.get() or None
        name_sub = name_entry.get() or None
        start = start_entry.get() or None
        end = end_entry.get() or None
        try:
            min_sz = int(min_entry.get()) if min_entry.get() else None
            max_sz = int(max_entry.get()) if max_entry.get() else None
        except ValueError:
            messagebox.showerror("Invalid Input", "Size must be a number.")
            return

        if not directory:
            messagebox.showerror("Missing Input", "Please provide a directory to search.")
            return

        output_box.delete("1.0", tk.END)
        results.clear()

        res = search_files(directory, start, end, ext, min_sz, max_sz, name_sub)
        results.extend(res)
        for line in res:
            output_box.insert(tk.END, line + "\n")

    def save():
        if not results:
            messagebox.showinfo("No Results", "No results to save.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write("\n".join(results))
            messagebox.showinfo("Saved", f"Results saved to {path}")

    results = []

    root = tk.Tk()
    root.title("File Search Tool")
    root.geometry("800x600")
    root.minsize(750, 500)

    # Load icons (fallback to text if missing)
    try:
        search_icon = PhotoImage(file="search.png")  # replace with your actual icon path
        save_icon = PhotoImage(file="save.png")
        browse_icon = PhotoImage(file="folder.png")
    except:
        search_icon = save_icon = browse_icon = None

    font_label = ("Segoe UI", 10)
    font_entry = ("Segoe UI", 10)

    input_frame = tk.Frame(root, padx=10, pady=10)
    input_frame.pack(fill="x")

    def labeled_entry(parent, label_text, row):
        tk.Label(parent, text=label_text, font=font_label).grid(row=row, column=0, sticky="e", pady=2)
        entry = tk.Entry(parent, font=font_entry, width=40)
        entry.grid(row=row, column=1, sticky="w", pady=2)
        return entry

    dir_entry = labeled_entry(input_frame, "Directory", 0)
    browse_btn = tk.Button(input_frame, text="Browse", image=browse_icon, compound="left" if browse_icon else None,
                           command=browse)
    browse_btn.grid(row=0, column=2, padx=5)

    name_entry = labeled_entry(input_frame, "File Name Contains", 1)
    ext_entry = labeled_entry(input_frame, "Extension (e.g., .txt)", 2)
    start_entry = labeled_entry(input_frame, "Start Date (DD-MM-YYYY)", 3)
    end_entry = labeled_entry(input_frame, "End Date (DD-MM-YYYY)", 4)
    min_entry = labeled_entry(input_frame, "Min Size (bytes)", 5)
    max_entry = labeled_entry(input_frame, "Max Size (bytes)", 6)

    button_frame = tk.Frame(root, pady=5)
    button_frame.pack()

    tk.Button(button_frame, text="Search", image=search_icon, compound="left" if search_icon else None,
              width=80, command=search).pack(side="left", padx=5)
    tk.Button(button_frame, text="Save Results", image=save_icon, compound="left" if save_icon else None,
              width=80, command=save).pack(side="left", padx=5)

    output_box = scrolledtext.ScrolledText(root, font=("Consolas", 10), wrap=tk.WORD)
    output_box.pack(fill="both", expand=True, padx=10, pady=10)

    root.mainloop()

# ---------------- CLI Mode ---------------- #

def run_cli():
    parser = argparse.ArgumentParser(description="File Search Tool")
    parser.add_argument("directory", help="Directory to search")
    parser.add_argument("--start", help="Start date (DD-MM-YYYY)")
    parser.add_argument("--end", help="End date (DD-MM-YYYY)")
    parser.add_argument("--extension", help="File extension (e.g., .txt)")
    parser.add_argument("--min-size", type=int, help="Minimum size (bytes)")
    parser.add_argument("--max-size", type=int, help="Maximum size (bytes)")
    parser.add_argument("--name", help="File name contains (case-insensitive)")
    parser.add_argument("--save", help="Save output to file")
    args = parser.parse_args()

    results = search_files(args.directory, args.start, args.end, args.extension,
                           args.min_size, args.max_size, args.name)

    for line in results:
        print(line)

    if args.save:
        with open(args.save, "w", encoding="utf-8") as f:
            f.write("\n".join(results))
        print(f"\nResults saved to {args.save}")

# ---------------- Entry Point ---------------- #

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        run_gui()
    else:
        run_cli()
