from connect_db import cursor, conn

dress_colors = {
    "MONDAY": ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
    "TUESDAY": ["ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"],
    "WEDNESDAY": ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"],
    "THURSDAY": ["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
    "FRIDAY": ["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"],
}

colors = dress_colors.values()

color_collection = []
sorts = ["WHITE", "GREEN", "BLACK", "BLUE", "RED", "CREAM", "ORANGE", "ARSH", "BROWN", "YELLOW"]

resort_colors = []


print("For data 2d visualization..")
v2d = input("Type v2d: ")

def visiual_2d(v2d):
    for weekly_worn_colors in colors:
        for color in weekly_worn_colors:
            color_collection.append(color)
    for sort in sorts:
        if sort in color_collection:
            print(f"{sort}:", color_collection.count(sort))

visiual_2d(v2d)
print()

# The code to sort for mean color.
print("For mean color..")
mean = input("Type mean: ")
def get_mean(mean):
    sub_mean = []
    for weekly_worn_colors in colors:
        for color in weekly_worn_colors:
            color_collection.append(color)
    for sort in sorts:
        if sort in color_collection:
            sub_mean.append(round(color_collection.count(sort) / len(color_collection), 2))
    # 
    for index, value in enumerate(sorts):
        if max(sub_mean) == sub_mean[index]:
            print("Mean color:", sorts[index])

get_mean(mean)
print()

# The code to sort for the most worn color through the week.
print("For most worn color..")
most_worn = input("Type mw: ")
def most_worn_color(most_worn):
    sub_mean = []
    for weekly_worn_colors in colors:
        for color in weekly_worn_colors:
            color_collection.append(color)
    for sort in sorts:
        if sort in color_collection:
            sub_mean.append(round(color_collection.count(sort) / len(color_collection), 2))

    # 
    for index, value in enumerate(sorts):
        if max(sub_mean) == sub_mean[index]:
            result = "Most worn color: "+ sorts[index]
    print(result)

most_worn_color(most_worn)
print()
# The code to sort for median color.
print("For median color..")
median_color = input("Type mc: ")
def get_median(media):
    sub_mean = []
    for weekly_worn_colors in colors:
        for color in weekly_worn_colors:
            color_collection.append(color)
    for sort in sorts:
        if sort in color_collection:
            sub_mean.append(round(color_collection.count(sort) / len(color_collection), 2))

    mid = len(sub_mean) // 2
    print("Median color:", sorts[mid])

get_median(median_color)










# for weekly_worn_colors in colors:
#     for color in weekly_worn_colors:
#         color_collection.append(color)
# for sort in sorts:
#     frq = color_collection.count(sort)

#     # fetch data
#     fetch = """SELECT * FROM colors"""
#     cursor.execute(fetch)
#     data_retrieve = cursor.fetchone()
#     print(data_retrieve)



    # data insert
#     insert_data = """INSERT INTO colors (title, frq)VALUES(%s, %s)"""
#     data = (sort, frq)
#     cursor.execute(insert_data, data)
            
# conn.commit()
# rowCount = cursor.rowcount
# print(rowCount, "Data inserted successfully..")



        

            
       


