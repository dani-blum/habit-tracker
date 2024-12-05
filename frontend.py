import tkinter as tk
from tkinter import messagebox
from backend import HabitManager  # Importa o backend

# Instancia o gerenciador de hábitos
habit_manager = HabitManager()

def add_habit():
    """Adiciona um hábito usando o backend."""
    name = entry_name.get()
    description = entry_description.get("1.0", "end")
    frequency = frequency_var.get()

    result = habit_manager.add_habit(name, description, frequency)
    if "error" in result:
        messagebox.showwarning("Erro", result["error"])
    else:
        update_habit_list()
        clear_inputs()

def update_habit_list():
    """Atualiza a lista de hábitos exibida."""
    listbox_habits.delete(0, tk.END)
    for habit in habit_manager.get_habits():
        listbox_habits.insert(tk.END, f"{habit['name']} ({habit['frequency']}): {habit['description']}")

def clear_inputs():
    """Limpa os campos de entrada."""
    entry_name.delete(0, tk.END)
    entry_description.delete("1.0", tk.END)
    frequency_var.set("Diário")

# Configuração da interface principal
root = tk.Tk()
root.title("Habit Tracker")
root.geometry("500x400")
root.resizable(False, False)

# Título
title = tk.Label(root, text="Habit Tracker", font=("Arial", 18), fg="#4CAF50")
title.pack(pady=10)

# Formulário
frame_form = tk.Frame(root)
frame_form.pack(pady=10)

# Campo Nome
label_name = tk.Label(frame_form, text="Nome do Hábito:", font=("Arial", 12))
label_name.grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_name = tk.Entry(frame_form, width=40)
entry_name.grid(row=0, column=1, padx=5, pady=5)

# Campo Descrição
label_description = tk.Label(frame_form, text="Descrição:", font=("Arial", 12))
label_description.grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_description = tk.Text(frame_form, width=30, height=4)
entry_description.grid(row=1, column=1, padx=5, pady=5)

# Frequência
label_frequency = tk.Label(frame_form, text="Frequência:", font=("Arial", 12))
label_frequency.grid(row=2, column=0, sticky="w", padx=5, pady=5)
frequency_var = tk.StringVar(value="Diário")
dropdown_frequency = tk.OptionMenu(frame_form, frequency_var, "Diário", "Semanal", "Mensal")
dropdown_frequency.grid(row=2, column=1, sticky="w", padx=5, pady=5)

# Botão Adicionar
button_add = tk.Button(root, text="Adicionar Hábito", font=("Arial", 12), bg="#4CAF50", fg="white", command=add_habit)
button_add.pack(pady=10)

# Lista de Hábitos
listbox_habits = tk.Listbox(root, width=70, height=10, font=("Arial", 10))
listbox_habits.pack(pady=10)

# Rodapé
footer = tk.Label(root, text="Criado com Python e Tkinter", font=("Arial", 8), fg="gray")
footer.pack(pady=10)

# Inicia o loop principal
root.mainloop()
