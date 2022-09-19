def main():
    dollars = dollars_to_float(input("What is the bill total? "))
    percent = percent_to_float(input("What percent would yo ulike to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    d = float(d)
    return d

def percent_to_float(p):
    p = float(p)
    p = p * .01
    return p

main()
