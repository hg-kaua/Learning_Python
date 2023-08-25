def open_or_senior(data):
    output = []
    for pair in data:
        if pair[0] > 54 and pair[1] > 7:
            output.append("Senior")
        else:
            output.append("Open")
    return output

# def open_or_senior(data):
    # return "Senior" if pair[0] > 54 and pair[1] > 7 else "Open" for pair in data

inputEl = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
print(open_or_senior(inputEl))