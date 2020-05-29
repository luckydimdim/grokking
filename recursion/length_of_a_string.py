def recursiveLength(testVariable):
    if not testVariable:
        return 0

    return 1 + recursiveLength(testVariable[1:])

print(recursiveLength("testVariable"))