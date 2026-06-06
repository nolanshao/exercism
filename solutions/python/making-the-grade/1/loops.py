"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    Parameters:
        student_scores (list[float]): Student exam scores.

    Returns:
        list[int]: Student scores *rounded* to the nearest integer value.
    """
    scores = []
        
    for i in range(len(student_scores)):
        scores.append(round(student_scores[i]))
    return scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    Parameters:
        student_scores (list[int]): Student scores as ints.

    Returns:
        int: The count of student scores at or below 40.
    """

    failed = 0
    for i in range(len(student_scores)):
        if student_scores[i] <= 40:
            failed += 1

    return failed


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    Parameters:
        student_scores (list[int]): Integer scores.
        threshold (int): The threshold to cross to be the "best" score.

    Returns:
        list[int]: Integer scores that are at or above the "best" threshold.
    """

    scores = []
    for i in range(len(student_scores)):
        if student_scores[i] >= threshold:
            scores.append(student_scores[i])
    return scores



def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    Parameters:
        highest (int): The value of the highest exam score.

    Returns:
        list[int]: Lower threshold scores for each D-A letter grade interval.

        For example, where the highest score is 100, and failing is <= 40,
        The result would be [41, 56, 71, 86]:
            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    a = highest
    c = (a + 40) // 2
    b = (a + c) // 2
    d = (c + 40) // 2

    return [41, d + 1, c + 1, b + 1]


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    Parameters:
        student_scores (list): Scores in descending order.
        student_names (list[str]): Student names by exam score in descending order.

    Returns:
        list[str]: Strings in format ["<rank>. <student name>: <score>"].
    """

    students = []
    for i in range(len(student_scores)):
        students.append((student_scores[i], student_names[i]))
    
    students.sort(reverse=True)
    return_values = []
    for i, s in enumerate(students):

        return_values.append(f"{i + 1}. {s[1]}: {s[0]}")
    return return_values



def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    Parameters:
        student_info (list[list[str, int]]): List of [<student name>, <score>] lists.

    Returns:
        list: First `[<student name>, 100]` found OR `[]` if no student score of 100 is found.
    """


    for student in student_info:
        if student[1] == 100:
            
            return student
    return []