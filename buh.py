from queue import PriorityQueue


def display_header():
    print("Student Performance Evaluator")
    print("")
    print("-"*50)

def get_student_info():
    name = input("Student Name: ")
    s1 = input("Score of first assessment: ")
    s2 = input("Score of second assessment: ")
    s3 = input("Score of third assessment: ")
    return name, s1, s2, s3

def evaluate_performance(s1,s2,s3):
    avg = (s1 + s2 + s3) / 3
    if avg <= 100 and avg > 90:
        perf = ("outstanding")
    elif avg <= 89 and avg > 85:
        perf = ("very satisfactory")
    elif avg <= 84 and avg > 80:
        perf = ("satisfactory")
    elif avg <= 80 and avg > 75:
        perf = ("fairly satisfactory")
    else:
        perf = ("needs improvement")
    return perf, avg

def display_report(name, s1, s2, s3,perf, avg):
    print(name)
    print(f"Score for assessment one: {s1}")
    print(f"Score for assessment two: {s2}")
    print(f"Score for assessment three: {s3}")
    print(f"Average score: {avg}")
    print(f"Performance: {perf}")


display_header()
get_student_info()
evaluate_performance()
display_report()



































