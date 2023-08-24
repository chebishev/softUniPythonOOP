from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    PERCENT = 10

    def __init__(self):
        super().__init__(protection=90, price=25)
