import time
from typing import Any, Callable

PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8

GenreSalesData = list[dict[str, str | float]]  # data about revenue

def performance_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator that measures and logs the execution time of a function.

    Args:
        func: The function whose performance needs to be tracked.

    Returns:
        A wrapper function  executes the inner function and prints its execution time.
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        execution_time = time.perf_counter() - start_time

        print(
            f"{PERFORMANCE_LOG_PREFIX} Функция '{func.__name__}' "
            f"выполнена за {execution_time:.{TIME_DECIMALS}f} сек."
        )
        return result

    return wrapper

@performance_logger
def get_sorted_report(data: GenreSalesData) -> GenreSalesData:
    """
    Sorts genre sales records by revenue in descending order.

    Args:
        data: A list of dictionaries containing genre categories and sales metrics.

    Returns:
        A new list of sales records sorted by the total sales amount from
        highest to lowest.
    """

    return sorted(data, key=lambda x: float(x["total_sales"]), reverse=True)

test_set_1: GenreSalesData = [
        {"category": "Action", "total_sales": 4311.85},
        {"category": "Animation", "total_sales": 4656.30},
        {"category": "Children", "total_sales": 3655.55},
]

test_set_2: GenreSalesData = [
        {"category": "Classics", "total_sales": 1200.10},
        {"category": "Comedy", "total_sales": 4000.00},
        {"category": "Documentary", "total_sales": 4000.00},
]

test_set_3: GenreSalesData = [
        {"category": "Drama", "total_sales": 500.00}
]

tests = [test_set_1, test_set_2, test_set_3]
print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")

for id, test_data in enumerate(tests, 1):
    print(f"--- ТЕСТ {id} ---")
    sorted_report = get_sorted_report(test_data)

    print("Топ категорий по выручке:")
    for rank, item in enumerate(sorted_report, 1):
        print(f"{rank}. {item['category']}: {item['total_sales']}")
