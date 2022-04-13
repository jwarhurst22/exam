import sys
import data
import report
import datetime
import statistics

PRICE_INDEX = 6
RAM_INDEX = 3
OS_INDEX = 4
OS_VERSION_INDEX = 5


def get_commandline_prams():
    """ This function validates command line parameters and returns a tuple """

    input_type_of_data = {"phone", "tablet", "laptop"}
    report_type_of_data = {"text", "csv", "json", "yaml"}

    if len(sys.argv) != 4:
        print("Invalid number of parameters")
        exit(0)

    input_type = sys.argv[1]
    report_type = sys.argv[2]
    report_filename = sys.argv[3]

    if input_type not in input_type_of_data:
        print("Input type must be either phone, tablet or laptop.")
        exit(0)

    if report_type not in report_type_of_data:
        print("Report type must be either text, csv, json or yaml.")
        exit(0)

    if report_filename == "":
        print("Report filename must not be an empty string.")
        exit(0)

    return input_type, report_type, report_filename


def main():
    """ The main function that produces reports according to the prams given """

    argv_data = get_commandline_prams()
    input_type = argv_data[0]
    report_type = argv_data[1]
    report_filename = argv_data[2]

    date = datetime.datetime.now()
    current_date = date.strftime("%Y-%m-%d %I:%M %p")

    device_lookup = {"phone": "Phone", "tablet": "Tablet", "laptop": "Laptop"}

    data_results = []

    if input_type == 'phone':
        data_results.extend(data.get_phone_info_list())

    elif input_type == 'tablet':
        data_results.extend(data.get_tablet_info_list())

    elif input_type == 'laptop':
        data_results.extend(data.get_laptop_info_list())

    price_list = []
    ram_list = []
    os_list = set()

    for results in data_results:
        fields = results.split(",")
        price_list.append(float(fields[PRICE_INDEX]))
        ram_list.append(int(fields[RAM_INDEX]))
        os_list.add(fields[OS_INDEX] + " " + fields[OS_VERSION_INDEX])

    device_name = device_lookup[input_type]
    num_of_devices = len(data_results)
    avg_price = round(statistics.mean(price_list), 2)
    min_price = min(price_list)
    max_price = max(price_list)
    median_ram = statistics.median(ram_list)
    os_list = list(os_list)
    os_list = sorted(os_list, reverse=True)

    if "text" == report_type:
        report.text_report(current_date, device_name, num_of_devices,
                           avg_price, min_price, max_price,
                           median_ram, os_list, report_filename)
    elif "json" == report_type:
        report.json_report(current_date, device_name, num_of_devices,
                           avg_price, min_price, max_price,
                           median_ram, os_list, report_filename)
    elif "csv" == report_type:
        report.csv_report(current_date, device_name, num_of_devices,
                          avg_price, min_price, max_price,
                          median_ram, os_list, report_filename)
    elif "yaml" == report_type:
        report.yaml_report(current_date, device_name, num_of_devices,
                           avg_price, min_price, max_price,
                           median_ram, os_list, report_filename)


if __name__ == '__main__':
    main()
