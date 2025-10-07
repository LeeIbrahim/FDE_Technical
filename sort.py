
def sort(width: int, height: int, length: int, mass: int) -> str:
    HEAVY: int = 20
    BULKY: int = 150
    BULKY_AREA: int = 1000000

    isHeavy: bool = False
    isBulky: bool = False

    if mass >= HEAVY:
        isHeavy = True

    if width * height * length >= BULKY_AREA or max(width, height, length) >= BULKY:
        isBulky = True


    if isHeavy and isBulky:
        return "REJECTED"
    elif isHeavy or isBulky:
        return "SPECIAL"
    return "STANDARD"
    


if __name__ == "__main__":
    #test cases
    assert(sort(10, 20, 30, 10) == "STANDARD")
    assert(sort(100, 20, 30, 40) == "SPECIAL")
    assert(sort(100, 200, 300, 40) == "REJECTED")
    assert(sort(10, 20, 30, 50) == "SPECIAL")
    assert(sort(10, 20, 30, 10) == "STANDARD")
    assert(sort(10, 20, 30, 200) == "SPECIAL")