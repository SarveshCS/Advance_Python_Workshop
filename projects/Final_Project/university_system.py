"""
University Management System - A comprehensive OOP-based solution
Date: June 2025
"""

import json
import os
from typing import Dict, List, Optional


class Person:
    """Base class representing a generic person in the university system"""
    
    def __init__(self, person_id: str, full_name: str):
        self._id = person_id
        self._name = full_name
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    def __str__(self) -> str:
        return f"ID: {self._id}, Name: {self._name}"
    
    def __repr__(self) -> str:
        return f"Person('{self._id}', '{self._name}')"
    
    def to_dict(self) -> dict:
        raise NotImplementedError("Subclasses must implement to_dict() method")


class Student(Person):
    """Student class inheriting from Person with enrollment capabilities"""
    
    def __init__(self, student_id: str, full_name: str, academic_major: str):
        super().__init__(student_id, full_name)
        self._major = academic_major
        self._enrolled_course_codes = []
    
    @property
    def major(self) -> str:
        return self._major
    
    @major.setter
    def major(self, new_major: str):
        self._major = new_major
    
    @property
    def enrolled_course_codes(self) -> List[str]:
        return self._enrolled_course_codes.copy()
    
    def enroll_course(self, course_code: str) -> None:
        if course_code not in self._enrolled_course_codes:
            self._enrolled_course_codes.append(course_code)
    
    def drop_course(self, course_code: str) -> None:
        if course_code in self._enrolled_course_codes:
            self._enrolled_course_codes.remove(course_code)
    
    def display_details(self) -> str:
        base_info = super().__str__()
        course_count = len(self._enrolled_course_codes)
        return f"{base_info}, Major: {self._major}, Enrolled Courses: {course_count}"
    
    def to_dict(self) -> dict:
        student_data = {
            'id': self._id,
            'name': self._name,
            'major': self._major,
            'enrolled_course_codes': self._enrolled_course_codes,
            'type': 'student'
        }
        return student_data
    
    def __str__(self) -> str:
        return self.display_details()


class Faculty(Person):
    """Faculty class inheriting from Person with course assignment capabilities"""
    
    def __init__(self, faculty_id: str, full_name: str, academic_department: str):
        super().__init__(faculty_id, full_name)
        self._department = academic_department
        self._assigned_course_codes = []
    
    @property
    def department(self) -> str:
        return self._department
    
    @department.setter
    def department(self, new_department: str):
        self._department = new_department
    
    @property
    def assigned_course_codes(self) -> List[str]:
        return self._assigned_course_codes.copy()
    
    def assign_course(self, course_code: str) -> None:
        if course_code not in self._assigned_course_codes:
            self._assigned_course_codes.append(course_code)
    
    def unassign_course(self, course_code: str) -> None:
        if course_code in self._assigned_course_codes:
            self._assigned_course_codes.remove(course_code)
    
    def display_details(self) -> str:
        base_info = super().__str__()
        course_count = len(self._assigned_course_codes)
        return f"{base_info}, Department: {self._department}, Assigned Courses: {course_count}"
    
    def to_dict(self) -> dict:
        faculty_data = {
            'id': self._id,
            'name': self._name,
            'department': self._department,
            'assigned_course_codes': self._assigned_course_codes,
            'type': 'faculty'
        }
        return faculty_data
    
    def __str__(self) -> str:
        return self.display_details()


class Course:
    """Course class representing university courses with prerequisites and enrollments"""
    
    def __init__(self, course_code: str, course_title: str, credit_hours: int, 
                 prerequisites: Optional[List[str]] = None):
        self._course_code = course_code
        self._title = course_title
        self._credits = credit_hours
        self._prerequisite_codes = prerequisites if prerequisites else []
        self._enrolled_student_ids = []
        self._assigned_faculty_id = None
    
    @property
    def course_code(self) -> str:
        return self._course_code
    
    @property
    def title(self) -> str:
        return self._title
    
    @property
    def credits(self) -> int:
        return self._credits
    
    @property
    def prerequisite_codes(self) -> List[str]:
        return self._prerequisite_codes.copy()
    
    @property
    def enrolled_student_ids(self) -> List[str]:
        return self._enrolled_student_ids.copy()
    
    @property
    def assigned_faculty_id(self) -> Optional[str]:
        return self._assigned_faculty_id
    
    @assigned_faculty_id.setter
    def assigned_faculty_id(self, faculty_id: Optional[str]):
        self._assigned_faculty_id = faculty_id
    
    def add_prerequisite(self, prerequisite_code: str) -> None:
        if prerequisite_code not in self._prerequisite_codes:
            self._prerequisite_codes.append(prerequisite_code)
    
    def add_student_id(self, student_id: str) -> None:
        if student_id not in self._enrolled_student_ids:
            self._enrolled_student_ids.append(student_id)
    
    def remove_student_id(self, student_id: str) -> None:
        if student_id in self._enrolled_student_ids:
            self._enrolled_student_ids.remove(student_id)
    
    def assign_faculty_id(self, faculty_id: str) -> None:
        self._assigned_faculty_id = faculty_id
    
    def unassign_faculty_id(self) -> None:
        self._assigned_faculty_id = None
    
    def display_details(self) -> str:
        prereq_info = f"Prerequisites: {', '.join(self._prerequisite_codes) if self._prerequisite_codes else 'None'}"
        enrollment_info = f"Enrolled Students: {len(self._enrolled_student_ids)}"
        faculty_info = f"Assigned Faculty: {self._assigned_faculty_id if self._assigned_faculty_id else 'None'}"
        
        return (f"Course: {self._course_code} - {self._title} ({self._credits} credits), "
                f"{prereq_info}, {enrollment_info}, {faculty_info}")
    
    def to_dict(self) -> dict:
        return {
            'course_code': self._course_code,
            'title': self._title,
            'credits': self._credits,
            'prerequisite_codes': self._prerequisite_codes,
            'enrolled_student_ids': self._enrolled_student_ids,
            'assigned_faculty_id': self._assigned_faculty_id
        }
    
    def __str__(self) -> str:
        return self.display_details()


class University:
    """Main orchestrator class managing all university entities and operations"""
    
    def __init__(self, student_file='students.json', faculty_file='faculty.json', 
                 course_file='courses.json'):
        self._students: Dict[str, Student] = {}
        self._faculty: Dict[str, Faculty] = {}
        self._courses: Dict[str, Course] = {}
        
        self._student_file = student_file
        self._faculty_file = faculty_file
        self._course_file = course_file
        
        self._load_data()
    
    def _load_data(self) -> None:
        try:
            if os.path.exists(self._student_file):
                with open(self._student_file, 'r', encoding='utf-8') as file:
                    student_records = json.load(file)
                    for record in student_records:
                        student_obj = Student(record['id'], record['name'], record['major'])
                        student_obj._enrolled_course_codes = record.get('enrolled_course_codes', [])
                        self._students[record['id']] = student_obj
            
            if os.path.exists(self._faculty_file):
                with open(self._faculty_file, 'r', encoding='utf-8') as file:
                    faculty_records = json.load(file)
                    for record in faculty_records:
                        faculty_obj = Faculty(record['id'], record['name'], record['department'])
                        faculty_obj._assigned_course_codes = record.get('assigned_course_codes', [])
                        self._faculty[record['id']] = faculty_obj
            
            if os.path.exists(self._course_file):
                with open(self._course_file, 'r', encoding='utf-8') as file:
                    course_records = json.load(file)
                    for record in course_records:
                        course_obj = Course(
                            record['course_code'], 
                            record['title'], 
                            record['credits'],
                            record.get('prerequisite_codes', [])
                        )
                        course_obj._enrolled_student_ids = record.get('enrolled_student_ids', [])
                        course_obj._assigned_faculty_id = record.get('assigned_faculty_id')
                        self._courses[record['course_code']] = course_obj
            
            self._validate_data_relationships()
            
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Warning: Could not load data files properly. Starting fresh. Error: {e}")
    
    def _validate_data_relationships(self) -> None:
        for student in self._students.values():
            valid_courses = [code for code in student._enrolled_course_codes 
                           if code in self._courses]
            student._enrolled_course_codes = valid_courses
        
        for faculty_member in self._faculty.values():
            valid_courses = [code for code in faculty_member._assigned_course_codes 
                           if code in self._courses]
            faculty_member._assigned_course_codes = valid_courses
        
        for course in self._courses.values():
            valid_students = [sid for sid in course._enrolled_student_ids 
                            if sid in self._students]
            course._enrolled_student_ids = valid_students
            
            if (course._assigned_faculty_id and 
                course._assigned_faculty_id not in self._faculty):
                course._assigned_faculty_id = None
    
    def _save_data(self) -> None:
        try:
            student_data = [student.to_dict() for student in self._students.values()]
            with open(self._student_file, 'w', encoding='utf-8') as file:
                json.dump(student_data, file, indent=2, ensure_ascii=False)
            
            faculty_data = [faculty.to_dict() for faculty in self._faculty.values()]
            with open(self._faculty_file, 'w', encoding='utf-8') as file:
                json.dump(faculty_data, file, indent=2, ensure_ascii=False)
            
            course_data = [course.to_dict() for course in self._courses.values()]
            with open(self._course_file, 'w', encoding='utf-8') as file:
                json.dump(course_data, file, indent=2, ensure_ascii=False)
                
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def add_student(self, student: Student) -> bool:
        if student.id in self._students:
            return False
        
        self._students[student.id] = student
        self._save_data()
        return True
    
    def remove_student(self, student_id: str) -> bool:
        if student_id not in self._students:
            return False
        
        student = self._students[student_id]
        if student.enrolled_course_codes:
            return False  # Cannot remove student with active enrollments
        
        for course in self._courses.values():
            course.remove_student_id(student_id)
        
        del self._students[student_id]
        self._save_data()
        return True
    
    def add_faculty(self, faculty: Faculty) -> bool:
        if faculty.id in self._faculty:
            return False
        
        self._faculty[faculty.id] = faculty
        self._save_data()
        return True
    
    def remove_faculty(self, faculty_id: str) -> bool:
        if faculty_id not in self._faculty:
            return False
        
        faculty_member = self._faculty[faculty_id]
        if faculty_member.assigned_course_codes:
            return False  # Cannot remove faculty with active assignments
        
        for course in self._courses.values():
            if course.assigned_faculty_id == faculty_id:
                course.unassign_faculty_id()
        
        del self._faculty[faculty_id]
        self._save_data()
        return True
    
    def add_course(self, course: Course) -> bool:
        if course.course_code in self._courses:
            return False
        
        self._courses[course.course_code] = course
        self._save_data()
        return True
    
    def remove_course(self, course_code: str) -> bool:
        if course_code not in self._courses:
            return False
        
        course = self._courses[course_code]
        if course.enrolled_student_ids:
            return False  # Cannot remove course with enrolled students
        
        if course.assigned_faculty_id is not None:
            return False  # Cannot remove course with assigned faculty
        
        for student in self._students.values():
            student.drop_course(course_code)
        
        for faculty_member in self._faculty.values():
            faculty_member.unassign_course(course_code)
        
        del self._courses[course_code]
        self._save_data()
        return True
    
    def enroll_student_in_course(self, student_id: str, course_code: str) -> bool:
        if student_id not in self._students or course_code not in self._courses:
            return False
        
        student = self._students[student_id]
        course = self._courses[course_code]
        
        if course_code in student.enrolled_course_codes:
            return False
        
        for prereq_code in course.prerequisite_codes:
            if prereq_code not in student.enrolled_course_codes:
                return False
        
        student.enroll_course(course_code)
        course.add_student_id(student_id)
        self._save_data()
        return True
    
    def drop_student_from_course(self, student_id: str, course_code: str) -> bool:
        if student_id not in self._students or course_code not in self._courses:
            return False
        
        student = self._students[student_id]
        course = self._courses[course_code]
        
        if course_code not in student.enrolled_course_codes:
            return False
        
        student.drop_course(course_code)
        course.remove_student_id(student_id)
        self._save_data()
        return True
    
    def assign_faculty_to_course(self, faculty_id: str, course_code: str) -> bool:
        if faculty_id not in self._faculty or course_code not in self._courses:
            return False
        
        faculty_member = self._faculty[faculty_id]
        course = self._courses[course_code]
        
        faculty_member.assign_course(course_code)
        course.assign_faculty_id(faculty_id)
        self._save_data()
        return True
    
    def unassign_faculty_from_course(self, faculty_id: str, course_code: str) -> bool:
        if faculty_id not in self._faculty or course_code not in self._courses:
            return False
        
        faculty_member = self._faculty[faculty_id]
        course = self._courses[course_code]
        
        if course.assigned_faculty_id != faculty_id:
            return False
        
        faculty_member.unassign_course(course_code)
        course.unassign_faculty_id()
        self._save_data()
        return True
    
    def get_course_roster(self, course_code: str) -> List[Student]:
        if course_code not in self._courses:
            return []
        
        course = self._courses[course_code]
        enrolled_students = []
        
        for student_id in course.enrolled_student_ids:
            if student_id in self._students:
                enrolled_students.append(self._students[student_id])
        
        return enrolled_students
    
    def display_all_students(self) -> None:
        if not self._students:
            print("No students registered.")
            return
        
        print("\n=== ALL REGISTERED STUDENTS ===")
        for student in self._students.values():
            print(f"  {student}")
    
    def display_all_faculty(self) -> None:
        if not self._faculty:
            print("No faculty registered.")
            return
        
        print("\n=== ALL REGISTERED FACULTY ===")
        for faculty_member in self._faculty.values():
            print(f"  {faculty_member}")
    
    def display_all_courses(self) -> None:
        if not self._courses:
            print("No courses registered.")
            return
        
        print("\n=== ALL REGISTERED COURSES ===")
        for course in self._courses.values():
            print(f"  {course}")
    
    def run_console_interface(self) -> None:
        print("=" * 60)
        print("UNIVERSITY MANAGEMENT SYSTEM")
        print("Advanced Python Workshop - Final Project")
        print("=" * 60)
        
        while True:
            self._display_main_menu()
            
            try:
                choice = input("\nEnter your choice (1-12): ").strip()
                
                if choice == '1':
                    self._handle_add_student()
                elif choice == '2':
                    self._handle_add_faculty()
                elif choice == '3':
                    self._handle_add_course()
                elif choice == '4':
                    self._handle_enroll_student()
                elif choice == '5':
                    self._handle_drop_student()
                elif choice == '6':
                    self._handle_assign_faculty()
                elif choice == '7':
                    self._handle_unassign_faculty()
                elif choice == '8':
                    self._handle_course_roster()
                elif choice == '9':
                    self.display_all_students()
                elif choice == '10':
                    self.display_all_faculty()
                elif choice == '11':
                    self.display_all_courses()
                elif choice == '12':
                    print("\nThank you for using University Management System!")
                    break
                else:
                    print("Invalid choice. Please select 1-12.")
                    
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
            
            input("\nPress Enter to continue...")
    
    def _display_main_menu(self) -> None:
        print("\n" + "=" * 50)
        print("MAIN MENU")
        print("=" * 50)
        print("1.  Add Student")
        print("2.  Add Faculty")
        print("3.  Add Course")
        print("4.  Enroll Student in Course")
        print("5.  Drop Student from Course")
        print("6.  Assign Faculty to Course")
        print("7.  Unassign Faculty from Course")
        print("8.  View Course Roster")
        print("9.  View All Students")
        print("10. View All Faculty")
        print("11. View All Courses")
        print("12. Exit")
    
    def _handle_add_student(self) -> None:
        print("\n--- ADD NEW STUDENT ---")
        try:
            student_id = input("Enter Student ID: ").strip()
            if not student_id:
                print("Student ID cannot be empty.")
                return
            
            name = input("Enter Student Name: ").strip()
            if not name:
                print("Student name cannot be empty.")
                return
            
            major = input("Enter Student Major: ").strip()
            if not major:
                print("Student major cannot be empty.")
                return
            
            new_student = Student(student_id, name, major)
            
            if self.add_student(new_student):
                print(f"Student {name} added successfully!")
            else:
                print(f"Student with ID {student_id} already exists.")
                
        except Exception as e:
            print(f"Error adding student: {e}")
    
    def _handle_add_faculty(self) -> None:
        print("\n--- ADD NEW FACULTY ---")
        try:
            faculty_id = input("Enter Faculty ID: ").strip()
            if not faculty_id:
                print("Faculty ID cannot be empty.")
                return
            
            name = input("Enter Faculty Name: ").strip()
            if not name:
                print("Faculty name cannot be empty.")
                return
            
            department = input("Enter Department: ").strip()
            if not department:
                print("Department cannot be empty.")
                return
            
            new_faculty = Faculty(faculty_id, name, department)
            
            if self.add_faculty(new_faculty):
                print(f"Faculty {name} added successfully!")
            else:
                print(f"Faculty with ID {faculty_id} already exists.")
                
        except Exception as e:
            print(f"Error adding faculty: {e}")
    
    def _handle_add_course(self) -> None:
        print("\n--- ADD NEW COURSE ---")
        try:
            course_code = input("Enter Course Code: ").strip().upper()
            if not course_code:
                print("Course code cannot be empty.")
                return
            
            title = input("Enter Course Title: ").strip()
            if not title:
                print("Course title cannot be empty.")
                return
            
            credits_str = input("Enter Credits: ").strip()
            try:
                credits = int(credits_str)
                if credits <= 0:
                    print("Credits must be a positive number.")
                    return
            except ValueError:
                print("Credits must be a valid number.")
                return
            
            prereq_input = input("Enter Prerequisites (comma-separated, or press Enter for none): ").strip()
            prerequisites = [code.strip().upper() for code in prereq_input.split(',') if code.strip()] if prereq_input else []
            
            new_course = Course(course_code, title, credits, prerequisites)
            
            if self.add_course(new_course):
                print(f"Course {course_code} added successfully!")
            else:
                print(f"Course with code {course_code} already exists.")
                
        except Exception as e:
            print(f"Error adding course: {e}")
    
    def _handle_enroll_student(self) -> None:
        print("\n--- ENROLL STUDENT IN COURSE ---")
        try:
            student_id = input("Enter Student ID: ").strip()
            course_code = input("Enter Course Code: ").strip().upper()
            
            if self.enroll_student_in_course(student_id, course_code):
                print(f"Student {student_id} enrolled in {course_code} successfully!")
            else:
                print("Enrollment failed. Check student ID, course code, or prerequisites.")
                
        except Exception as e:
            print(f"Error enrolling student: {e}")
    
    def _handle_drop_student(self) -> None:
        print("\n--- DROP STUDENT FROM COURSE ---")
        try:
            student_id = input("Enter Student ID: ").strip()
            course_code = input("Enter Course Code: ").strip().upper()
            
            if self.drop_student_from_course(student_id, course_code):
                print(f"Student {student_id} dropped from {course_code} successfully!")
            else:
                print("Drop failed. Check student ID, course code, or enrollment status.")
                
        except Exception as e:
            print(f"Error dropping student: {e}")
    
    def _handle_assign_faculty(self) -> None:
        print("\n--- ASSIGN FACULTY TO COURSE ---")
        try:
            faculty_id = input("Enter Faculty ID: ").strip()
            course_code = input("Enter Course Code: ").strip().upper()
            
            if self.assign_faculty_to_course(faculty_id, course_code):
                print(f"Faculty {faculty_id} assigned to {course_code} successfully!")
            else:
                print("Assignment failed. Check faculty ID and course code.")
                
        except Exception as e:
            print(f"Error assigning faculty: {e}")
    
    def _handle_unassign_faculty(self) -> None:
        print("\n--- UNASSIGN FACULTY FROM COURSE ---")
        try:
            faculty_id = input("Enter Faculty ID: ").strip()
            course_code = input("Enter Course Code: ").strip().upper()
            
            if self.unassign_faculty_from_course(faculty_id, course_code):
                print(f"Faculty {faculty_id} unassigned from {course_code} successfully!")
            else:
                print("Unassignment failed. Check faculty ID, course code, or assignment status.")
                
        except Exception as e:
            print(f"Error unassigning faculty: {e}")
    
    def _handle_course_roster(self) -> None:
        print("\n--- COURSE ROSTER ---")
        try:
            course_code = input("Enter Course Code: ").strip().upper()
            
            if course_code not in self._courses:
                print(f"Course {course_code} not found.")
                return
            
            roster = self.get_course_roster(course_code)
            course = self._courses[course_code]
            
            print(f"\nRoster for {course_code} - {course.title}:")
            print("-" * 50)
            
            if not roster:
                print("No students enrolled in this course.")
            else:
                for i, student in enumerate(roster, 1):
                    print(f"{i:2}. {student}")
                    
        except Exception as e:
            print(f"Error displaying roster: {e}")


def main():
    try:
        university_system = University()
        university_system.run_console_interface()
    except Exception as e:
        print(f"Critical error starting system: {e}")


if __name__ == "__main__":
    main()