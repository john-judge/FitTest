
from source.field import Field


class Position:

    def __init__(self, position_name, default_value):
        self.name = position_name
        self.x = Field(position_name + "_x", default_value=default_value[0])
        self.y = Field(position_name + "_y", default_value=default_value[1])


class DynamicFitUnit:

    def __init__(self):
        self.saddle = Position("Saddle", [0, 0])
        self.handlebars = Position("Handlebars", [0, 0])

    def get_fields(self):
        return [self.saddle.x, self.saddle.y, self.handlebars.x, self.handlebars.y]
