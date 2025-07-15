import logging
import time


def log_args(fonction):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Appel {fonction.__name__} avec args={args} and kwargs={kwargs}")
        result = fonction(*args, **kwargs)
        end_time = time.time()
        print(f"{fonction.__name__} returned {result} in {end_time - start_time:.2f} seconds")
        return result
    return wrapper

@log_args
def facture_total(**kwargs):
    return sum(kwargs.values())


if __name__ == "__main__":
    print("Exécution du code dans le fichier principal.")