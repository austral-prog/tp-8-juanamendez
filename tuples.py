"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    record=record[1]
    return record


def convert_coordinate(coordinate):
    c1=coordinate[0]
    c2=coordinate[1]
    return (c1,c2)


def create_record(azara_record, rui_record):
    c1=azara_record[1][0]
    c2=azara_record[1][1]
    CA=(c1,c2)
    if CA==rui_record[1]:
        return (azara_record[0],azara_record[1],rui_record[0], rui_record[1], rui_record[2])
