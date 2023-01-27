import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from load_save import ikelti_failus, failo_narsykle
from edit import pasirinkt
from Plot import show

# pagrindinis langas jo dydis pavadinimas parametrai
root = tk.Tk()
root.title("Baigimasis projektas")
root.geometry("1480x720")
root.pack_propagate(False)
root.resizable(0, 0)

# Remeliai
remelis1 = tk.LabelFrame(root, text="Excel Data")
remelis1.place(height=600, width=700)
remelis2 = tk.LabelFrame(root, text="Editor")
remelis2.place(height=500, width=750, rely=0, relx=0.48)
file_remelis1 = tk.LabelFrame(root, text="Plot menu")
file_remelis1.place(height=200, width=750, rely=0.70, relx=0.48)
file_remelis2 = tk.LabelFrame(root, text="Open File")
file_remelis2.place(height=100, width=700, rely=0.839, relx=0.003)
remelis3 = tk.LabelFrame(remelis2, text="Excel Data")
remelis3.place(height=300, width=730, rely=0, relx=0.01)
remelis33 = tk.LabelFrame(remelis2, text="Options")
remelis33.place(height=170, width=730, rely=0.63, relx=0.01)

# Mygtukai
mygtukas1 = tk.Button(file_remelis2, text="Browse A File", command=lambda: failo_narsykle(label_file))
mygtukas1.place(rely=0.65, relx=0.50)
mygtukas2 = tk.Button(file_remelis2, text="Load File", command=lambda: ikelti_failus(tree1, label_file))
mygtukas2.place(rely=0.65, relx=0.30)
editorbutton = tk.Button(remelis33, text="Open file in editor",
                         command=lambda: [ikelti_failus(tree2, label_file), pasirinkt(remelis33, tree2)])
editorbutton.place(rely=0.75, relx=0.45)
mygtukas2 = tk.Button(file_remelis2, text="Help", command=lambda: information())
mygtukas2.place(rely=0.65, relx=0.75)

# Uzrasai
label_file = ttk.Label(file_remelis2, text="No File Selected")
label_file.place(rely=0, relx=0)

# Pagrindinis ir mazesnis (editor) Treeview
tree1 = ttk.Treeview(remelis1)
tree1.place(relheight=1, relwidth=1)
tree2 = ttk.Treeview(remelis3)
tree2.place(relheight=1, relwidth=1)

# Slankikliai
treescrolly = tk.Scrollbar(remelis1, orient="vertical", command=tree1.yview)
treescrollx = tk.Scrollbar(remelis1, orient="horizontal", command=tree1.xview)
tree1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
treescrollx.pack(side="bottom", fill="x")
treescrolly.pack(side="right", fill="y")
treescrolly2 = tk.Scrollbar(remelis3, orient="vertical", command=tree2.yview)
treescrollx2 = tk.Scrollbar(remelis3, orient="horizontal", command=tree2.xview)
tree2.configure(xscrollcommand=treescrollx2.set, yscrollcommand=treescrolly2.set)
treescrollx2.pack(side="bottom", fill="x")
treescrolly2.pack(side="right", fill="y")
show(file_remelis1, label_file)


def information():
    """
    Informacija paspaudus help mygtuka
    """
    tk.messagebox.showinfo("Information", f"This project created by Dovydas Skauminas as final project at CodeAcademy\n"
                                          f"Functionality:\n"
                                          f"1. To load a csv file you need to click on 'Browse a file' button and select a wanted csv file\n"
                                          f"2. Once you selected a file click 'Load file' button to see data in treeview\n"
                                          f"3. To open file in editor view click on 'Open file in editor'\n"
                                          f"4. To search enter a value in enty box and click 'Find' button\n"
                                          f"5. To delete click on cell you want to delete and click 'Delete' button\n"
                                          f"6. To add a new cell click on 'Add cell' button and enter values\n"
                                          f"7. To filter by wanted value click 'Show only' button and enter values\n"
                                          f"8. To edit cell double click on value and enter new value"
                                          f"9. To save edited treeview into CSV/SQL file click 'Save to CSV/SQL' button\n"
                                          f"10. To plot data click 'Show PlotMenu' button then seleck values and click 'Make a plot' button\n")


def editint(event):
    """
    Pakeisti lasteles duomenis
    """
    objektas = tree2.identify('item', event.x, event.y)
    stulpelis = tree2.identify_column(event.x)
    value = tree2.item(objektas, "values")[int(stulpelis[1]) - 1]
    naujas_value = simpledialog.askstring("Edit cell", "Enter the new value", initialvalue=value)
    if naujas_value:
        tree2.set(objektas, stulpelis, naujas_value)


tree2.bind("<Double-1>", editint)

root.mainloop()
