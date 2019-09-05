class Router:
    METHODS = (
        "GET",
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
        "OPTIONS",
    )
    database = list()

    def __init__(self, *x):
        self.x = x

    def __getattr__(self, attribute):
        if attribute.upper() in self.METHODS:
            return lambda path: self.request(attribute.upper(), path)
        raise AttributeError(f" instance has not {attribute} attribute")

    def add_path(self, path, attribute, info):
        list_of_data = path, attribute, info
        database = self.database.append(list_of_data)
        return f"ok, path - \"{path}\", attribute - " \
            f"\"{attribute}\" was include"

    def my_info(self, attribute, path):
        return 200, {"me": "Joanne"}

    def request(self, method, path):
        if path not in ([(el[0]) for el in router.database]):
            return f"Error 404: {path} not found"
        elif method not in self.METHODS:
            return f"Error 405: Method{method} not Allowed"
        return router.my_info(method, path)


def get(self, path=None):
    print("self for get", self)
    return router.my_info(path)


if __name__ == "__main__":
    router = Router()
    print(router.add_path("/av", "GET", "cancan"))
    print(router.add_path("/am", "GIVEN", "name"))
    print(router.get("/am"))
    print(router.request('GET', '/me'))
    print(router.get("/us"))
    # print(router.prg("/am"))