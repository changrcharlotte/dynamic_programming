
num_of_rows,num_to_remove = 0,0

def format_numbers(input_array):
    global num_of_rows ,num_to_remove
    num_of_rows= input_array[0][0]
    num_to_remove = input_array[0][1]
    rows, cols = num_of_rows, 2
    grid =[[0]*cols for _ in range(rows)]

    while len(input_array)-1 < num_of_rows:
        input_array.append((0,0))

    for i in range(num_of_rows):
        grid[i][0]= input_array[i+1][0]
        grid[i][1] = input_array[i+1][1]

    return grid

def make_ranked_list(gallery_layout):

    value_dict = {}

    for i in range(0, num_of_rows):
        for j in range(0,2):
            if gallery_layout[i][j] not in value_dict:
                value_dict[gallery_layout[i][j]]=1
            else:
                value_dict[gallery_layout[i][j]] +=1

    sorted_by_key = dict(sorted(value_dict.items()))
    #print(sorted_by_key)

    return sorted_by_key

def check_possible_route(layout_grid):
    possible = False

# rule: never close both rooms on the same row
    for i in range(0, len(layout_grid)):
        if layout_grid[i][0] == -1 and layout_grid[i][1] == -1:
            possible = False
            return possible

    possible = True
    return possible

#possibly implementing recursion?




def find_indexes_by_item(layout_grid, item_to_find):
    list_of_indexes = []

    for i in range(0, num_of_rows):
        for j in range(0, 2):
            if layout_grid[i][j] == item_to_find:
                list_of_indexes.append((i,j))

    return list_of_indexes


#print("input data:")
input_data = []
while True:
    try:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        input_data.append((a, b))
    except EOFError:  # end of input (if from file or redirected stdin)
        break

#print(input_data)#ignores sentinel values
layout_grid= format_numbers(input_data)
ranked_list = make_ranked_list(layout_grid)
num_removed = 0
room_weight_index = 0

for value in ranked_list.keys():
    #if value == 0:
        #print("stop")

    list_of_indexes = find_indexes_by_item(layout_grid, value)  # y, x
    for n in list_of_indexes:
        burner_layout_grid = [row[:] for row in layout_grid]
        y = n[0]
        x = n[1]
        burner_layout_grid[y][x] = -1
        if check_possible_route(burner_layout_grid):
            layout_grid[y][x] = -1
            num_removed += 1
        if num_removed == num_to_remove:
            break
    if num_removed == num_to_remove:
        break
total = 0
for i in range(0, len(layout_grid)):
    for j in range(0, 2):
        if layout_grid[i][j] != -1:
            total += layout_grid[i][j]
#print(layout_grid)
print(total)