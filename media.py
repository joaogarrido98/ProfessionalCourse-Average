mediaCurso = int(input("Media do curso?\n"))
mediaEstagios = int(input("Media estagios\n"))
pap = int(input("PAP\n"))
result = float(2 * mediaCurso + (0.3 * mediaEstagios + 0.7 * pap)) / 3
print("A média do curso é:" + str(result))
