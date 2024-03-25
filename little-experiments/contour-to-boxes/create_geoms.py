import numpy as np
import random
import matplotlib.pyplot as plt
import json

random.seed(42)

def circle(r, res=100):
    # Create a circle
    x_circ, y_circ = np.meshgrid(np.linspace(-r, r, res), np.linspace(-r, r, res))
    circle = np.sqrt(x_circ ** 2 + y_circ ** 2) <= 1
    circle_array = circle.astype(int)#.tolist()
    return circle_array

def rectangle(w, h, res=100):
    # Create a rectangle
    x_rect, y_rect = np.meshgrid(np.linspace(-w, h, res), np.linspace(-w/2, h/2, res))
    rectangle = np.ones_like(x_rect, dtype=bool)
    rect_array = rectangle.astype(int)#.tolist()
    return rect_array

# def triangle(w, h, res=100):
#     # Create a triangle
#     x_tri, y_tri = np.meshgrid(np.linspace(-w, h, res), np.linspace(-w, h, res))
#     # triangle = (y_tri >= 0) & (y_tri <= 1 - np.abs(x_tri))
#     # triangle = (y_tri >= 0)
#     triangle = (y_tri <= 1 - np.abs(x_tri))
#     # tri_array = triangle.astype(int)#.tolist()
#     return triangle
#     return tri_array

def create_objects(w, h):
    canvas = np.zeros((w, h), dtype=int)

    l1 = random.randint(w/4, 3*w/4); s1 = random.randint(0, w/2)
    l2 = random.randint(w/4, 3*w/4); s2 = random.randint(0, w/4)
    l3 = random.randint(w/4, 3*w/4); s3 = random.randint(0, w/4)

    print("l1:", l1)
    print("s1:", s1)
    canvas[l1-s1:l1+s1, l1-s1:l1+s1] = circle(1, res=s1*2)

    print("l2:", l2)
    print("s2:", s2)
    canvas[l2-s2:l2+s2, l2-s2:l2+s2] = rectangle(s2, s2, res=s2*2)
    print("rectangle shape:", rectangle(s2, s2, res=s2*2).shape)

    # print("l3:", l3)
    # print("s3:", s3)
    # canvas[l3-s3:l3+s3, l3-s3:l3+s3] = triangle(s3, s3, res=s3*2)
    # print("triangle shape:", triangle(s3, s3, res=s3*2).shape)

    return canvas

    # with open("objects.json", "w") as f:
    #     json.dump(objects, f)

    # print("Objects saved to objects.json")

# Call the function
# create_objects(w=100, h=100)
# res = triangle(100, 100)
res = create_objects(w=200, h=200)
plt.imshow(res)
plt.show()

objects = {"grid": res.flatten().tolist()}
with open("objects.json", "w") as f:
    f.write(json.dumps(objects))