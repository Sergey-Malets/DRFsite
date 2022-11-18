from rest_framework import routers


class MyCustomRouter(routers.SimpleRouter):
    routes = [
        routers.Route(url=r'^{prefix}$',  #шаблон маршрута, можно использ регулярное выражение
                      mapping={'get': 'list'},  #связывает тип запроса с сооответствующим методом ViewSet
                      name='{basename}-list',  # определяет название маршрута
                      detail=False,  #false - список, true- отдельная запись
                      initkwargs={'suffix': 'List'}),  #дополнительные аргументы для колл-ции kwargs, кот. передаются
                                            # конкретному определению при срабатыванию маршрута
        routers.Route(url=r'^{prefix}/{lookup}$',
                      mapping={'get': 'retrieve'},
                      name='{basename}-detail',
                      detail=True,
                      initkwargs={'suffix': 'Detail'})
    ]