# Date Utility Library (Python)
#### Video Demo:  <https://youtu.be/MD5RHTe8-bY>

### Description:

This project is a Python-based **date utility library** that provides several functions for validating, formatting, manipulating, and analyzing dates. The project accepts dates in the format **YYYY-MM-DD** and allows users to extract different components of a date, perform calculations, and convert dates into different readable formats.

The goal of the project is to implement functionality similar to date functions commonly found in **SQL databases and spreadsheet software**, but entirely in Python. The program allows users to work with dates without needing complex datetime logic.

This project demonstrates the use of **Python functions, regular expressions, dictionaries, error handling, and built-in modules** to build a reusable date-processing tool.

The program includes features such as:

* Extracting parts of a date (year, month, day, week)
* Determining the day of the week
* Formatting dates into readable formats
* Calculating date differences
* Adding intervals such as days, weeks, months, and years
* Determining the start or end of a month
* Validating date inputs

All dates are validated before processing to ensure they follow a correct format and represent valid calendar dates.

---

# Features

The library includes several useful functions:

### Date Validation

`is_date()`

Checks whether a given string is a valid date within a specified range.

Example:

```
is_date("2024-10-05")
```

Returns:

```
True
```

---

### Extract Date Parts

The following functions extract parts of a date:

* `day()`
* `month()`
* `year()`
* `week()`
* `week_day()`
* `quarter()`
* `day_of_week()`
* `day_of_year()`

Example:

```
month("2024-05-17")
```

Output:

```
5
```

---

### Date Part Function

`date_part()`

Returns a specified component of a date.

Example:

```
date_part("2024-05-17", "week")
```

Output:

```
20
```

---

### Date Name Function

`date_name()`

Returns the textual representation of a date component.

Example:

```
date_name("2024-05-17", "day_of_week")
```

Output:

```
Friday
```

---

### Date Formatting

`date_format()`

Formats a date into different string formats.

Example:

```
date_format("2024-05-17", "dd-mmm-yyyy")
```

Output:

```
17 May, 2024
```

Supported formats include:

* `dd`
* `ddd`
* `dddd`
* `mm`
* `mmm`
* `mmmm`
* `yy`
* `yyyy`
* `dd-mmm`
* `dd-mmmm`
* `dd-mm-yyyy`
* `dd-mmm-yyyy`

---

### Date Truncation

`date_trunc()`

Truncates a date to the start of a specified period.

Example:

```
date_trunc("2024-05-17", "month")
```

Output:

```
2024-05-01
```

---

### Start and End of Month

Functions included:

```
start_of_month()
end_of_month()
```

Example:

```
end_of_month("2024-02-10")
```

Output:

```
2024-02-29
```

---

### Date Addition

`date_add()`

Adds intervals to a given date.

Example:

```
date_add("2024-05-17", 10, "days")
```

Output:

```
2024-05-27
```

Supported units:

* days
* weeks
* months
* years

---

### Date Difference

`date_diff()`

Calculates the difference between two dates.

Example:

```
date_diff("2024-01-01", "2024-01-10", "days")
```

Output:

```
9
```

Supported units:

* days
* weeks
* months
* years

---

# Program Execution

The program includes a simple command-line interface in `main()` that allows the user to input two dates and calculate the difference between them.

Example:

```
Date1: 2024-01-01
Date2: 2024-01-10
```

Output:

```
9
```

---

# Project Structure

```
project.py
test_project.py
requirement.txt
README.md
```

* `project.py` – Contains all date utility functions
* `tets_project.py` – Contains all the tests for my functions using Pytest
* `requirement.txt` – List of python modules used in the project
* `README.md` – Project documentation

---

# Technologies Used

This project uses the following Python modules:

* `datetime`
* `calendar`
* `re` (regular expressions)
* `dateutil.relativedelta`

---

# Design Choices

One important design decision was implementing a **custom date validation function (`is_date`)** instead of relying solely on Python's built-in date parsing. This allowed stricter control over acceptable formats and provided clear validation rules.

Another design choice was using **dictionary mappings** for functions such as `date_part`, `date_format`, and `date_add`. This approach simplifies extending the library with additional date operations in the future.

Regular expressions were used to validate and extract components from the input date strings, ensuring consistent formatting and avoiding parsing errors.

---

# Possible Future Improvements

Potential improvements for the project include:

* Supporting additional date formats (e.g., `MM/DD/YYYY`)
* Adding timezone support
* Implementing business-day calculations
* Adding more formatting options
* Building a command-line interface with more interactive features

