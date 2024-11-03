import json

with open("basket.json", "r") as f:
    reader = json.load(f)
    print("The cost of the consumer basket: ")

    for m, v in reader.items():
        print(f"{m}: {v}")

    
    max_increace = 0
    max_increace_m = None
    previous_v = None

    for m, v in reader.items():
        if previous_v is not None:
            increase = v - previous_v

            if increase > max_increace:
                max_increace = increase
                max_increace_m = m

        previous_v = v

    if max_increace_m:
        print(f"month with max: {max_increace_m}")
    else:
        print(f"not found month")