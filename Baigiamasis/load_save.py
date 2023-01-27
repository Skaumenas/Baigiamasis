import pandas as pd
import tkinter as tk
from tkinter import messagebox
import csv
from tkinter import filedialog
import sqlite3


def failo_narsykle(arg):
    """
    Funkcija kuri paspaudus mygtuka ijungs operacines sistemos failu narsykle
    """
    pavadinimas = filedialog.askopenfilename(initialdir="/",
                                             title="Select A File",
                                             filetype=(("csv files", "*.csv"), ("All Files", "*.*")))
    arg["text"] = pavadinimas
    return None


def ikelti_failus(arg, label):
    """
    Funkcija kuri paspaudus mygtuka ikelia visus pasirinkto csv failo duomenis i treeview perziura
    """
    vieta = label["text"]
    try:
        pavadinimas = r"{}".format(vieta)
        if pavadinimas[-4:] == ".csv":
            df = pd.read_csv(pavadinimas)
        else:
            df = pd.read_excel(pavadinimas)

    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file")
        return None

    for i in arg.get_children():
        arg.delete(i)

    arg["column"] = list(df.columns)
    arg["show"] = "headings"
    for column in arg["columns"]:
        arg.heading(column, text=column)

    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        arg.insert("", "end", values=row)
    return None


def export_csv(arg):
    """
    Funkcija kuri leidzia issaugoti tree2 treeview esancius duomenis i csv faila
    """
    pavadinimas = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")])
    if pavadinimas:
        with open(pavadinimas, 'w', newline='') as f:
            writer = csv.writer(f)
            duomenys = [arg.heading(col, option='text') for col in arg['columns']]
            writer.writerow(duomenys)
            for row in arg.get_children():
                reiksmes = [arg.set(row, col) for col in arg['columns']]
                writer.writerow(reiksmes)
        messagebox.showinfo("Success", "Data saved successfully to " + pavadinimas)


def export_sql(arg):
    """
    Funkcija kuri leidzia issaugoti tree2 treeview esancius duomenis i sql faila
    """
    pavadinimas = filedialog.asksaveasfilename(defaultextension=".sql", filetypes=[("SQL", "*.sql")])
    if pavadinimas:
        conn = sqlite3.connect(pavadinimas)
        c = conn.cursor()
        column_names = [arg.heading(col, option='text') for col in arg['columns']]
        c.execute(f'CREATE TABLE data({",".join(column_names)})')
        for row in arg.get_children():
            reiksmes = arg.item(row, option='values')
            placeholders = ','.join('?' * len(column_names))
            c.execute(f'INSERT INTO data({",".join(column_names)}) VALUES({placeholders})', reiksmes)
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Data saved successfully to " + pavadinimas)
