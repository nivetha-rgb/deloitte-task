import json
import datetime

# Convert Format 1
def convertFromFormat1(jsonObject):
    locationParts = jsonObject["location"].split("/")

    return {
        "deviceID": jsonObject["deviceID"],
        "deviceType": jsonObject["deviceType"],
        "timestamp": jsonObject["timestamp"],
        "location": {
            "country": locationParts[0],
            "city": locationParts[1],
            "area": locationParts[2],
            "factory": locationParts[3],
            "section": locationParts[4]
        },
        "data": {
            "status": jsonObject["operationStatus"],
            "temperature": jsonObject["temp"]
        }
    }

# Convert Format 2
def convertFromFormat2(jsonObject):
    date = datetime.datetime.strptime(jsonObject["timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
    timestamp = int((date - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)

    return {
        "deviceID": jsonObject["device"]["id"],
        "deviceType": jsonObject["device"]["type"],
        "timestamp": timestamp,
        "location": {
            "country": jsonObject["country"],
            "city": jsonObject["city"],
            "area": jsonObject["area"],
            "factory": jsonObject["factory"],
            "section": jsonObject["section"]
        },
        "data": jsonObject["data"]
    }

# Main logic
def main(jsonObject):
    if jsonObject.get("device") is None:
        return convertFromFormat1(jsonObject)
    else:
        return convertFromFormat2(jsonObject)

# Run program
if __name__ == "__main__":
    with open("data-1.json") as f:
        data1 = json.load(f)

    with open("data-2.json") as f:
        data2 = json.load(f)

    result1 = main(data1)
    result2 = main(data2)

    print("Result from data-1.json:")
    print(json.dumps(result1, indent=4))

    print("\nResult from data-2.json:")
    print(json.dumps(result2, indent=4))
