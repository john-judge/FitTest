
from source.field import Field


class Position:

    def __init__(self, position_name, default_value, bounds):
        self.name = position_name
        self.x = Field(position_name + "_x", default_value=default_value[0], bounds=bounds[0])
        self.y = Field(position_name + "_y", default_value=default_value[1], bounds=bounds[1])


class DynamicFitUnit:

    def __init__(self, saddle_default, handlebars_default, saddle_bounds, handlebars_bounds, step_size):
        self.saddle = Position("Saddle", saddle_default, saddle_bounds)
        self.handlebars = Position("Handlebars", handlebars_default, handlebars_bounds)
        self.step_size = step_size

    def get_fields(self):
        return [self.saddle.x, self.saddle.y, self.handlebars.x, self.handlebars.y]

    # calculate stack
    def get_stack(self):
        return self.handlebars.y

    # calculate reach
    def get_reach(self):
        return self.handlebars.x