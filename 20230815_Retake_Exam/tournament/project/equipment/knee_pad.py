from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    PROTECTION = 120
    PRICE = 15.0
    PERCENT = 20

    def __init__(self):
        super().__init__(protection=self.PROTECTION, price=self.PRICE)