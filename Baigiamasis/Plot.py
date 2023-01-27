import tkinter as tk
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def diagrama(arg1, arg2):
    """
    Funkcija leidzia piesti plot ir pasirinkti pagal kokius duomenis piesti
    """
    try:
        # mygtukai, label option menus
        csv = pd.read_csv(f"{arg2['text']}")
        tree6 = list(csv.columns)
        tree6.append("None")
        xlabel = tk.Label(arg1, text="Choose X:")
        xlabel.place(rely=0.03, relx=0.01)
        ylabel = tk.Label(arg1, text="Choose Y:")
        ylabel.place(rely=0.23, relx=0.01)
        huelabel = tk.Label(arg1, text="Choose Hue:")
        huelabel.place(rely=0.43, relx=0.01)
        plotlabel = tk.Label(arg1, text="Choose Plot:")
        plotlabel.place(rely=0.63, relx=0.01)
        clickedx = tk.StringVar()
        clickedx.set("None")
        drop1 = tk.OptionMenu(arg1, clickedx, *tree6)
        drop1.place(rely=0, relx=0.11)
        clickedy = tk.StringVar()
        clickedy.set("None")
        drop2 = tk.OptionMenu(arg1, clickedy, *tree6)
        drop2.place(rely=0.2, relx=0.11)
        clickedhue = tk.StringVar()
        clickedhue.set("None")
        drop3 = tk.OptionMenu(arg1, clickedhue, *tree6)
        drop3.place(rely=0.4, relx=0.11)

        pasirinkimai = ["Scatter plot", "Bar plot", "Strip plot", "Swarm plot", "Box plot", "Violin plot",
                        "Histogram plot", "Joint plot", "Pair plot"]

        clicked1 = tk.StringVar()
        clicked1.set(pasirinkimai[0])
        drop4 = tk.OptionMenu(arg1, clicked1, *pasirinkimai)
        drop4.place(rely=0.6, relx=0.11)

        mygtukas = tk.Button(arg1, text="Clear OptionMenu", command=lambda: [istrink(), show(arg1, arg2)])
        mygtukas.place(rely=0.8, relx=0.01)

        def gauti():
            """
            Funkcija kuri gauna is vartotojo paspausta reiksme
            """
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

        diagramosbutton = tk.Button(arg1, text="Make a plot", command=lambda: gauti())
        diagramosbutton.place(rely=0.8, relx=0.5)

        def istrink():
            """
            Istrina pries tai esancius widgets
            """
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
        show(arg1, arg2)
        return None


def show(arg1, arg2):
    """
    Mygtukas ir label funkcijoje, del update galimybes
    """
    mygtukas3 = tk.Button(arg1, text="Show PlotMenu",
                          command=lambda: [diagrama(arg1, arg2), mygtukas3.destroy(), label.destroy()])
    mygtukas3.place(rely=0.8, relx=0.01)
    label = tk.Label(arg1, text="Caution: Big datasets could take a while to create a plot\n"
                                "If any of parameters is unwanted choose None\n"
                                "Some plots won't be available with chosen parameters\n"
                                "To save a plot click on 'Save a plot' button")
    label.place(rely=0.05, relx=0.30)
