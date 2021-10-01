def average_score(scores):
    """
    calculate the average, please use for loop here, and don't use sum() and len()
    return sum(scores) / len(scores)
    """
    sum_score = 0
    counter = 0

    for score in scores:
        sum_score = sum_score + score
        counter = counter + 1

    return round(sum_score / counter, 2)



scores = [63,79,98,93,100,89,84,70,65]

print("Average score =", average_score(scores))