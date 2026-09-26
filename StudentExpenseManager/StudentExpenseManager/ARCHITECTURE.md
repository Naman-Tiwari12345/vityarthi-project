# System Architecture

```text
                    +----------------+
                    |     Student    |
                    +-------+--------+
                            |
                            v
                    +----------------+
                    |    main.py     |
                    +-------+--------+
                            |
        +-------------------+-------------------+
        |                   |                   |
        v                   v                   v
 +-------------+     +-------------+     +-------------+
 | user.py     |     | expenses.py |     | budget.py   |
 +-------------+     +-------------+     +-------------+
        |                   |                   |
        +-------------------+-------------------+
                            |
                            v
                    +----------------+
                    |  reports.py    |
                    +-------+--------+
                            |
                            v
                    +----------------+
                    |  storage.py    |
                    +-------+--------+
                            |
                            v
                    +----------------+
                    | expenses.json  |
                    +----------------+
```

## Workflow

```text
START
  |
Register/Login
  |
Main Menu
  |
  +--> Add Expense ------+
  |                      |
  +--> View Expenses ----+
  |                      |
  +--> Delete Expense ---+
  |                      |
  +--> Set Budget -------+
  |                      |
  +--> Check Budget -----+
  |                      |
  +--> Generate Report --+
  |                      |
  +--> Logout
         |
        END
```
