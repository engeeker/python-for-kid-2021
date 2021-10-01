packs_num = 50  # 50包砖，50 packs of bricks
bricks_per_pack = 200 # 每包有867块，each pack has 200 bricks
bricks_need_per_floor = 867  # 每层楼需要867块

floor = 4643//bricks_need_per_floor +1
print("The 4643th brick used to build floor",floor)

floors = (bricks_per_pack * packs_num) // bricks_need_per_floor 
print("These bricks can build",floors)

left = packs_num *bricks_per_pack % bricks_need_per_floor 
print(left,"bricks will be left at the end.")
