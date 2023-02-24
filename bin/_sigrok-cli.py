# Typewriter bin
import re
import subprocess


def sigrok_command(in_file):
    output = subprocess.run(['sigrok-cli', '-i', in_file, '-P', 'timing:avg_period=0'],
                            stderr=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            text=True)
    return output


def sigrok_output_to_list(output):
    timing_matches = re.findall(r':([^()]+)\(', output)
    stripped_timing = [s.strip() for s in timing_matches]
    return stripped_timing




