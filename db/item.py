import xml.dom.minidom

from peewee import *

from db.db import db
from metadata.progression_items import progression_items
from metadata.item_general import unused_items, unplaceable_items
from enums import Enums


class Item(Model):
    # keyitem, badge etc
    item_type = CharField(null=True)
    # item byte value as int (eg 348 = 0x15c (StarPiece))
    value = IntegerField()
    # actual item name w/o spaces or apostrophe
    item_name = CharField()
    # base sell price of the item
    base_price = IntegerField()
    # True if item can be required to reach locations
    progression = BooleanField(default=False)
    # Is the item unused in the vanilla game, but functional
    unused = BooleanField(default=False)
    # Is the item unintended to be placed in the world and could break things,
    # or is unused but non-functional
    unplaceable = BooleanField(default=False)

    def __str__(self):
        return f"{self.item_name} ({self.item_type})[{hex(self.value)}]"

    def is_trapped(self):
        trap_flag = 0x2000
        return self.value & trap_flag == trap_flag

    @classmethod
    def get_type(cls, item_id:int):
        if 0x00 == item_id:
            return "NOTHING"
        elif 0x07 <= item_id <= 0x7F or (0x16D <= item_id <= 0x17E):
            return "KEYITEM"
        elif 0x80 <= item_id <= 0xDF or 0x1DC <= item_id <= 0x1E4:
            return "ITEM"
        elif 0xE0 <= item_id <= 0x155 or 0x1EB <= item_id <= 0x1F9:
            return "BADGE"
        elif 0x156 <= item_id <= 0x15C:
            return {
                0x156: "HEART",
                0x157: "COIN",
                0x159: "STARPOINT",
                0x15A: "FULLHEAL",
                0x15B: "FLOWER",
                0x15C: "STARPIECE",
            }.get(item_id)
        elif 0x185 <= item_id <= 0x1DB:
            return "STARPIECE"
        elif 0x1E5 <= item_id <= 0x1EA:
            return "GEAR"
        elif 0x1FF <= item_id <= 0x207:
            return "PARTNER"
        else:
            return "OTHER"

    class Meta:
        database = db


# Run this to create all items in Item table
def create_items():
    db.drop_tables([Item])
    db.create_tables([Item])

    items_doc = xml.dom.minidom.parse("../../globals/Items.xml")
    # need index (itemid), sell value
    item_data = []
    for item in items_doc.getElementsByTagName("Item"):
        item_index = item.getAttribute("index")
        item_sell_value = item.getAttribute("sellValue")
        if item_sell_value is None or item_sell_value == "":
            item_sell_value = "50"
        item_data.append(
            {
                "Index": item_index,
                "Sell Value": item_sell_value
            }
        )

    for item in item_data:
        item_id = int(item["Index"], 16)
        if item_id == 0x18:
            # Ignore fake Volcano Vase
            continue
        item_name = Enums.get("Item")[item_id]
        base_price = int(item["Sell Value"], 10) if item["Sell Value"] != "FFFF" else 50
        if "BubbleBerryProxy" in item_name:
            base_price = 3
        elif "BerryProxy" in item_name:
            base_price = 2
        item,_ = Item.get_or_create(
            item_type = Item.get_type(item_id),
            value = item_id,
            item_name = item_name,
            base_price = base_price,
            progression = (Item.get_type(item_id) in ["KEYITEM","PARTNER"] and item_id in progression_items.keys()),
            unused = item_name in unused_items,
            unplaceable = item_name in unplaceable_items
        )
