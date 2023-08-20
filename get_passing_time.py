import json
import time
import os
from n2yo import n2yo

api_key = ""
lat = 0.0
long = 0.0
alt = 0

METEOR_M2_3_ID = 57166

def find_key_in_list(key, dictionary_list):
    for dictionary in dictionary_list:
        if key in dictionary:
            return dictionary[key]
    return None  # Key not found in any dictionary

def utc_to_local(utc):
    local_time = time.localtime(utc)
    return time.strftime('%H:%M', local_time)

def call_satdump(t_start, t_rec): 
    cmd =  ('satdump record MeteorM2-3 --source hackrf --samplerate 2000000'
                '--frequency 137100000 --baseband_format f32 --timeout' + str(t_rec) + ' | at ' + str(t_start))
    os.system(cmd)


def main():
    session = n2yo.N2YO(api_key, lat, long, alt)
    passes = session.get_radio_passes(METEOR_M2_3_ID, 3, lat, long, alt)

    print(passes)
    print("\n\n")


    for i in range(0, len(passes)):
        str_passes = json.dumps(passes[i])
        json_passes = json.loads(str_passes)

        start_utc = find_key_in_list("startUTC", json_passes)
        end_utc   = find_key_in_list("endUTC", json_passes)

        if start_utc and end_utc is not None:
            print(f"Value for startUTC: {start_utc} {utc_to_local(start_utc)}")
            print(f"Value for endUTC: {end_utc} {utc_to_local(end_utc)}")
            # Not using this function until the times matches with the N2YO Website
            #call_satdump(utc_to_local(start_utc), end_utc - start_utc)
        else:
            print("No start and end time found")

if __name__ == "__main__":
    main()
