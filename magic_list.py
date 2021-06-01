from dataclasses import dataclass


@dataclass
class Person:
    age: int = 1


class MagicList:
    def __init__(self, cls_type=None):
        self.collection = []
        self.cls_type = cls_type
        self.delta = 0

    def __repr__(self):
        return f"Items: {repr(self.collection)}, Default: {self.cls_type}"

    def __getitem__(self, index):
        if self.cls_type:
            # Empty list case
            if not self.collection:
                self.delta = index
                self._append_item(0)
                return self.collection[-1]

            # Populated list case
            else:
                real_index = index - self.delta
                # negative index
                if real_index < 0:
                    raise IndexError("Index out of bound")
                # next element
                elif real_index == len(self.collection):
                    self._append_item(0)
                    return self.collection[-1]
                # get element in list
                elif real_index < len(self.collection):
                    return self.collection[real_index]
                # index non continuous
                else:
                    raise IndexError("Indexes must be continuous")

        return self.collection[index]

    def __setitem__(self, index, value):
        # Empty list case
        if not self.collection:
            self.delta = index
            self._append_item(value)

        # Populated list case
        else:
            real_index = index - self.delta
            # negative index
            if real_index < 0:
                raise IndexError("Index out of bound")
            # next element
            elif real_index == len(self.collection):
                self._append_item(value)
            # change element in list
            elif real_index < len(self.collection):
                self.collection[real_index] = value
            # index non continuous
            else:
                raise IndexError("Indexes must be continuous")

    def _append_item(self, value):
        self.collection.append(self.cls_type(value) if self.cls_type else value)
