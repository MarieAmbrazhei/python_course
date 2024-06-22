"""Homework_14_1: Writing and implementing programs."""

# Files

import os


def create_and_write_file(file_path):
    """Create a file and write initial student data if it doesn't exist."""
    # to create file if it not exists
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            students = ['Pavel, group 1, 8',
                        'Ivan, group 1, 9',
                        'Petya, group 2, 10',
                        'Vasya, group 2, 9'
                        ]
            for student in students:
                file.write(student + '\n')


# Откройте файл и прочитайте всю
# информацию из него. Напечатайте общее количество студентов, количество
# студентов для каждой группы и среднюю оценку для каждой группы.
def read_and_process_file(file_path):
    """Read the file, calculate and print student statistics."""
    result_info = ''
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        total_students = len(lines)
        groups_students_count = {}
        groups_grades = {}
        for line in lines:
            splitted_line = line.split(', ')
            if len(splitted_line) == 3:
                _, group, grade = splitted_line
                grade = int(grade)
                if group in groups_students_count:
                    groups_students_count[group] += 1
                    groups_grades[group] += grade
                else:
                    groups_students_count[group] = 1
                    groups_grades[group] = grade
        average_group_grade = {}
        for group in groups_grades:
            average_group_grade[group] = groups_grades[group] / \
                                         groups_students_count[group]
        result_info = (f'\n\ntotal student count is {total_students} \n'
                       f'group student count is {groups_students_count} \n'
                       f'average group grade is {average_group_grade}\n')
        print(result_info)
    else:
        print(f'File {file_path} does not exist')
    return result_info


entire_info = read_and_process_file(file_path='student.txt')


# Допишите эту информацию в конец файла.
def add_result_info(file_path, info):
    """Append the result information to the file."""
    if os.path.exists(file_path):
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(info)
    else:
        print(f'File {file_path} does not exist')


add_result_info(file_path='student.txt', info=entire_info)
