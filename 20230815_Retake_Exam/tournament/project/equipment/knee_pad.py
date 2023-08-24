from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    PERCENT = 20

    def __init__(self):
        super().__init__(protection=120, price=15)
