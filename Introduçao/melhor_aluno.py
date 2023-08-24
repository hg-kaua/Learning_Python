def better_than_average(class_points, your_points):
    # Your code here
    sum = 0
    for point in class_points:
        sum += point
    average = sum / len(class_points)
    
    if your_points > average:
        return True
    else:
        return False