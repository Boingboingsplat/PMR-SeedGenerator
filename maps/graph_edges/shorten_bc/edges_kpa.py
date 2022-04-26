"""This file represents all edges of the world graph that have origin-nodes in the KPA (Bowser's Castle) area."""
edges_kpa_add = [
    # KPA_32 Lower Grand Hall
    {"from": {"map": "KPA_32",  "id": 0}, "to": {"map": "KPA_82",  "id": 1}, "reqs": []}, # Lower Grand Hall Door Bottom Left -> Guard Door 2 Guard Door Right

    # KPA_33 Upper Grand Hall
    {"from": {"map": "KPA_33",  "id": 2}, "to": {"map": "KPA_102", "id": 0}, "reqs": []}, # Upper Grand Hall Door Top Right -> Blue Fire Bridge Door Left

    # KPA_50 Hall to Guard Door 1
    {"from": {"map": "KPA_50",  "id": 1}, "to": {"map": "KPA_82",  "id": 0}, "reqs": []}, # Hall to Guard Door 1 Door Right -> Guard Door 2 Door Left

    # KPA_51 Hall to Water Puzzle
    {"from": {"map": "KPA_51",  "id": 1}, "to": {"map": "KPA_130", "id": 0}, "reqs": []}, # Hall to Water Puzzle Door Right -> Bill Blaster Hall Door Left

    # KPA_61 Battlement
    {"from": {"map": "KPA_61",  "id": 0}, "to": {"map": "KPA_112", "id": 1}, "reqs": []}, # Battlement Door Bottom Left -> Hidden Passage 1 Door Right

    # KPA_62 Front Door Exterior
    {"from": {"map": "KPA_62",  "id": 3}, "to": {"map": "KPA_62",  "id": 0}, "reqs": []}, #? Front Door Exterior Hangar Door Bottom Left -> Front Door Exterior Front Door

    # KPA_82 Guard Door 2
    {"from": {"map": "KPA_82",  "id": 0}, "to": {"map": "KPA_50",  "id": 1}, "reqs": []}, # Guard Door 2 Door Left -> Hall to Guard Door 1 Door Right
    {"from": {"map": "KPA_82",  "id": 1}, "to": {"map": "KPA_32",  "id": 0}, "reqs": []}, # Guard Door 2 Guard Door Right -> Lower Grand Hall Door Bottom Left

    # KPA_102 Blue Fire Bridge
    {"from": {"map": "KPA_102", "id": 0}, "to": {"map": "KPA_33",  "id": 2}, "reqs": []}, # Blue Fire Bridge Door Left -> Upper Grand Hall Door Top Right

    # KPA_112 Hidden Passage 1
    {"from": {"map": "KPA_112", "id": 1}, "to": {"map": "KPA_61",  "id": 0}, "reqs": []}, # Hidden Passage 1 Door Right -> Battlement Door Bottom Left

    # KPA_130 Bill Blaster Hall
    {"from": {"map": "KPA_130", "id": 0}, "to": {"map": "KPA_51",  "id": 1}, "reqs": []}, # Bill Blaster Hall Door Left -> Hall to Water Puzzle Door Right
]

edges_kpa_remove = [
    # KPA_32 Lower Grand Hall
    {"from": {"map": "KPA_32",  "id": 0}, "to": {"map": "KPA_81",  "id": 2}, "reqs": []}, # Lower Grand Hall Door Bottom Left -> Guard Door 1 Guard Door Right

    # KPA_33 Upper Grand Hall
    {"from": {"map": "KPA_33",  "id": 2}, "to": {"map": "KPA_52",  "id": 0}, "reqs": []}, # Upper Grand Hall Door Top Right -> Split Level Hall Door Left

    # KPA_50 Hall to Guard Door 1
    {"from": {"map": "KPA_50",  "id": 1}, "to": {"map": "KPA_81",  "id": 0}, "reqs": []}, # Hall to Guard Door 1 Door Right -> Guard Door 1 Door Left

    # KPA_51 Hall to Water Puzzle
    {"from": {"map": "KPA_51",  "id": 1}, "to": {"map": "KPA_133", "id": 0}, "reqs": []}, # Hall to Water Puzzle Door Right -> Left Water Puzzle Door Bottom Left

    # KPA_61 Battlement
    {"from": {"map": "KPA_61",  "id": 0}, "to": {"map": "KPA_82",  "id": 1}, "reqs": []}, # Battlement Door Bottom Left -> Guard Door 2 Guard Door Right

    # KPA_62 Front Door Exterior
    {"from": {"map": "KPA_62",  "id": 3}, "to": {"map": "KPA_62",  "id": 0}, "reqs": [[{"BowserCastleKey": 1}]]}, #? Front Door Exterior Hangar Door Bottom Left -> Front Door Exterior Front Door

    # KPA_82 Guard Door 2
    {"from": {"map": "KPA_82",  "id": 0}, "to": {"map": "KPA_113", "id": 1}, "reqs": []}, # Guard Door 2 Door Left -> Room with Hidden Door 2 Door Right
    {"from": {"map": "KPA_82",  "id": 1}, "to": {"map": "KPA_61",  "id": 0}, "reqs": []}, # Guard Door 2 Guard Door Right -> Battlement Door Bottom Left

    # KPA_102 Blue Fire Bridge
    {"from": {"map": "KPA_102", "id": 0}, "to": {"map": "KPA_41",  "id": 2}, "reqs": []}, # Blue Fire Bridge Door Left -> Maze Room Door Top Right

    # KPA_112 Hidden Passage 1
    {"from": {"map": "KPA_112", "id": 1}, "to": {"map": "KPA_113", "id": 0}, "reqs": []}, # Hidden Passage 1 Door Right -> Room with Hidden Door 2 Door Left

    # KPA_130 Bill Blaster Hall
    {"from": {"map": "KPA_130", "id": 0}, "to": {"map": "KPA_134", "id": 1}, "reqs": []}, # Bill Blaster Hall Door Left -> Right Water Puzzle Door Bottom Right
]
