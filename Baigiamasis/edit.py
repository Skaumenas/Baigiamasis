import tkinter as tk
from tkinter import messagebox, simpledialog
from load_save import export_csv, export_sql


def pasirinkt(remelis, tree, ):
    """
    Funkcija kuri paspaudus mygtuka Open file in editor atidaro faila i tree2 ir atidaro Edit mygtukus
    """
    add_button = tk.Button(remelis, text="Add Cell", command=lambda: add_cell(tree))
    add_button.place(rely=0.05, relx=0.55)
    labelis = tk.Label(remelis, text="Search: ")
    labelis.place(rely=0.065, relx=0.03)
    find = tk.Button(remelis, text="Find", command=lambda: find_object())
    find.place(rely=0.05, relx=0.4)
    delete = tk.Button(remelis, text="Delete", command=lambda: delete_cell(tree))
    delete.place(rely=0.05, relx=0.47)
    export_button = tk.Button(remelis, text="Save to CSV", command=lambda: export_csv(tree))
    export_button.place(rely=0.75, relx=0.65)
    filter_button = tk.Button(remelis, text="Show only", command=lambda: filter_data(tree))
    filter_button.place(rely=0.05, relx=0.65)
    entry = tk.Entry(remelis)
    entry.place(height=25, width=200, rely=0.06, relx=0.10)
    save_sql = tk.Button(remelis, text="Save to SQL", command=lambda: export_sql(tree))
    save_sql.place(rely=0.75, relx=0.80)

    def find_object():
        """
        Surasti faila excel data editor label
        """
        paieska = entry.get()
        for i in tree.get_children():
            duomenys = tree.item(i)
            reiksme = duomenys.get("values")
            if paieska in reiksme:
                tree.see(i)
                tree.selection_set(i)
                return
        messagebox.showerror("Error", "Object not found.")


def add_cell(arg):
    """
    Funkcija leidzianti paspaudus Add cell mygtuka prideti nauja lastele tree2 treeview
    """
    nauji_duomenys = simpledialog.askstring("Add cell", "Enter the values for the new row, separated by commas")
    if nauji_duomenys:
        new_values = nauji_duomenys.split(",")
        arg.insert("", "end", values=new_values)


def delete_cell(arg):
    """
    Funkcija kuri leidzia pasirikta lastele tree2 treeview, paspaudus Delete mygtuka, istrina lastele
    """
    pasirinkimas = arg.selection()
    if not pasirinkimas:
        messagebox.showinfo("Error", "No cell is selected. Please select a cell to delete.")
    else:
        patvirtint = messagebox.askyesno("Delete cell", "Are you sure you want to delete the selected cell?")
        if patvirtint:
            gauti = arg.parent(pasirinkimas)
            arg.delete(pasirinkimas)
            if not arg.get_children(gauti):
                arg.delete(gauti)


def filter_data(arg):
    """
    Funkcija kuri atvaizuoja tik ivestus duomenis
    """
    stulpelis = simpledialog.askstring("Show data", "Enter the column name")
    reiksme = simpledialog.askstring("Show data", "Enter the value")
    if stulpelis and reiksme:
        for row in arg.get_children():
            values = arg.set(row, stulpelis)
            if values != reiksme:
                arg.delete(row)
