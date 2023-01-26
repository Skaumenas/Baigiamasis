import tkinter as tk
from tkinter import filedialog, messagebox, ttk, simpledialog
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import csv

# pagrindinis langas jo dydis pavadinimas parametrai
# --------------------------------------------------
root = tk.Tk()
root.title("Baigimasis projektas")
root.geometry("1480x720")
root.pack_propagate(False)
root.resizable(0, 0)
# --------------------------------------------------


# -------------------------------------------------------------------------------------------------
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
mygtukas1 = tk.Button(file_remelis2, text="Browse A File", command=lambda: failo_narsykle())
mygtukas1.place(rely=0.65, relx=0.50)
mygtukas2 = tk.Button(file_remelis2, text="Load File", command=lambda: ikelti_failus(tree1))
mygtukas2.place(rely=0.65, relx=0.30)
editorbutton = tk.Button(remelis33, text="Open file in editor", command=lambda: [ikelti_failus(tree2), pasirinkt()])
editorbutton.place(rely=0.75, relx=0.45)
mygtukas2 = tk.Button(file_remelis2, text="Help", command=lambda: help())
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


def help():
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
                                          f"9. To save edited treeview into CSV file click 'Save to CSV' button\n"
                                          f"10. To plot data click 'Show PlotMenu' button then seleck values and click 'Make a plot' button\n")


# -------------------------------------------------------------------------------------------------
# Mygtukas ir label funkcijoje, del update galimybes
# -------------------------------------------------------------------------------------------------
def show():
    mygtukas3 = tk.Button(file_remelis1, text="Show PlotMenu",
                          command=lambda: [diagrama(), mygtukas3.destroy(), label.destroy()])
    mygtukas3.place(rely=0.8, relx=0.01)
    label = tk.Label(file_remelis1, text="Caution: Big datasets could take a while to create a plot\n"
                                         "If any of parameters is unwanted choose None\n"
                                         "Some plots won't be available with chosen parameters\n"
                                         "To save a plot click on 'Save a plot' button")
    label.place(rely=0.05, relx=0.30)


show()


# -------------------------------------------------------------------------------------------------


# Pakeisti lasteles duomenis
# -------------------------------------------------------------------------------------------------
def edit(event):
    objektas = tree2.identify('item', event.x, event.y)
    stulpelis = tree2.identify_column(event.x)
    value = tree2.item(objektas, "values")[int(stulpelis[1]) - 1]
    naujas_value = simpledialog.askstring("Edit cell", "Enter the new value", initialvalue=value)
    if naujas_value:
        tree2.set(objektas, stulpelis, naujas_value)


tree2.bind("<Double-1>", edit)


# -------------------------------------------------------------------------------------------------


# Funkcija kuri paspaudus mygtuka ijungs operacines sistemos failu narsykle
# -------------------------------------------------------------------------------------------------
def failo_narsykle():
    pavadinimas = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=(("csv files", "*.csv"), ("All Files", "*.*")))
    label_file["text"] = pavadinimas
    return None


# -------------------------------------------------------------------------------------------------

# Funkcija kuri paspaudus mygtuka ikelia visus csv duomenis i treeview perziura
# -------------------------------------------------------------------------------------------------
def ikelti_failus(arg):
    vieta = label_file["text"]
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


# -------------------------------------------------------------------------------------------------

# Funkcija turinti daug paskirciu, ji leidzia piesti plot ir pasirinkti pagal kokius duomenis piesti
# -------------------------------------------------------------------------------------------------
def diagrama():
    try:
        # mygtukai, label option menus
        csv = pd.read_csv(f"{label_file['text']}")
        tree6 = list(csv.columns)
        tree6.append("None")
        xlabel = tk.Label(file_remelis1, text="Choose X:")
        xlabel.place(rely=0.03, relx=0.01)
        ylabel = tk.Label(file_remelis1, text="Choose Y:")
        ylabel.place(rely=0.23, relx=0.01)
        huelabel = tk.Label(file_remelis1, text="Choose Hue:")
        huelabel.place(rely=0.43, relx=0.01)
        plotlabel = tk.Label(file_remelis1, text="Choose Plot:")
        plotlabel.place(rely=0.63, relx=0.01)
        clickedx = tk.StringVar()
        clickedx.set("None")
        drop1 = tk.OptionMenu(file_remelis1, clickedx, *tree6)
        drop1.place(rely=0, relx=0.11)
        clickedy = tk.StringVar()
        clickedy.set("None")
        drop2 = tk.OptionMenu(file_remelis1, clickedy, *tree6)
        drop2.place(rely=0.2, relx=0.11)
        clickedhue = tk.StringVar()
        clickedhue.set("None")
        drop3 = tk.OptionMenu(file_remelis1, clickedhue, *tree6)
        drop3.place(rely=0.4, relx=0.11)

        pasirinkimai = ["Scatter plot", "Bar plot", "Strip plot", "Swarm plot", "Box plot", "Violin plot",
                        "Histogram plot", "Joint plot", "Pair plot"]

        clicked1 = tk.StringVar()
        clicked1.set(pasirinkimai[0])
        drop4 = tk.OptionMenu(file_remelis1, clicked1, *pasirinkimai)
        drop4.place(rely=0.6, relx=0.11)

        mygtukas = tk.Button(file_remelis1, text="Clear OptionMenu", command=lambda: [istrink(), show()])
        mygtukas.place(rely=0.8, relx=0.01)

        def gauti():
            a = clickedx.get()
            if a == "None":
                a = None
            else:
                a = clickedx.get()

            b = clickedy.get()
            if b == "None":
                b = None
            else:
                b = clickedy.get()

            c = clickedhue.get()
            if c == "None":
                c = None
            else:
                c = clickedhue.get()

            a1 = clicked1.get()
            if a1 == "Scatter plot":
                sns.scatterplot(data=csv, x=a, y=b, hue=c)
                plt.show()
            elif a1 == "Bar plot":
                sns.barplot(data=csv, x=a, y=b, hue=c)
                plt.show()
            elif a1 == "Strip plot":
                sns.stripplot(data=csv, x=a, y=b, hue=c)
                plt.show()
            elif a1 == "Swarm plot":
                sns.swarmplot(data=csv, x=a, y=b, hue=c)
                plt.show()
            elif a1 == "Box plot":
                sns.boxplot(data=csv, x=a, y=b, hue=c)
                plt.show()
            elif a1 == "Violin plot":
                sns.violinplot(data=csv, x=a, y=b, hue=c)
                plt.show()
            elif a1 == "Histogram plot":
                sns.histplot(data=csv, x=a, y=b, hue=c)
                plt.show()
            elif a1 == "Joint plot":
                sns.jointplot(data=csv, x=a, y=b)
                plt.show()
            elif a1 == "Pair plot":
                sns.pairplot(csv)
                plt.show()

        diagramosbutton = tk.Button(file_remelis1, text="Make a plot", command=lambda: gauti())
        diagramosbutton.place(rely=0.8, relx=0.5)

        def istrink():
            xlabel.destroy()
            ylabel.destroy()
            huelabel.destroy()
            plotlabel.destroy()
            drop1.destroy()
            drop2.destroy()
            drop3.destroy()
            drop4.destroy()
            diagramosbutton.destroy()
            mygtukas.destroy()
    except FileNotFoundError:
        tk.messagebox.showerror("Information", "Select a file first")
        show()
        return None


# -------------------------------------------------------------------------------------------------

def clear_data():
    tree1.delete(*tree1.get_children())
    tree2.delete(*tree2.get_children())
    return None


# -------------------------------------------------------------------------------------------------
# Funkcija kuri paspaudus mygtuka Open file in editor atidaro faila i tree2 ir parodo Edit mygtukus
# -------------------------------------------------------------------------------------------------
def pasirinkt():
    add_button = tk.Button(remelis33, text="Add Cell", command=lambda: add_cell())
    add_button.place(rely=0.05, relx=0.55)
    labelis = tk.Label(remelis33, text="Search: ")
    labelis.place(rely=0.065, relx=0.03)
    find = tk.Button(remelis33, text="Find", command=lambda: find_object())
    find.place(rely=0.05, relx=0.4)
    delete = tk.Button(remelis33, text="Delete", command=lambda: delete_cell())
    delete.place(rely=0.05, relx=0.47)
    export_button = tk.Button(remelis33, text="Save to CSV", command=lambda: export_csv())
    export_button.place(rely=0.75, relx=0.65)
    filter_button = tk.Button(remelis33, text="Show only", command=filter_data)
    filter_button.place(rely=0.05, relx=0.65)
    entry = tk.Entry(remelis33)
    entry.place(height=25, width=200, rely=0.06, relx=0.10)

    # -------------------------------------------------------------------------------------------------
    # Surasti faila excel data editor label
    # -------------------------------------------------------------------------------------------------
    def find_object():
        paieska = entry.get()  # gauna teksta is entry
        for i in tree2.get_children():
            duomenys = tree2.item(i)
            reiksme = duomenys.get("values")
            if paieska in reiksme:
                tree2.see(i)  # numeta i vieta kurioje yra objektas
                tree2.selection_set(i)  # parenka objekta
                return
        messagebox.showerror("Error", "Object not found.")


# -------------------------------------------------------------------------------------------------
# Funkcija kuri leidzia pasinikta lastele tree2 treeview, paspaudus Delete mygtuka, istrina lastele
# -------------------------------------------------------------------------------------------------
def delete_cell():
    pasirinkimas = tree2.selection()
    if not pasirinkimas:
        messagebox.showinfo("Error", "No cell is selected. Please select a cell to delete.")
    else:
        patvirtint = messagebox.askyesno("Delete cell", "Are you sure you want to delete the selected cell?")
        if patvirtint:
            gauti = tree2.parent(pasirinkimas)
            tree2.delete(pasirinkimas)
            if not tree2.get_children(gauti):
                tree2.delete(gauti)


# -------------------------------------------------------------------------------------------------
# Funkcija kuri leidzia issaugoti tree2 treeview esancius duomenis i csv faila
# -------------------------------------------------------------------------------------------------
def export_csv():
    pavadinimas = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")])
    if pavadinimas:
        with open(pavadinimas, 'w', newline='') as f:
            writer = csv.writer(f)
            duomenys = [tree2.heading(col, option='text') for col in tree2['columns']]
            writer.writerow(duomenys)
            for row in tree2.get_children():
                reiksmes = [tree2.set(row, col) for col in tree2['columns']]
                writer.writerow(reiksmes)
        messagebox.showinfo("Success", "Data saved successfully to " + pavadinimas)


# -------------------------------------------------------------------------------------------------
# Funkcija leidzianti paspaudus Add cell mygtuka prideti nauja lastele tree2 treeview
# -------------------------------------------------------------------------------------------------
def add_cell():
    nauji_duomenys = simpledialog.askstring("Add cell", "Enter the values for the new row, separated by commas")
    if nauji_duomenys:
        new_values = nauji_duomenys.split(",")
        tree2.insert("", "end", values=new_values)


# -------------------------------------------------------------------------------------------------
# Funkcija kuri atvaizuoja tik ivestus duomenis
# -------------------------------------------------------------------------------------------------
def filter_data():
    stulpelis = simpledialog.askstring("Show data", "Enter the column name")
    reiksme = simpledialog.askstring("Show data", "Enter the value")
    if stulpelis and reiksme:
        for row in tree2.get_children():
            values = tree2.set(row, stulpelis)
            if values != reiksme:
                tree2.delete(row)


root.mainloop()
