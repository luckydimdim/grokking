def decimalToBinary(testVariable) :
  if testVariable <= 1:
    return str(testVariable)

  return decimalToBinary(testVariable // 2) + decimalToBinary(testVariable % 2)

print(decimalToBinary(11))