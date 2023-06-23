T = int(input())


for tc in range(T):
    subjects_num = int(input())
    verbs_num = int(input())
    objects_num = int(input())
    
    subjects = [input() for _ in range(subjects_num)]
    verbs = [input() for _ in range(verbs_num)]
    objects = [input() for _ in range(objects_num)] 
    
    
    for subject in subjects:
        for verb in verbs:
            for object in objects:
                print(subject +" "+ verb +" "+ object+ ".")
    print()