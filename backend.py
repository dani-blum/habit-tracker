# Backend: Gerencia a lógica e os dados dos hábitos
class HabitManager:
    def __init__(self):
        self.habits = []

    def add_habit(self, name, description, frequency):
        """Adiciona um novo hábito."""
        if not name:
            return {"error": "O nome do hábito é obrigatório."}
        
        habit = {
            "name": name,
            "description": description.strip(),
            "frequency": frequency,
        }
        self.habits.append(habit)
        return {"success": True}

    def get_habits(self):
        """Retorna a lista de hábitos."""
        return self.habits
