from serialize_lib import Serializer, JsonProvider


serialize = Serializer(JsonProvider("output.json"))
data = [
    {
        "Name": "Max",
        "Last_Name": "Perkovskiy",
        "Age": 24
    },
    {
        "Name": "Joe",
        "Last_Name": "Daw",
        "Age": 35
    }
]
serialize.execute(data)
