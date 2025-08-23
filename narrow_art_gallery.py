from rich.traceback import install
install(show_locals=True)
n,k = 0,0

def format_numbers(input_array):
    global n ,k
    n= input_array[0][0]
    k = input_array[0][1]
    rows, cols = n, 2
    grid =[[0]*cols for _ in range(rows)]

    for i in range(n):
        grid[i][0]= input_array[i+1][0]
        grid[i][1] = input_array[i+1][1]

    return grid

def make_ranked_list(gallery_layout):

    value_dict = {}

    for i in range(0, n):
        for j in range(0,2):
            if gallery_layout[i][j] not in value_dict:
                value_dict[gallery_layout[i][j]]=1
            else:
                value_dict[gallery_layout[i][j]] +=1

    sorted_by_key = dict(sorted(value_dict.items()))
    print(sorted_by_key)

    return

def check_possible_route(layout_grid):

    return


#main program

# sample_input = input("input here:")
# print(sample_input)

# arr = []
# print("Enter numbers (empty line to stop):")
# while True:
#     line = input()
#     if line == "":
#         break
#     arr.append(string(line))
#
# print(arr)

# rows = int(input("Rows: "))
# matrix = []
# for _ in range(rows):
#     matrix.append(list(map(int, input().split())))
#
# print(matrix)

print("input data:")
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
while(num_removed < k):
    ranked_list[0]
