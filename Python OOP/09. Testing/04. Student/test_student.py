from unittest import TestCase, main

from project.student import Student


class StudentTest(TestCase):
    def setUp(self) -> None:
        self.student = Student('Stamat',{
            'Web Basics': ['note1', 'note2'],
            'Fundamentals': ['note3', 'note4']
        })
    def test_init_only_with_name(self):
        name = 'Stamat'
        student = Student(name)
        self.assertEqual(name, student.name)
        self.assertEqual({}, student.courses)

    def test_init_with_courses(self):
        name = 'Stamat'
        courses = {
            'Web Basics': ['note1', 'note2'],
            'Fundamentals': ['note3', 'note4']
        }

        student = Student(name, courses)

        self.assertEqual(name, student.name)
        self.assertEqual(courses, student.courses)

    def test_enroll_with_already_enrolled_course_add_notes_to_the_course(self):
        course = 'Fundamentals'
        new_notes = ['new_note']
        expected_notes = self.student.courses[course] + new_notes
        results = self.student.enroll(course, ['new_note'])

        self.assertEqual('Course already added. Notes have been updated.', results)
        self.assertEqual(expected_notes, self.student.courses[course])

    def test_enroll_new_course_with_notes(self):
        course = 'Data Basics'
        notes = ['Data_note 1', 'Data_note 2']

        result = self.student.enroll(course, notes, 'Y')
        self.assertEqual('Course and course notes have been added.', result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual(notes, self.student.courses[course])

    def test_enroll_new_course_with_notes_(self):
        course = 'Data Basics'
        notes = ['Data_note 1', 'Data_note 2']

        result = self.student.enroll(course, notes, '')
        self.assertEqual('Course and course notes have been added.', result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual(notes, self.student.courses[course])

    def test_enroll_new_course_without_notes_(self):
        course = 'Data Basics'
        notes = ['Data_note 1', 'Data_note 2']

        result = self.student.enroll(course, notes, 'T')
        self.assertTrue('Course has been added.', result)
        self.assertEqual([], self.student.courses[course])

    def test_add_notes_add_notes_to_existing_course_(self):
        result =  self.student.add_notes('Fundamentals', 'Fundamentals_note')
        self.assertEqual('Notes have been updated', result)
        self.assertEqual(['note3', 'note4', "Fundamentals_note"], self.student.courses["Fundamentals"])

    def test_add_notes_add_notes_raises_when_no_such_course(self):
        with self.assertRaises(Exception) as context:
            self.student.add_notes('Front-End', 'note')
        self.assertEqual('Cannot add notes. Course not found.', str(context.exception))

    def test_leave_course_removes_course_from_courses(self):
        course = 'Fundamentals'
        results = self.student.leave_course(course)
        self.assertEqual('Course has been removed', str(results))
        self.assertTrue(course not in self.student.courses)
        self.assertTrue(len(self.student.courses) > 0)

    def test_leave_course_that_is_not_in_courses(self):
        course = 'Math'
        with self.assertRaises(Exception) as context:
            self.student.leave_course(course)
        self.assertEqual('Cannot remove course. Course not found.', str(context.exception))


if __name__ == '__main__':
    main()