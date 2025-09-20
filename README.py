import math

def main():
    people = int(input("Enter the number of people attending: "))
    perPerson = int(input("Enter the number of hot dogs each person will eat: "))

    totalHotdogs = people * perPerson

    hotdogPackages = math.ceil(totalHotdogs / 10)
    bunPackages = math.ceil(totalHotdogs / 8)

    leftoverHotdogs = hotdogPackages * 10 - totalHotdogs
    leftoverBuns = bunPackages * 8 - totalHotdogs

    print(f"Minimum number of hot dog packages required: {hotdogPackages}")
    print(f"Minimum number of hot dog bun packages required: {bunPackages}")
    print(f"Hot dogs left over: {leftoverHotdogs}")
    print(f"Hot dog buns left over: {leftoverBuns}")


main()
