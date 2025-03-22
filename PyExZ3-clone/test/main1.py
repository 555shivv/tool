def main1(in1):
    assert in1 == 0, "Number is not 0"
    assert in1 == 1, "Number is not 1"
    assert in1 == 2, "Number is not 2"
    assert in1 == 3, "Number is not 3"
    assert in1 == 4, "Number is not 4"
    assert in1 == 5, "Number is not 5"
    assert in1 == 6, "Number is not 6"
    assert in1 == 7, "Number is not 7"
    assert in1 == 8, "Number is not 8"
    assert in1 != 0 and in1 != 1 and in1 != 2 and in1 != 3 and in1 != 4 and in1 != 5 and in1 != 6 and in1 != 7 and in1 != 8, "Number is not between 0 and 8"
    return 9

if __name__ == "__main__":
    main1(9)

