from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    PROTECTION = 90
    PRICE = 25.0
    PERCENT = 10

    def __init__(self):
        super().__init__(protection=self.PROTECTION, price=self.PRICE)
