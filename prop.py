import numpy as np

def load_tle(filename : str):
    """Returns array of TLEs"""

    num_elements = 0
    first_line = False

    elements_by_id = {}

    with open(filename) as f:
        for i, line in enumerate(f.readlines()):
            toks = line.strip().split()
            if toks[1][-1] == 'U':
                if first_line:
                    raise ValueError("Unexpected first line: {}".format(i))
                num_elements += 1
                first_line = True
                # Skipping the first line data for now...
            else:
                if not first_line:
                    raise ValueError("Missing element first line: {}".format(i))
                first_line = False
                id = toks[1]
                inclination_deg = float(toks[2])
                raan_deg = float(toks[3])
                eccentricity = int(toks[4])
                argument_of_perigee_deg = float(toks[5])
                mean_anomaly_deg = float(toks[6])
                mean_motion = float(toks[7][:11])

                elements_by_id[id] = [inclination_deg, raan_deg, eccentricity, 
                argument_of_perigee_deg, mean_anomaly_deg, mean_motion]
    print("Loaded {} elements.".format(num_elements))
    return elements_by_id