from n2yo import n2yo
import json

api_key = ""
lat = 0.0
long = 0.0
alt = 0

METEOR_M2_3_ID = 57166

def main():
    session = n2yo.N2YO(api_key, lat, long, alt)
    passes = session.get_radio_passes(METEOR_M2_3_ID, 3, lat, long, alt)

    print(passes)
    print(len(passes))
    print("\n\n")

    for i in range(0, len(passes)):
        str_passes = json.dumps(passes[i])
        json_passes = json.loads(str_passes)
        
        # Error: Doesnt find the key when present
        if 'startUCT' in json_passes:
            print("Time found!")
        else:
            print("No time found!")

if __name__ == "__main__":
    main()
