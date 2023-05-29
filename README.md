# Phone Book Console Application

This repository contains a console application written in Python that represents a phone book. The program reads records from a file with a predefined structure, sorts them based on chosen criteria and ordering, and displays the sorted records in the console. It also provides validation messages for each line with nonvalid items.

## Getting Started

To use this phone book console application, follow the steps below:

1. Clone the repository to your local machine: 
   git clone https://github.com/Vardges-ops/PhoneBook.git

2. Open the project in your preferred Python development environment.

3. Build the solution to ensure all dependencies are resolved.

4. Locate the file containing the phone book records. It should have the following structure:
{name} {surname} {separator} {phoneNumber}
Example:
Edgar Danielyan - 0989598949
Hovhannes Shitikyan - 0988598949
Artak Hovhannisyan : 0925484988
Nara Hovhannisyan : 092548487
5. Run the console application. It will prompt you to choose the ordering and criteria for sorting the phone book records. 

6. After selecting the sorting options, the application will display the sorted records in the console. 

7. Any validation messages for nonvalid items in the file will also be shown.

## Sorting Criteria and Ordering
The program provides the following sorting criteria options:

Name
Surname
PhoneNumberCode
For each criterion, you can choose either ascending or descending ordering.

## Validations
The program validates each line in the file to ensure the following conditions are met:

Phone number should be 9 digits.
The surname can be empty.
The separator should be : or -.
If a line contains nonvalid items, a validation message will be displayed along with the line number.

## Contributing
Contributions to this phone book console application are welcome. If you find any issues or would like to suggest improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.