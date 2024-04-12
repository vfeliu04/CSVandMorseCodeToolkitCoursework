"""
Please write your name
@author: Vicente Feliu

"""

# Reminder: You are only allowed to import the csv module (done it for you).
# OTHER MODULES ARE NOT ALLOWED (NO OTHER IMPORT!!!).

import csv


class Leopard:
    def __init__(self, filepath: str) -> None:
        # Set the variable self.filepath to filepath
        self.filepath = filepath
        # Set the variable self.header to an empty list
        self.header = []
        # Set the variable self.data to and empty list
        self.data = []

        # try to see if the file exits
        # if file does not  exist set the header and data to None

        # Opening csv file
        file = open(filepath)
        type(file)
        csvreader = csv.reader(file)

        # Adding the data of the csv file to the header and to the data array
        self.header = next(csvreader)
        for row in csvreader:
            self.data.append(row)

    def get_header(self) -> list:
        # Return the header
        return self.header

    def get_data(self) -> list:
        # Return the data
        return self.data

    def stats(self) -> dict:
        # Create a dictionary named numerical value dictionary
        numerical_value_dictionary = {}

        # Create a list called temp_data
        temp_data = []

        # Create an int called total
        total = 0

        # Create an int called maximum
        maximum = 0

        # Create an int called minimum
        minimum = 0

        # Create an int called count and set it to zero
        count = 0

        # Create an int called mean and set it to zero
        mean = 0

        # Create an int called break_counter and set it equal to zero
        break_counter = 0

        # Loop through the row in the self.data
        for row in range(len(self.data)):

            # If the break_counter is equal to 1 then break
            if break_counter == 1:
                break
            else:
                # Add one to the break_counter
                break_counter += 1

            # Loop through the columns of the row inside self.data
            for column in range(len(self.data[row])):

                # If the data point you are looking at is a digit
                if self.data[row][column].isdigit():
                    # Set the row equal to zero
                    row = 0
                    # Set the list called temp_data to nothing
                    temp_data = []
                    # Loop while the row is less than the length of the
                    # self.data list
                    while row < len(self.data):
                        # Add the data point to the temp_data list
                        temp_data.append(self.data[row][column])
                        # Add one to the row
                        row += 1
                    # Loop through the temp_data
                    for item in temp_data:
                        # If the item you are looking at is invalid
                        if (item == 'NA') or (item == '-') or (item == ' '):
                            # Remove the item from the temp_data list
                            temp_data.remove(item)
                        else:
                            # Add one to the count of valid data
                            count += 1
                            # Add the value to the total
                            total += int(item)
                    # Set the mean equal to the total divided by the count
                    # rounded up to 2 decimal figures
                    mean = round((total / count), 2)
                    # Set the maximum to the maximum of the temp_data list
                    maximum = max(temp_data, key=int)
                    # Set the minimum to the minimum of the temp_data list
                    minimum = min(temp_data, key=int)

                    # Set the numerical value dictionary key according to
                    # the current header and within that set the
                    # stats gathered above within that header dictionary
                    numerical_value_dictionary[self.header[column]] = \
                        {'count': count, 'mean': mean, 'min': minimum,
                         'max': maximum}
                    # set the row equal to zero
                    row = 0
        # Return the numeral_value_dictionary
        return numerical_value_dictionary

    def html_stats(self, stats: dict, filepath: str) -> None:
        # create a new file called index.html
        name_of_file = filepath[0:len(filepath)-5].capitalize()
        # Open file with write mode
        with open(filepath, "w") as html:
            # Below I wrote the basic html headers and font and color decisions
            html.write(
                """
                <html>
                <head>
                <style>
                table {
                  font-family: arial, sans-serif;
                  border-collapse: collapse;
                  width: 100%;
                }
                td, th {
                  border: 2px solid black;
                  text-align: center;
                  padding: 8px;
                }
                tr:nth-child(even) {
                  background-color: #dddddd;
                }
                </style>
                </head>
                <body>
                <h2>""" + name_of_file + """</h2>
                <table>
                """
            )
            html.write("<tr>\n")
            html.write("<th>Type of Data</th>")
            # Loop through the key in the dictionary
            for key in stats:
                # Write the key as the column
                html.write("<th>" + key + "</th>\n")
            # Write count as the row
            html.write("""
                </tr>
                <tr>
                <th>Count</th>
            """)
            # Loop through the keys in the dictionary and write in html
            # all the values inside key count
            for key in stats:
                html.write("<td>" + str(stats[key]['count']) + "</td>\n")
            # Write count as the Mean
            html.write("""
                            </tr>
                            <tr>
                            <th>Mean</th>
                        """)
            # Loop through the keys in the dictionary and write in html
            # all the values inside key mean
            for key in stats:
                html.write("<td>" + str(stats[key]['mean']) + "</td>\n")
            # Write count as the Maximum
            html.write("""
                                        </tr>
                                        <tr>
                                        <th>Maximum</th>
                                    """)
            # Loop through the keys in the dictionary and write in html
            # all the values inside key max
            for key in stats:
                html.write("<td>" + str(stats[key]['max']) + "</td>\n")
            # Write count as the Minimum
            html.write("""
                                        </tr>
                                        <tr>
                                        <th>Minimum</th>
                                    """)
            # Loop through the keys in the dictionary and write
            # in html all the values inside key min
            for key in stats:
                html.write("<td>" + str(stats[key]['min']) + "</td>\n")

    def count_instances(self, criteria) -> int:
        """
        The data type of the criteria is dictionary and one argument
        can be inputted to this method. In the dictionary
        set the value of the key to the header of the data you are
        looking for and the value of the key
        the corresponding data
        """
        instance = 0
        reached = 0

        for i in range(len(self.header)):
            for key in criteria:
                if key == self.header[i]:
                    index = i
                    for row in range(len(self.data)):
                        for column in range(len(self.data[row])):
                            if (criteria.get(key) == self.data[row][column]) \
                                    and (column == index):
                                instance += 1
                                reached += 1
        # If the variable reached equals zero that means the code did not
        # run properly
        if reached == 0:
            print("""There is a mistake in the parameters given or no data
                  exists with the parameters given""")
        else:
            # Return instance
            return instance


if __name__ == "__main__":
    # DO NOT COMMENT ALL WHEN SUBMIT YOUR FILE, cannot have an if statement
    # with nothing afterwards.

    # test diabetes_data.csv
    test = Leopard("diabetes_data.csv")
    print(test.get_header())
    print(test.get_data())
    stats = test.stats()
    print(stats)
    test.html_stats(stats, "diabetes.html")
    criteria = {'Age': '40', 'Gender': 'Male'}
    print(test.count_instances(criteria))
    print()

    # test fide2021.csv
    test2 = Leopard("fide2021.csv")
    print(test2.get_header())
    print(test2.get_data())
    stats2 = test2.stats()
    print(stats2)
    test2.html_stats(stats2, "fide2021.html")
    criteria = {'Rank': '1'}
    print(test2.count_instances(criteria))
    print()

    # test student.csv
    test3 = Leopard("student.csv")
    print(test3.get_header())
    print(test3.get_data())
    stats3 = test3.stats()
    print(stats3)
    test3.html_stats(stats3, "student.html")
    criteria = {'G3': '15'}
    print(test3.count_instances(criteria))
