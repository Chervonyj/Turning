class TuringMachine:
    def __init__(self, tape, initial_state, final_states, transition_function):
        self.tape = list(tape)  # Лента с входными данными
        self.head_position = 0  # Начальная позиция головки
        self.current_state = initial_state  # Начальное состояние
        self.final_states = final_states  # Множество конечных состояний
        self.transition_function = transition_function  # Таблица переходов

    def step(self):
        # Получаем текущий символ под головкой
        current_symbol = self.tape[self.head_position]
        
        # Если текущее состояние и символ есть в таблице переходов
        if (self.current_state, current_symbol) in self.transition_function:
            # Получаем новое состояние, символ для записи и направление движения
            new_state, write_symbol, move_direction = self.transition_function[(self.current_state, current_symbol)]
            
            # Записываем новый символ на ленту
            self.tape[self.head_position] = write_symbol
            
            # Обновляем текущее состояние
            self.current_state = new_state
            
            # Двигаем головку влево или вправо
            if move_direction == 'R':
                self.head_position += 1
            elif move_direction == 'L':
                self.head_position -= 1
        else:
            raise Exception("Transition not defined for this state and symbol")

    def run(self):
        while self.current_state not in self.final_states:
            self.step()
        return ''.join(self.tape)

# Определяем таблицу переходов для нашей машины
transition_function = {
    ('q0', 'a'): ('q0', 'x', 'R'),  # В состоянии q0, если видим 'a', заменяем на 'x' и двигаемся вправо
    ('q0', 'b'): ('q0', 'b', 'R'),  # В состоянии q0, если видим 'b', оставляем 'b' и двигаемся вправо
    ('q0', '_'): ('qf', '_', 'R')   # В состоянии q0, если видим пустой символ '_', переходим в конечное состояние qf
}

# Создаём экземпляр Машины Тюринга с начальной лентой, начальным состоянием и конечными состояниями
turing_machine = TuringMachine(tape="aabbaa_", initial_state='q0', final_states={'qf'}, transition_function=transition_function)

# Запускаем машину и выводим результат
output = turing_machine.run()
print(output)  # Ожидаемый результат: "xxbbxx_"