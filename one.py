import heapq

def min_cost_to_connect_cables(cable_lengths):
    # Створюємо мін-купу з початкового списку кабелів
    heapq.heapify(cable_lengths)
    
    # Змінна для збереження загальних витрат
    total_cost = 0
    
    # Об'єднуємо кабелі, поки не залишиться один
    while len(cable_lengths) > 1:
        # Витягуємо два найкоротші кабелі
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        
        # Об'єднуємо їх і додаємо витрати
        cost = first + second
        total_cost += cost
        
        # Додаємо новий кабель назад до купи
        heapq.heappush(cable_lengths, cost)
    
    return total_cost

# Приклад використання
cables = [5, 4, 1, 7]
print(min_cost_to_connect_cables(cables))  