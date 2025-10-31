import threading
from controllers.home_controller import HomeController


class DummyFacade:
    pass


def create_instance(results, index):
    inst = HomeController(DummyFacade(), agents=[], views=None)
    results[index] = id(inst)


def main():
    threads = []
    n = 10
    results = [None] * n

    for i in range(n):
        t = threading.Thread(target=create_instance, args=(results, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("IDs obtenidos desde threads:", results)
    unique_ids = set(results)
    print("IDs únicos:", unique_ids)
    if len(unique_ids) == 1:
        print("TEST PASSED: Solo existe una instancia de HomeController en todos los hilos.")
    else:
        print("TEST FAILED: Se crearon múltiples instancias.")


if __name__ == '__main__':
    main()
