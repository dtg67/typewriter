import os.path


def get_letter(file):
    file_name = os.path.basename(file)
    start_index = file_name.find("_") + 1
    end_index = file_name.find(".sr")
    return file_name[start_index:end_index]


def convert_timing(times):
    converted_times = []
    timing_conv_dict = {'ns': 1e-9, 'μs': 1e-6, 'ms': 1e-3}
    for time in times:
        if 'μs' in time:
            converted_times.append(float(time[:-3]) * timing_conv_dict['μs'])
        elif 'ms' in time:
            converted_times.append(float(time[:-3]) * timing_conv_dict['ms'])
        elif 'ns' in time:
            converted_times.append(float(time[:-3]) * timing_conv_dict['ns'])
        else:
            converted_times.append(float(time[:-3]))

    return converted_times


def timing_dict(file, times):
    return {get_letter(file): convert_timing(times)}

