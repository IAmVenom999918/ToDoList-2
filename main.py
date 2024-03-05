import tkinter as tk
import customtkinter as ctk


def Main_Window_Loop():
    root_tk = tk.Tk()  # create the Tk window like you normally do
    root_tk.geometry("500x700")
    root_tk.title("To-Dos")
    root_tk.resizable(False, False)

    def New_Task_Button_Function():
        text = entry.get()
        print("button pressed")
        print(text)
        entry.delete(0, len(text))

    entry = ctk.CTkEntry(master=root_tk,
                               width=480,
                               height=25,
                               corner_radius=10
                               )
    entry.place(x=10,y=25)

    
    button = ctk.CTkButton(master=root_tk, corner_radius=10, command=New_Task_Button_Function, text="New Task")
    button.place(relx=0.5, y = 80, anchor=tk.CENTER)

    # label = ctk.CTkLabel(master=root_tk,
    #                             text="New Task :",
    #                             width=120,
    #                             height=25,
    #                             corner_radius=8)
    # label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    # Use CTkButton instead of tkinter Button

    root_tk.mainloop()

Main_Window_Loop()