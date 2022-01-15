
from source.field import Field


class Position:

    def __init__(self, position_name, default_value):
        self.name = position_name
        self.x = Field(position_name + "_x", default_value=default_value[0])
        self.y = Field(position_name + "_y", default_value=default_value[1])


class DynamicFitUnit:

    def __init__(self, saddle_default, handlebars_default):
        self.saddle = Position("Saddle", saddle_default)
        self.handlebars = Position("Handlebars", handlebars_default)

    def get_fields(self):
        return [self.saddle.x, self.saddle.y, self.handlebars.x, self.handlebars.y]
