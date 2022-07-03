"""This file represents all edges of the world graph that have origin-nodes in the KZN (Mt. Lavalava) area."""
edges_kzn = [
    # KZN_01 Volcano Entrance
    {"from": {"map": "KZN_01", "id": 0}, "to": {"map": "JAN_22", "id": 2}, "reqs": []}, # Volcano Entrance Exit West (Volcano Entrance) -> Path to the Volcano Exit Right
    {"from": {"map": "KZN_01", "id": 1}, "to": {"map": "KZN_02", "id": 0}, "reqs": []}, # Volcano Entrance Exit East -> First Lava Lake Exit West
    
    {"from": {"map": "KZN_01", "id": 0}, "to": {"map": "KZN_01", "id": 1}, "reqs": []}, #? Volcano Entrance Exit West (Volcano Entrance) -> Volcano Entrance Exit East
    {"from": {"map": "KZN_01", "id": 1}, "to": {"map": "KZN_01", "id": 0}, "reqs": []}, #? Volcano Entrance Exit East -> Volcano Entrance Exit West (Volcano Entrance)

    # KZN_02 First Lava Lake
    {"from": {"map": "KZN_02", "id": 0}, "to": {"map": "KZN_01", "id": 1}, "reqs": []}, # First Lava Lake Exit West -> Volcano Entrance Exit East
    {"from": {"map": "KZN_02", "id": 1}, "to": {"map": "KZN_03", "id": 0}, "reqs": []}, # First Lava Lake Exit East -> Central Cavern Exit West Upper
    
    {"from": {"map": "KZN_02", "id": 0}, "to": {"map": "KZN_02", "id": 1}, "reqs": []}, #? First Lava Lake Exit West -> First Lava Lake Exit East
    {"from": {"map": "KZN_02", "id": 1}, "to": {"map": "KZN_02", "id": 0}, "reqs": []}, #? First Lava Lake Exit East -> First Lava Lake Exit West

    # KZN_03 Central Cavern
    {"from": {"map": "KZN_03", "id": 0}, "to": {"map": "KZN_02", "id": 1}, "reqs": []}, # Central Cavern Exit West Upper -> First Lava Lake Exit East
    {"from": {"map": "KZN_03", "id": 1}, "to": {"map": "KZN_04", "id": 0}, "reqs": []}, # Central Cavern Exit East Upper -> Fire Bar Bridge Exit West
    {"from": {"map": "KZN_03", "id": 2}, "to": {"map": "KZN_09", "id": 0}, "reqs": []}, # Central Cavern Exit East Lower 1 (Ultra Block) -> Zipline Cavern Exit West Upper
    {"from": {"map": "KZN_03", "id": 3}, "to": {"map": "KZN_05", "id": 1}, "reqs": []}, # Central Cavern Exit West Lower -> Descent Toward Ultra Hammer Exit East
    {"from": {"map": "KZN_03", "id": 4}, "to": {"map": "KZN_09", "id": 2}, "reqs": []}, # Central Cavern Exit East Lower 2 -> Zipline Cavern Exit West Lower
    
    {"from": {"map": "KZN_03", "id": 0}, "to": {"map": "KZN_03", "id": 1}, "reqs": []}, #? Central Cavern Exit West Upper -> Central Cavern Exit East Upper
    {"from": {"map": "KZN_03", "id": 1}, "to": {"map": "KZN_03", "id": 0}, "reqs": []}, #? Central Cavern Exit East Upper -> Central Cavern Exit West Upper
    {"from": {"map": "KZN_03", "id": 0}, "to": {"map": "KZN_03", "id": 2}, "reqs": [["UltraHammer","RF_KZN07_OpenedHammerChest"]]}, #? Central Cavern Exit West Upper -> Central Cavern Exit East Lower 1 (Ultra Block)
    {"from": {"map": "KZN_03", "id": 2}, "to": {"map": "KZN_03", "id": 0}, "reqs": []}, #? Central Cavern Exit East Lower 1 (Ultra Block) -> Central Cavern Exit West Upper
    {"from": {"map": "KZN_03", "id": 0}, "to": {"map": "KZN_03", "id": 3}, "reqs": []}, #? Central Cavern Exit West Upper -> Central Cavern Exit West Lower
    {"from": {"map": "KZN_03", "id": 3}, "to": {"map": "KZN_03", "id": 0}, "reqs": []}, #? Central Cavern Exit West Lower -> Central Cavern Exit West Upper
    {"from": {"map": "KZN_03", "id": 0}, "to": {"map": "KZN_03", "id": 4}, "reqs": []}, #? Central Cavern Exit West Upper -> Central Cavern Exit East Lower 2
    {"from": {"map": "KZN_03", "id": 4}, "to": {"map": "KZN_03", "id": 0}, "reqs": []}, #? Central Cavern Exit East Lower 2 -> Central Cavern Exit West Upper
    
    {"from": {"map": "KZN_03", "id": 0},         "to": {"map": "KZN_03", "id": "ItemA"},   "reqs": []}, #* Central Cavern Exit West Upper -> ItemA (FireShield)
    {"from": {"map": "KZN_03", "id": "ItemA"},   "to": {"map": "KZN_03", "id": 0},         "reqs": []}, #* ItemA (FireShield) -> Central Cavern Exit West Upper
    {"from": {"map": "KZN_03", "id": 0},         "to": {"map": "KZN_03", "id": "ItemB"},   "reqs": [["Kooper","UltraBoots"]]}, #* Central Cavern Exit West Upper -> ItemB (POWBlock)
    {"from": {"map": "KZN_03", "id": "ItemB"},   "to": {"map": "KZN_03", "id": 0},         "reqs": []}, #* ItemB (POWBlock) -> Central Cavern Exit West Upper
    {"from": {"map": "KZN_03", "id": 0},         "to": {"map": "KZN_03", "id": "YBlockA"}, "reqs": []}, #* Central Cavern Exit West Upper -> YBlockA (Coin)
    {"from": {"map": "KZN_03", "id": "YBlockA"}, "to": {"map": "KZN_03", "id": 0},         "reqs": []}, #* YBlockA (Coin) -> Central Cavern Exit West Upper
    {"from": {"map": "KZN_03", "id": 0},         "to": {"map": "KZN_03", "id": "YBlockB"}, "reqs": []}, #* Central Cavern Exit West Upper -> YBlockB (Coin)
    {"from": {"map": "KZN_03", "id": "YBlockB"}, "to": {"map": "KZN_03", "id": 0},         "reqs": []}, #* YBlockB (Coin) -> Central Cavern Exit West Upper
    {"from": {"map": "KZN_03", "id": 0},         "to": {"map": "KZN_03", "id": "YBlockC"}, "reqs": []}, #* Central Cavern Exit West Upper -> YBlockC (Coin)
    {"from": {"map": "KZN_03", "id": "YBlockC"}, "to": {"map": "KZN_03", "id": 0},         "reqs": []}, #* YBlockC (Coin) -> Central Cavern Exit West Upper
    {"from": {"map": "KZN_03", "id": 0},         "to": {"map": "KZN_03", "id": "YBlockD"}, "reqs": []}, #* Central Cavern Exit West Upper -> YBlockD (Coin)
    {"from": {"map": "KZN_03", "id": "YBlockD"}, "to": {"map": "KZN_03", "id": 0},         "reqs": []}, #* YBlockD (Coin) -> Central Cavern Exit West Upper

    # KZN_04 Fire Bar Bridge
    {"from": {"map": "KZN_04", "id": 0}, "to": {"map": "KZN_03", "id": 1}, "reqs": []}, # Fire Bar Bridge Exit West -> Central Cavern Exit East Upper

    # KZN_05 Descent Toward Ultra Hammer
    {"from": {"map": "KZN_05", "id": 0}, "to": {"map": "KZN_06", "id": 0}, "reqs": []}, # Descent Toward Ultra Hammer Exit West -> Flowing Lava Puzzle Exit East Upper
    {"from": {"map": "KZN_05", "id": 1}, "to": {"map": "KZN_03", "id": 3}, "reqs": []}, # Descent Toward Ultra Hammer Exit East -> Central Cavern Exit West Lower
    
    {"from": {"map": "KZN_05", "id": 0}, "to": {"map": "KZN_05", "id": 1}, "reqs": []}, #? Descent Toward Ultra Hammer Exit West -> Descent Toward Ultra Hammer Exit East
    {"from": {"map": "KZN_05", "id": 1}, "to": {"map": "KZN_05", "id": 0}, "reqs": []}, #? Descent Toward Ultra Hammer Exit East -> Descent Toward Ultra Hammer Exit West

    # KZN_06 Flowing Lava Puzzle
    {"from": {"map": "KZN_06", "id": 0}, "to": {"map": "KZN_05", "id": 0}, "reqs": []}, # Flowing Lava Puzzle Exit East Upper -> Descent Toward Ultra Hammer Exit West
    {"from": {"map": "KZN_06", "id": 1}, "to": {"map": "KZN_07", "id": 0}, "reqs": []}, # Flowing Lava Puzzle Exit West -> Ultra Hammer Room Exit East
    {"from": {"map": "KZN_06", "id": 2}, "to": {"map": "KZN_08", "id": 0}, "reqs": []}, # Flowing Lava Puzzle Exit East Lower -> Dizzy Stomp Room Exit West
    
    {"from": {"map": "KZN_06", "id": 0}, "to": {"map": "KZN_06", "id": 1}, "reqs": [["Parakarry","Lakilester"]]}, #? Flowing Lava Puzzle Exit East Upper -> Flowing Lava Puzzle Exit West
    {"from": {"map": "KZN_06", "id": 1}, "to": {"map": "KZN_06", "id": 0}, "reqs": [["Parakarry","Lakilester"]]}, #? Flowing Lava Puzzle Exit West -> Flowing Lava Puzzle Exit East Upper
    {"from": {"map": "KZN_06", "id": 0}, "to": {"map": "KZN_06", "id": 2}, "reqs": [["UltraHammer","RF_KZN07_OpenedHammerChest"]]}, #? Flowing Lava Puzzle Exit East Upper -> Flowing Lava Puzzle Exit East Lower
    {"from": {"map": "KZN_06", "id": 2}, "to": {"map": "KZN_06", "id": 0}, "reqs": []}, #? Flowing Lava Puzzle Exit East Lower -> Flowing Lava Puzzle Exit East Upper
    
    {"from": {"map": "KZN_06", "id": 0},               "to": {"map": "KZN_06", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"]]}, #* Flowing Lava Puzzle Exit East Upper -> HiddenYBlockA (LifeShroom)
    {"from": {"map": "KZN_06", "id": "HiddenYBlockA"}, "to": {"map": "KZN_06", "id": 0},               "reqs": []}, #* HiddenYBlockA (LifeShroom) -> Flowing Lava Puzzle Exit East Upper

    # KZN_07 Ultra Hammer Room
    {"from": {"map": "KZN_07", "id": 0}, "to": {"map": "KZN_06", "id": 1}, "reqs": []}, # Ultra Hammer Room Exit East -> Flowing Lava Puzzle Exit West

    {"from": {"map": "KZN_07", "id": 0}, "to": {"map": "KZN_07", "id": 0}, "reqs": [["Parakarry","Lakilester","UltraHammer"]], "pseudoitems": ["EQUIPMENT_Hammer_Progressive_2","RF_KZN07_OpenedHammerChest"]}, #+ Open Ultra Hammer Chest

    # KZN_08 Dizzy Stomp Room
    {"from": {"map": "KZN_08", "id": 0}, "to": {"map": "KZN_06", "id": 2}, "reqs": []}, # Dizzy Stomp Room Exit West -> Flowing Lava Puzzle Exit East Lower
    
    {"from": {"map": "KZN_08", "id": 0},        "to": {"map": "KZN_08", "id": "ChestA"}, "reqs": [["Parakarry","Lakilester"]]}, #* Dizzy Stomp Room Exit West -> ChestA (DizzyStomp)
    {"from": {"map": "KZN_08", "id": "ChestA"}, "to": {"map": "KZN_08", "id": 0},        "reqs": []}, #* ChestA (DizzyStomp) -> Dizzy Stomp Room Exit West

    # KZN_09 Zipline Cavern
    {"from": {"map": "KZN_09", "id": 0}, "to": {"map": "KZN_03", "id": 2}, "reqs": []}, # Zipline Cavern Exit West Upper -> Central Cavern Exit East Lower 1 (Ultra Block)
    {"from": {"map": "KZN_09", "id": 1}, "to": {"map": "KZN_10", "id": 0}, "reqs": []}, # Zipline Cavern Exit East -> Descent Toward Boss Exit West
    {"from": {"map": "KZN_09", "id": 2}, "to": {"map": "KZN_03", "id": 4}, "reqs": []}, # Zipline Cavern Exit West Lower -> Central Cavern Exit East Lower 2
    
    {"from": {"map": "KZN_09", "id": 0}, "to": {"map": "KZN_09", "id": 1}, "reqs": []}, #? Zipline Cavern Exit West Upper -> Zipline Cavern Exit East
    {"from": {"map": "KZN_09", "id": 0}, "to": {"map": "KZN_09", "id": 2}, "reqs": []}, #? Zipline Cavern Exit West Upper -> Zipline Cavern Exit West Lower
    {"from": {"map": "KZN_09", "id": 1}, "to": {"map": "KZN_09", "id": 2}, "reqs": []}, #? Zipline Cavern Exit East -> Zipline Cavern Exit West Lower
    
    {"from": {"map": "KZN_09", "id": 2},             "to": {"map": "KZN_09", "id": "HiddenPanel"}, "reqs": [["can_flip_panels"]]}, #* Zipline Cavern Exit West Lower -> HiddenPanel (StarPiece)
    {"from": {"map": "KZN_09", "id": "HiddenPanel"}, "to": {"map": "KZN_09", "id": 2},             "reqs": []}, #* HiddenPanel (StarPiece) -> Zipline Cavern Exit West Lower

    # KZN_10 Descent Toward Boss
    {"from": {"map": "KZN_10", "id": 0}, "to": {"map": "KZN_09", "id": 1}, "reqs": []}, # Descent Toward Boss Exit West -> Zipline Cavern Exit East
    {"from": {"map": "KZN_10", "id": 1}, "to": {"map": "KZN_11", "id": 0}, "reqs": []}, # Descent Toward Boss Exit East -> Second Lava Lake Exit West
    
    {"from": {"map": "KZN_10", "id": 0}, "to": {"map": "KZN_10", "id": 1}, "reqs": []}, #? Descent Toward Boss Exit West -> Descent Toward Boss Exit East
    {"from": {"map": "KZN_10", "id": 1}, "to": {"map": "KZN_10", "id": 0}, "reqs": []}, #? Descent Toward Boss Exit East -> Descent Toward Boss Exit West

    # KZN_11 Second Lava Lake
    {"from": {"map": "KZN_11", "id": 0}, "to": {"map": "KZN_10", "id": 1}, "reqs": []}, # Second Lava Lake Exit West -> Descent Toward Boss Exit East
    {"from": {"map": "KZN_11", "id": 1}, "to": {"map": "KZN_17", "id": 0}, "reqs": []}, # Second Lava Lake Exit East -> Spike Roller Trap Exit West
    
    {"from": {"map": "KZN_11", "id": 0}, "to": {"map": "KZN_11", "id": 1}, "reqs": []}, #? Second Lava Lake Exit West -> Second Lava Lake Exit East
    {"from": {"map": "KZN_11", "id": 1}, "to": {"map": "KZN_11", "id": 0}, "reqs": []}, #? Second Lava Lake Exit East -> Second Lava Lake Exit West

    # KZN_17 Spike Roller Trap
    {"from": {"map": "KZN_17", "id": 0}, "to": {"map": "KZN_11", "id": 1}, "reqs": []}, # Spike Roller Trap Exit West -> Second Lava Lake Exit East
    {"from": {"map": "KZN_17", "id": 1}, "to": {"map": "KZN_18", "id": 0}, "reqs": []}, # Spike Roller Trap Exit East -> Boss Antechamber Exit West
    
    {"from": {"map": "KZN_17", "id": 0}, "to": {"map": "KZN_17", "id": 1}, "reqs": [["UltraHammer","RF_KZN07_OpenedHammerChest"]]}, #? Spike Roller Trap Exit West -> Spike Roller Trap Exit East
    {"from": {"map": "KZN_17", "id": 1}, "to": {"map": "KZN_17", "id": 0}, "reqs": []}, #? Spike Roller Trap Exit East -> Spike Roller Trap Exit West

    # KZN_18 Boss Antechamber
    {"from": {"map": "KZN_18", "id": 0}, "to": {"map": "KZN_17", "id": 1}, "reqs": []}, # Boss Antechamber Exit West -> Spike Roller Trap Exit East
    {"from": {"map": "KZN_18", "id": 1}, "to": {"map": "KZN_19", "id": 0}, "reqs": []}, # Boss Antechamber Exit East Upper -> Boss Room Exit West Upper
    {"from": {"map": "KZN_18", "id": 2}, "to": {"map": "KZN_19", "id": 1}, "reqs": []}, # Boss Antechamber Exit East Lower -> Boss Room Exit West Lower
    
    {"from": {"map": "KZN_18", "id": 0}, "to": {"map": "KZN_18", "id": 1}, "reqs": []}, #? Boss Antechamber Exit West -> Boss Antechamber Exit East Upper
    {"from": {"map": "KZN_18", "id": 1}, "to": {"map": "KZN_18", "id": 0}, "reqs": []}, #? Boss Antechamber Exit East Upper -> Boss Antechamber Exit West
    {"from": {"map": "KZN_18", "id": 0}, "to": {"map": "KZN_18", "id": 2}, "reqs": []}, #? Boss Antechamber Exit West -> Boss Antechamber Exit East Lower
    {"from": {"map": "KZN_18", "id": 2}, "to": {"map": "KZN_18", "id": 0}, "reqs": []}, #? Boss Antechamber Exit East Lower -> Boss Antechamber Exit West
    
    {"from": {"map": "KZN_18", "id": 0},             "to": {"map": "KZN_18", "id": "HiddenPanel"}, "reqs": [["can_flip_panels"]]}, #* Boss Antechamber Exit West -> HiddenPanel (StarPiece)
    {"from": {"map": "KZN_18", "id": "HiddenPanel"}, "to": {"map": "KZN_18", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Boss Antechamber Exit West

    # KZN_19 Boss Room
    {"from": {"map": "KZN_19", "id": 0}, "to": {"map": "KZN_18", "id": 1}, "reqs": []}, # Boss Room Exit West Upper -> Boss Antechamber Exit East Upper
    {"from": {"map": "KZN_19", "id": 1}, "to": {"map": "KZN_18", "id": 2}, "reqs": []}, # Boss Room Exit West Lower -> Boss Antechamber Exit East Lower
    {"from": {"map": "KZN_19", "id": 2}, "to": {"map": "KZN_20", "id": 0}, "reqs": []}, # Boss Room Exit East -> Rising Lava 1 Exit West
    
    {"from": {"map": "KZN_19", "id": 1}, "to": {"map": "KZN_19", "id": 2}, "reqs": []}, #? Boss Room Exit West Lower -> Boss Room Exit East
    {"from": {"map": "KZN_19", "id": 2}, "to": {"map": "KZN_19", "id": 1}, "reqs": []}, #? Boss Room Exit East -> Boss Room Exit West Lower
    
    {"from": {"map": "KZN_19", "id": 0},         "to": {"map": "KZN_19", "id": "YBlockA"}, "reqs": []}, #* Boss Room Exit West Upper -> YBlockA (SuperShroom)
    {"from": {"map": "KZN_19", "id": "YBlockA"}, "to": {"map": "KZN_19", "id": 0},         "reqs": []}, #* YBlockA (SuperShroom) -> Boss Room Exit West Upper
    {"from": {"map": "KZN_19", "id": 0},         "to": {"map": "KZN_19", "id": "YBlockB"}, "reqs": []}, #* Boss Room Exit West Upper -> YBlockB (MapleSyrup)
    {"from": {"map": "KZN_19", "id": "YBlockB"}, "to": {"map": "KZN_19", "id": 0},         "reqs": []}, #* YBlockB (MapleSyrup) -> Boss Room Exit West Upper

    # KZN_20 Rising Lava 1
    {"from": {"map": "KZN_20", "id": 0}, "to": {"map": "KZN_19", "id": 2}, "reqs": []}, # Rising Lava 1 Exit West -> Boss Room Exit East
    {"from": {"map": "KZN_20", "id": 1}, "to": {"map": "KZN_22", "id": 0}, "reqs": []}, # Rising Lava 1 Bombable Wall -> Rising Lava 2 Bombable Wall (non-bomb side)
    
    {"from": {"map": "KZN_20", "id": 0}, "to": {"map": "KZN_20", "id": 1}, "reqs": []}, #? Rising Lava 1 Exit West -> Rising Lava 1 Bombable Wall
    {"from": {"map": "KZN_20", "id": 1}, "to": {"map": "KZN_20", "id": 0}, "reqs": []}, #? Rising Lava 1 Bombable Wall -> Rising Lava 1 Exit West

    # KZN_22 Rising Lava 2
    {"from": {"map": "KZN_22", "id": 0}, "to": {"map": "KZN_20", "id": 1}, "reqs": []}, # Rising Lava 2 Bombable Wall (non-bomb side) -> Rising Lava 1 Bombable Wall

    {"from": {"map": "KZN_22", "id": 0}, "to": {"map": "KZN_22", "id": 0}, "reqs": [], "pseudoitems": ["MF_Ch5_FoundEscapeRoute"]}, #+ Escape Volcano
]