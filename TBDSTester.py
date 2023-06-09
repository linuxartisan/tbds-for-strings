from TBDS import TBDS

def main():
    tbds = TBDS()

    tbds.add("a", "a")
    tbds.add("an", "an")
    tbds.add("mam", "mam")
    tbds.add("and", "and")
    tbds.add("man", "man")
    tbds.add("ant", "ant")
    tbds.add("many", "many")
    tbds.add("zoom", "zoom")
    tbds.add("zoo", "zoo")

    tbds.print()
    print()

    tbds.add("anti", "anti")
    tbds.add("zone", "zone")
    tbds.add("mad", "mad")
    tbds.add("ann", "ann")
    tbds.add("anne", "anne")

    tbds.print()
    print()

    print("Checking for count")
    print(tbds.count())

    print("Checking for keys:")

    key = "man"
    print(key, ":", tbds.containsKey(key))

    key = "zone"
    print(key, ":", tbds.containsKey(key))

    key = "m"
    print(key, ":", tbds.containsKey(key))

    key = "ma"
    print(key, ":", tbds.containsKey(key))

    key = "mam"
    print(key, ":", tbds.containsKey(key))

    key = "mar"
    print(key, ":", tbds.containsKey(key))

    key = "act"
    print(key, ":", tbds.containsKey(key))

    key = "z"
    print(key, ":", tbds.containsKey(key))

    key = "ann"
    print(key, ":", tbds.containsKey(key))

    key = "anne"
    print(key, ":", tbds.containsKey(key))

    print()


    print("Get values for keys:")

    key = "ma"
    print(key, ":", tbds.get(key))

    key = "zoom"
    print(key, ":", tbds.get(key))

    key = "act"
    print(key, ":", tbds.get(key))

    key = "ant"
    print(key, ":", tbds.get(key))

    key = "a"
    print(key, ":", tbds.get(key))

    key = "kick"
    print(key, ":", tbds.get(key))

    key = "an"
    print(key, ":", tbds.get(key))

    key = "and"
    print(key, ":", tbds.get(key))

    key = "anti"
    print(key, ":", tbds.get(key))

    key = "antil"
    print(key, ":", tbds.get(key))

    key = "ann"
    print(key, ":", tbds.get(key))

    print()


    print("Keys for prefix:")

    prefix = "mad"
    print("Keys (", prefix, ") :", tbds.getKeysForPrefix(prefix))

    prefix = "an"
    print("Keys (", prefix, ") :", tbds.getKeysForPrefix(prefix))

    prefix = ""
    print("Keys (", prefix, ") :", tbds.getKeysForPrefix(prefix))

    prefix = "cli"
    print("Keys (", prefix, ") :", tbds.getKeysForPrefix(prefix))


if __name__ == "__main__":
    main()
