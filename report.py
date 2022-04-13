import json
import yaml


def text_report(date, device_type, num_of_devices, avg_price, min_price, max_price, median_ram, os, filename):
    """ Prints and Generates text report files for type of devices. """

    data_to_display = "Timestamp: %s\nDevice: %s\nNumber: %d\nAverage Price: " \
                      "%f\nMinimum Price: %f\nMaximum price: %f\nMedian Ram: " \
                      "%f\nOperating Systems: %s" % \
                      (date, device_type, num_of_devices, avg_price, min_price, max_price, median_ram, ','.join(os))

    print(data_to_display)

    with open("%s.txt" % filename[:12], "w") as write_data:
        write_data.write(data_to_display)


def csv_report(date, device_type, num_of_devices, avg_price, min_price, max_price, median_ram, os, filename):
    """ Prints and Generates csv report files for type of devices. """

    data_to_display = "%s,%s,%d,%f,%f,%f,%f,%s" % \
                      (date, device_type, num_of_devices, avg_price, min_price, max_price, median_ram, '/'.join(os))


    print(data_to_display)

    with open("%s.csv" % filename[:12], "w") as write_data:
        write_data.write(data_to_display)


def json_report(date, device_type, num_of_devices, avg_price, min_price, max_price, median_ram, os, filename):
    """ Prints and Generates json report files for type of devices. """

    data = {
        "date_time": date,
        "device_type": device_type,
        "number": num_of_devices,
        "average_price": avg_price,
        "min_price": min_price,
        "max_price": max_price,
        "median_ram": median_ram,
        "operating_systems": os
    }

    print(json.dumps(data, indent=4))

    with open("%s.json" % filename[:12], "w") as write_data:
        write_data.write(json.dumps(data, indent=4))


def yaml_report(date, device_type, num_of_devices, avg_price, min_price, max_price, median_ram, os, filename):
    """ Prints and Generates yaml report files for type devices. """

    data = {
        "date_time": date,
        "device_type": device_type,
        "number": num_of_devices,
        "average_price": avg_price,
        "min_price": min_price,
        "max_price": max_price,
        "median_ram": median_ram,
        "operating_systems": os
    }

    print(yaml.safe_dump(data))

    with open("%s.yaml" % filename[:12], "w") as write_data:
        write_data.write(yaml.safe_dump(data))
