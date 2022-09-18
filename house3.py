x = input("Name? ").lower()

match x:
    case "harry":
        print("Gryffindor")
    case "hermione":
        print("Gryffindor")
    case "ron":
        print("Gryffindor")
    case "draco":
        print("Slytherin")
    case _:
        print("Who?")