a = open("motto.txt", "w")

a.write("Fiat Lux!")

a.close()

a = open("motto.txt", "a")

a.write("\nLet there be light!")

a.close()