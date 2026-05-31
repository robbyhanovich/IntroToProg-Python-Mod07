# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Robby Hanovich, 31 May 2026, Updated script to add Person and Student Classes
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Create a Person Class with a constructor with first_name and last_name properties
# TODO Create a Person Class (Done)
class Person:
    """
    A person object consisting of first name and last name strings of characters A - Z.

    ChangeLog: (Who, When, What)
    Robby Hanovich, 31 May 2026, Created Person Class.

    """

    # TODO Add first_name and last_name properties to the constructor (Done)
    def __init__ (self, first_name: str ="", last_name: str = "") -> None:
        """ This initializes the values of the Person class with empty strings

         ChangeLog: (Who, When, What)
         Robby Hanovich, 31 May 2026, Created __init__

         :param
            first_name: string of characters A-Z representing the persons first name
            last_name: string of characters A-Z representing the persons last name
         :return: None
         """
        self.__first_name = first_name
        self.__last_name = last_name

    # TODO Create a getter and setter for the first_name property (Done)
    @property          #getter for first_name of Person class
    def first_name (self) -> str:
        """This is getter method for the first_name of the Person class.

         ChangeLog: (Who, When, What)
         Robby Hanovich, 31 May 2026, Created getter

        :return: first name as a string using title case
        """
        return self.__first_name.title()  # return first name using title case

    @first_name.setter  # setter for first_name of Person class
    def first_name (self, value) -> None:
        """This is setter method for the first_name of the Person class.

         ChangeLog: (Who, When, What)
         Robby Hanovich, 31 May 2026, Created setter

        :param value: string to set to first_name
        """
        if str (value).isalpha():
            self.__first_name = str(value).title() #set the first name using title case
        else:
            raise Exception ("First names cannot be numbers.\n")

    # TODO Create a getter and setter for the last_name property (Done)
    @property          #getter for last_name of Person class
    def last_name (self) -> str:
        """This is getter method for the last_name of the Person class.

         ChangeLog: (Who, When, What)
         Robby Hanovich, 31 May 2026, Created getter

        :return: last name as a string using title case
        """
        return self.__last_name.title()  # return last name using title case

    @last_name.setter  # setter for last_name of Person class
    def last_name (self, value) -> None:
        """This is setter method for the last_name of the Person class.

         ChangeLog: (Who, When, What)
         Robby Hanovich, 31 May 2026, Created setter

        :param value: string to set to last_name
        """
        if str (value).isalpha():
            self.__last_name = str(value).title() #set the last name using title case
        else:
            raise Exception ("Last names cannot be numbers.\n")

    # TODO Override the __str__() method to return Person data (Done)
    def __str__(self) -> str:
        """This method overrides the default __str__ and returns a comma separated
         string of the Person Class.

         ChangeLog: (Who, When, What)
         Robby Hanovich, 31 May 2026, Created method

        :return:
        """
        return f"{self.first_name}, {self.last_name}"

    # TODO Create a Student class the inherits from the Person class (Done)
# Create a Student Class that inherits the Person class and adds the course_name property
class Student (Person):

    # TODO call to the Person constructor and pass it the first_name and last_name data (Done)
    def __init__ (self, first_name: str ="", last_name: str = "", course_name: str = "") -> None:
        """ This initializes the values of the Student class with empty strings

         ChangeLog: (Who, When, What)
         Robby Hanovich, 31 May 2026, Created __init__

         :param
            first_name: string of characters A-Z representing the persons first name
            last_name: string of characters A-Z representing the persons last name
            course_name: string of characters representing the course name
         :return: None
         """
        super().__init__ (first_name = first_name, last_name = last_name) # call to Person Class constructor
        # TODO add a assignment to the course_name property using the course_name parameter (Done)
        self.__course_name = course_name


    # TODO add the getter for course_name (Done)
    @property          #getter for course_name of Student class
    def course_name (self) -> str:
        """This is getter method for the course_name of the Student class.

         ChangeLog: (Who, When, What)
         Robby Hanovich, 31 May 2026, Created getter

        :return: course name as a string using title case
        """
        return self.__course_name.title()  # return last name using title case

    # TODO add the setter for course_name (Done)
    @course_name.setter  # setter for last_name of Person class
    def course_name (self, value) -> None:
        """This is setter method for the course_name of the Student class.

         ChangeLog: (Who, When, What)
         Robby Hanovich, 31 May 2026, Created setter

        :param value: string to set to course_name
        """
        self.__course_name = str(value).title() #set the course name using title case


    # TODO Override the __str__() method to return the Student data (Done)
def __str__(self) -> str:
    """This method overrides the default __str__ and returns a comma separated
     string of the Student Class.

     ChangeLog: (Who, When, What)
     Robby Hanovich, 31 May 2026, Created method

    :return:
    """
    return f"{self.first_name}, {self.last_name}, {self.course_name}"

# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    Robby Hanovich, 31 May 2026, updated functions below to support Person and Student Classes
        - read_data_from_file
        - write_data_to_file
    """
    @staticmethod
    def read_data_from_file(file_name: str) -> list[Student]:
        """ This function reads data from a JSON file and loads it into a list of dictionary rows
        then returns the list filled with student data.

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Robby Hanovich, 31 May 2026, updated functions below to support Person and Student Classes

        :param file_name: string data with name of file to read from

        :return: list
        """
        file = None

        try:
            # Get a list of dictionary rows from the data file
            file = open(file_name, "r")
            json_students = json.load(file)

            # Convert the list of dictionary rows into a list of Student objects
            student_objects:list [Student] = []
            # TODO replace this line of code to convert dictionary data to Student data (Done)
            #student_objects = json_students
            for row in json_students:
                student_objects.append(Student(first_name = row['FirstName'], last_name = row['LastName'], course_name = row['CourseName']))

        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file is not None and file.closed == False:
                file.close()

        return student_objects

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list[Student]) -> None:
        """ This function writes data to a JSON file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Robby Hanovich, 31 May 2026, updated functions below to support Person and Student Classes

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """
        file = None

        try:
            # TODO Add code to convert Student objects into dictionaries (Done)
            student_objects:list[dict[str,str]] = []
            for student in student_data:
                student_objects.append ({"FirstName":student.first_name, "LastName": student.last_name, "CourseName": student.course_name})

            file = open(file_name, "w")
            json.dump ( student_objects,file, indent=2)

            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file is not None and file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    Robby Hanovich, 31 May 2026, updated functions below to support Person and Student Classes
        - output_student_and_course_names
        - input_student_data(student_data

    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str) -> None:
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function


        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice() -> str:
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list[Student]) -> None:
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Robby Hanovich, 31 May 2026, updated functions below to support Person and Student Classes

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:
            # TODO Add code to access Student object data instead of dictionary data (Done)
            print(f'Student {student.first_name} '
                  f'{student.last_name} is enrolled in {student.course_name}')

        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list[Student]) -> list[Student]:
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Robby Hanovich, 31 May 2026, updated functions below to support Person and Student Classes

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")

            # TODO Replace this code to use a Student objects instead of a dictionary objects (done)
            #student = {"FirstName": student_first_name,
             #          "LastName": student_last_name,
             #         "CourseName": course_name}

            student_data.append(Student(
                first_name = student_first_name,
                last_name = student_last_name,
                course_name = course_name))

            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Start of main body

# Define the Data Variables
students: list [Student] = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
