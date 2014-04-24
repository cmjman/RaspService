from tornado_rest_handler import routes, rest_routes

TORNADO_ROUTES = [

    rest_routes(User, handler = UserHandler),
    rest_routes(Sensor, handler = SensorHandler),
    rest_routes(SensorData, handler = SensorDataHandler),
    rest_routes(Switch, handler = SwitchHandler),
    rest_routes(Task, handler = TaskHandler)
]

TORNADO_SETTINGS = {}

application = tornado.web.Application(routes(TORNADO_ROUTES), **TORNADO_SETTINGS)
