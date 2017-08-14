"""
    Python version of the Grades program
"""

import pandas
import pickle
from difflib import get_close_matches


class Course:
    def __init__(self, name, weighted=False):
            self.categories = []
            self.name = name
            self.weighted = weighted

    def addCategory(self, key, weight=None):
        self.categories.append({key: [{"Weight": weight}]})

    def addGrade(self, category, title, score, maxScore):
        percent = "{0:.2%}".format((score/maxScore))
        for i, j in enumerate(self.categories):
            if str(list(j.keys())[0]).lower() == category.lower():
                key = (i, list(j.keys())[0])

        self.categories[key[0]][key[1]] += \
            [{title: [score, maxScore, percent]}]

    def findCategory(self, userInput):
        userInput = userInput.lower()

        for i in self.categories:
            keyList.append(list(i.keys())[0])
        else:
            for i in keyList:
                keys.append(i)

        print("yo", keys)

        if userInput in self.categories:
            return self.categories[category]
        elif len(get_close_matches(userInput, keys, 5)) > 0:
            print("Unknown category {0}".format(userInput))
            print("Did you mean to type one of these categories?")

            for i, j in enumerate(
                    get_close_matches(userInput, self.categories.keys(), 5)):
                print("{0}: {1}".format(i+1, j))

            return None
        else:
            print("The word '{0}' does not exist. Try again".format(userInput))
            return None

    def __str__(self):
        return "{}{}\n{:>12}{}\n{:>12}{}\n{:>12}{}" \
               .format(self.name, ".__str__(): ",  # remove this format later
                       "Name: ", self.name,
                       "Weighted? ", self.weighted,
                       "Categories: ", self.categories)


def findCourse(courses, courseName):
    for i in courses:
        if i.name.lower() == courseName.lower():
            return i
    else:
        return None


def main():
    courses = []
    courses.append(Course("CS38", True))
    crs = courses[0]

    crs.addCategory("Tests", 50)
    crs.addGrade("Tests", "test1", 100, 100)
    crs.addCategory("Quizzes", 20)
    crs.addGrade("Quizzes", "popquiz1", 20, 22)
    crs.addCategory("Homework", 10)
    crs.addGrade("Homework", "assignment1", 10, 10)

    print(findCourse(courses, "CS38"))

if __name__ == '__main__':
    main()
