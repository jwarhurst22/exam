# Data Module


def get_phone_info_list():
    """ Returns a list of phone data """
    # Format <id>,<manufacturer>,<model>,<memory in GB>,<operating system>,<os version>,<price>

    with open("phones.csv", "r") as phone_data:
        phones = phone_data.readlines()

    return phones


def get_tablet_info_list():
    """ Returns a list of tablet data """
    # Format <id>,<manufacturer>,<model>,<memory in GB>,<operating system>,<os version>,<price>

    with open("tablets.csv", "r") as tablet_data:
        tablets = tablet_data.readlines()

    return tablets


def get_laptop_info_list():
    """ Returns a list of laptop data """
    # Format <id>,<manufacturer>,<model>,<memory in GB>,<operating system>,<os version>,<price>

    with open("laptops.csv", "r") as laptop_data:
        laptops = laptop_data.readlines()

    return laptops
