import json
from json import JSONEncoder


class FileEncoder(JSONEncoder):
    def default(self, o):
        # if type(o) == np.ndarray:
        #     return o.tolist()
        return o.__dict__


class Field:

    def __init__(self, field_name, default_value=0, gui_element=None, bounds=None):
        self.field_name = field_name  # identifier for this data field

        self.value = default_value
        self.gui_element = gui_element
        self.hardware = None

        # Numeric validation
        self.bounds = bounds
        if self.bounds is None:
            self.bounds = [-2500, 2500]

    def get_upper_bound(self):
        return self.bounds[1]

    def get_lower_bound(self):
        return self.bounds[0]

    def set_value(self, val):
        if self.gui_element is not None:
            self.gui_element.update(val)
        self.value = val

    def get_value(self):
        return self.value

    def increment_value(self, amount=1):
        new_val = int(self.get_value() + amount)
        if self.get_upper_bound() is not None:
            if new_val > self.get_upper_bound():
                new_val = self.get_upper_bound()
        actual_amount = new_val - self.get_value()
        if actual_amount > 0:
            self.set_value(new_val)
            self.hardware.increment_position(self.field_name, millmeters=actual_amount)

    def decrement_value(self, amount=1):
        new_val = int(self.get_value() - amount)
        if self.get_lower_bound() is not None:
            if new_val < self.get_lower_bound():
                new_val = self.get_lower_bound()
        actual_amount = self.get_value() - new_val
        if actual_amount > 0:
            self.set_value(new_val)
            self.hardware.decrement_position(self.field_name, millimeters=actual_amount)


class EventMapping:

    def __init__(self, dfu):
        self.dfu = dfu
        self.fields = dfu.get_fields()

    def handle_event(self, event_name):
        field_name = event_name[:-1]
        found = False
        if event_name.endswith('-'):
            found = self.decrement_field(field_name)
        elif event_name.endswith('+'):
            found = self.increment_field(field_name)
        if not found:
            print("Event not found:", event_name)

    def saturate_lower_limits(self, field_names, bounds):
        for i in range(len(field_names)):
            range_length = bounds[i][1] - bounds[i][0]
            self.decrement_field(field_names[i], range_length)

    def snap_to_measurement(self, field_names, curr_positions, new_positions):
        for i in range(len(field_names)):
            move_amount = new_positions[i] - curr_positions[i]
            print("Snap", field_names[i], "by", move_amount)
            if move_amount > 0:
                self.increment_field(field_names[i], move_amount)
            elif move_amount < 0:
                self.decrement_field(field_names[i], -1 * move_amount)

    def decrement_field(self, field_name, amount=None):
        if amount is None:
            amount = self.dfu.step_size
        for f in self.fields:
            if f.field_name == field_name:
                f.decrement_value(amount=amount)
                return True
        return False

    def increment_field(self, field_name, amount=None):
        if amount is None:
            amount = self.dfu.step_size
        for f in self.fields:
            if f.field_name == field_name:
                f.increment_value(amount=amount)
                return True
        return False

    def export_file(self, filename):
        json = self.export_fields_json()
        self.dump_python_object_to_json(filename, json)

    def import_file(self, filename):
        json = self.retrieve_python_object_from_json(filename)
        if json is not None:
            self.import_fields_json(json)

    # fetch current field values and return in same order as list arg
    def get_curr_field_values(self, field_names):
        vals = []
        for f_name in field_names:
            for f in self.fields:
                if f.field_name == f_name:
                    vals.append(f.get_value())
        return vals

    def import_fields_json(self, field_json):
        for f in self.fields:
            if f.field_name in field_json:
                f.set_value(field_json[f.field_name])

    def export_fields_json(self):
        field_json = {}
        for f in self.fields:
            field_json[f.field_name] = f.get_value()
        return field_json

    @staticmethod
    def retrieve_python_object_from_json(filename):
        try:
            f = open(filename)
            obj = json.load(f)
            if type(obj) == str:
                obj = json.loads(obj)
            f.close()
            return obj
        except Exception as e:
            print("could not load file:", filename)
            print(e)

    @staticmethod
    def dump_python_object_to_json(filename, obj):
        with open(filename, 'w') as f:
            json.dump(obj, f, cls=FileEncoder)