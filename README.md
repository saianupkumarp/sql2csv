# SQL To CSV (SQL2CSV)

SQL2CSV Downloads all table data from SQL Database into a separate csv for each of the table with header information

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
 - [Python 2.7][py27]
 - pymssql (Pip install pymssql)
 - csv
 - Create a folder titled "_Output/SQLOutput" in the root directory to save all the data

### Installation

SQL2CSV requires [Python 2.7](https://www.python.org/download/releases/2.7/) to run.

Install the dependencies and start the exporting.

```sh
$ python sql_all_tables_to_csv.py
```
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

   [py27]: <https://www.python.org/download/releases/2.7/>