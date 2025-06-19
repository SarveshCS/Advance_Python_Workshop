# University Management System

This is a complete, console-based University Management System built using Python's Object-Oriented Programming (OOP) principles. It allows administrators to manage students, faculty, and courses, while maintaining all data in persistent JSON files.

---

## Features

- Register and manage students and faculty  
- Add and manage courses with prerequisites  
- Enroll or drop students from courses  
- Assign or unassign faculty to courses  
- View course rosters  
- Display all students, faculty, and courses  
- Data is saved persistently between runs  

---

## Object-Oriented Design

This project demonstrates solid OOP principles:

### 1. Classes

- **`Person`**: Base class for `Student` and `Faculty`  
- **`Student`**: Inherits from `Person`, manages enrollment  
- **`Faculty`**: Inherits from `Person`, manages teaching assignments  
- **`Course`**: Holds course details, enrolled students, prerequisites  
- **`University`**: Orchestrator managing all above classes and the system interface  

### 2. Encapsulation

All internal attributes use private-like naming (e.g., `_name`, `_major`) and are accessed via `@property` decorators.

### 3. Inheritance

`Student` and `Faculty` inherit shared functionality from `Person`.

### 4. Composition

The `University` class contains and manages all instances of `Student`, `Faculty`, and `Course`.

---

## Data Persistence

All changes are automatically saved to:

- `students.json`
- `faculty.json`
- `courses.json`

These are loaded when the program starts and relationships are re-linked through `_validate_data_relationships()`.

---

## Console Interface

Run the script to access an intuitive menu with 12 options:

~~~bash
python university_system.py
~~~

Example menu options:

- Add Student
- Enroll Student in Course
- Assign Faculty to Course
- View Course Roster
- Exit

---

## Key Concepts Used

- `@property` for safe attribute access  
- `to_dict()` for converting objects to JSON format  
- `__str__()` and `display_details()` for readable outputs  
- Proper validation before adding/removing entities  
- Enforcement of course prerequisites  
- Safe object linking and cleanup  

---

## Viva Preparedness

A set of curated questions with answers is available to help you prepare for oral evaluations.

📄 [Download Viva PDF](sandbox:/mnt/data/Viva_Questions_University_Management_System.pdf)

---

## License

This project is free for academic and educational purposes.
