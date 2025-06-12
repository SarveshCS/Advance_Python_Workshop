# Question 5 of Workshop pdf

class Student:
    def __init__(self, name, marks):
        self.name = name
        if len(marks) != 3:
            raise ValueError("Marks list must contain exactly 3 subjects")
        self.marks = marks
    
    def compute(self):
        total_marks = sum(self.marks)
        average_marks = total_marks / len(self.marks)
        return total_marks, average_marks
    
    def display(self):
        total, average = self.compute()
        print(f"Student Information:")
        print(f"Name: {self.name}")
        print(f"Marks in three subjects: {self.marks}")
        print(f"Total Marks: {total}")
        print(f"Average Marks: {average:.2f}")
        print("-" * 40)


if __name__ == "__main__":
    student1 = Student("Ram", [85, 92, 78])
    student2 = Student("Raju", [90, 88, 95])
    student3 = Student("Anurag", [76, 82, 89])
    
    student1.display()
    student2.display()
    student3.display()
    
    print("Individual computation example:")
    total, avg = student1.compute()
    print(f"{student1.name}'s total: {total}, average: {avg:.2f}")

