def add_score(difficulty):
    my_file = open("scores_file.txt", 'a')
    my_file.close()

    my_file = open("scores_file.txt", 'r')
    line_value = my_file.readline()
    my_file.close()

    if not line_value:
        point_of_winning = int(difficulty * 3) + 5
        my_file = open("scores_file.txt", 'w')
        my_file.write(str(point_of_winning))
        my_file.close()
    else:
        point_of_winning = int(line_value) + int(difficulty * 3) + 5
        my_file = open("scores_file.txt", 'w')
        my_file.write(str(point_of_winning))
        my_file.close()
