from typing import Any

DEFAULT_RETURN_INDEX_BASE = 10.0

def calculate_overdue_fine(
    movie_title: str, days_overdue: Any, fine_rate: float
) -> tuple[float, float] | None:
    """Calculates the overdue fine and internal return index metrics for a rental.

    Args:
        movie_title: The title of the rented movie.
        days_overdue: The number of days the movie return is late. Can accept
        numeric values or alternative types for safe parsing.
        fine_rate: The financial charge rate per overdue day.

    Returns:
        A tuple containing:
            - total_fine (float): The total accumulated fine amount.
            - return_index (float): A calculated score based on days.
        Returns None if an arithmetic exception or invalid argument type parsing occurs.
    """

    try:
        numeric_days = float(days_overdue)
        total_fine = numeric_days * fine_rate
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days

        print(f"Фильм: '{movie_title}' | Итоговый штраф: {total_fine}$ | Индекс: {return_index}")

        return total_fine, return_index

    except ZeroDivisionError as e:
        print(
            f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для "
            f"'{movie_title}': {e}"
        )
        return None

    except ValueError as e:
        print(
            f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для "
            f"'{movie_title}': {e}"
        )
        return None

    except TypeError as e:
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для '{movie_title}': {e}")
        return None

    finally:
        print("--- Проверка транзакции возврата завершена ---")



test_cases = [
    {"title": "Matrix", "days": 5, "rate": 1.5},
    {"title": "Inception", "days": "пять", "rate": 2.0},
    {"title": "Avatar", "days": 0, "rate": 2.5},
    {"title": "Interstellar", "days":[3,], "rate": 3.0},
]

print("=== ПРОВЕРКА ВОЗВРАТОВ ===")

for case in test_cases:
    calculate_overdue_fine(case["title"], case["days"], case["rate"])
