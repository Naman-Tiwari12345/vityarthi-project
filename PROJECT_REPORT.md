# Student Expense & Budget Management System
## Python Project Report

### 1. Introduction
The Student Expense & Budget Management System is a Python console application developed to help students maintain records of their daily expenses and monitor their monthly budget.

### 2. Problem Statement
Students may find it difficult to track small daily expenses. Without organized records, total spending and major spending categories can be difficult to identify.

### 3. Objectives
- Record daily expenses.
- Allow users to manage their own expense records.
- Set a monthly budget.
- Calculate total spending.
- Identify the highest spending category.
- Demonstrate Python programming concepts.

### 4. Functional Requirements
- User registration and login.
- Add, view and delete expenses.
- Set and check monthly budget.
- Generate spending reports.
- Store information persistently.

### 5. Non-Functional Requirements
- Usability: menu-driven and simple interface.
- Reliability: data is stored in JSON format.
- Maintainability: functionality is divided into modules.
- Error Handling: invalid numeric input is handled.
- Performance: suitable for normal student-scale data.

### 6. System Architecture
User -> Main Menu -> Functional Modules -> JSON Storage

Functional modules:
- User Management
- Expense Management
- Budget Management
- Reporting

### 7. Design Diagrams

#### Use Case
Student -> Register/Login
Student -> Add Expense
Student -> View/Delete Expense
Student -> Set Budget
Student -> Check Budget
Student -> Generate Report

#### Workflow
Start -> Login/Register -> Main Menu -> Select Operation -> Process Data -> Save/Display Result -> Return to Menu -> Exit

#### Component Diagram
Main Module
  |
  +-- User Module
  +-- Expense Module
  +-- Budget Module
  +-- Report Module
  +-- Validation Module
  +-- Storage Module

### 8. Design Decisions
JSON was selected because the project is designed as a beginner-friendly Python application and does not require a separate database server. Separate Python modules were used to keep the program organized and maintainable.

### 9. Implementation Details
The project uses functions, dictionaries, lists, loops, conditions, file handling, JSON serialization, exception handling and modular programming.

### 10. Screenshots / Results
Add screenshots of:
1. Registration
2. Login
3. Add Expense
4. View Expenses
5. Budget Check
6. Expense Report

### 11. Testing Approach
The `unittest` module is used to test validation functions and currency formatting.

### 12. Challenges Faced
- Designing a simple data structure for multiple users.
- Handling invalid numeric input.
- Maintaining persistent data.
- Dividing the application into separate modules.

### 13. Learnings
- Modular Python programming
- File handling and JSON
- Functions and validation
- Exception handling
- Basic data analysis
- Unit testing
- Project organization

### 14. Future Enhancements
- Graphical user interface
- Expense charts
- CSV/PDF export
- Database integration
- Cloud synchronization

### 15. References
- Python documentation
- Python `json` module documentation
- Python `unittest` module documentation
