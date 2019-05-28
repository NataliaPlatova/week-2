grade_list = [
    {'school_class': '1a', 'scores': [3,4,4,5,2]},
    {'school_class': '1b', 'scores': [4,5,4,5,5,4,4,5,5]},
    {'school_class': '2a', 'scores': [3,2,3,5,2]},
    {'school_class': '3a', 'scores': [5,5,4,5,5,2]},
    {'school_class': '4a', 'scores': [4,4,4,5,3]},
    {'school_class': '4b', 'scores': [3,3,3,3,3]},

]
school_sum = 0
for grade in grade_list:
    class_sum = 0
    for score in grade['scores']:
        class_sum += score
        print(class_sum)
    class_av_score = class_sum / len(grade['scores'])
    print(f'{grade["school_class"]}: {class_av_score}')
    school_sum += class_av_score
school_av_score = school_sum / len(grade_list)
print(f'School score: {school_av_score}')

