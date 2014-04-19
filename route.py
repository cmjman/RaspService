from tornado_rest_handler import routes, rest_routes
from model.base import *
from handlers.user import *
from handlers.sensor import *
from handlers.switch import *
from handlers.task import *

Prefix = "service/"

TORNADO_ROUTES = [

    rest_routes(User, prefix = Prefix + "user",  handler = UserHandler),
    rest_routes(Sensor, prefix = Prefix +"sensor", handler = SensorHandler),
    rest_routes(SensorData, prefix = Prefix+r"sensorDatas/(.*)", handler = SensorDataHandler),
    rest_routes(Switch, prefix = Prefix + "switch", handler = SwitchHandler),
    rest_routes(Task, prefix = Prefix + "task", handler = TaskHandler)
]

TORNADO_SETTINGS = {}

application = tornado.web.Application(routes(TORNADO_ROUTES), **TORNADO_SETTINGS)
