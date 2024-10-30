# import circle

# pi = 3
# print(pi)
# print(circle.pi)
# print(circle.area(3))
# print(circle.circumference(3))
# print(circle.sphereSurface(3))

import square

print(square.area(5))
print(square.perimeter(5))


# ユーザーからの入力を求めるver.
side = float(
    input(
        "一片の長さを入力してください：",
    )
)

print(square.area_user(side))
print(square.perimeter_user(side))
