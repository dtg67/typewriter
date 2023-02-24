import os.path


def get_letter(file):
    file_name = os.path.basename(file)
    start_index = file_name.find("_") + 1
    end_index = file_name.find(".sr")
    return file_name[start_index:end_index]


def convert_timing(*times, **kwargs):
    units = kwargs.get("units", "seconds")
    factors = {'microseconds': 1e-6, 'miliseconds': 1e-3}
    factor = factors.get(units, 1)
    converted_times = [t * factor for t in times]
    return converted_times

