"""
Модуль розрахунку розрахункового часу доставки (ETA).
Автор: Наконечний Владислав, група 3-41 (Варіант 8)
"""

def eta_hours(distance_km: float, express: bool = False) -> float:
    if distance_km < 0:
        raise ValueError("Відстань не може бути від'ємною")

    full_100km = int(distance_km // 100)
    total_hours = 24 + full_100km

    if express:
        total_hours = max(4.0, total_hours / 2.0)

    return float(total_hours)
