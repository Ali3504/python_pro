None
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşılık cevap",
            "SHEESH": "onaylamamak",
            "CREEPY": "korkunç",
            "AGGRO": "agresifleşmek/sinirlenmek"
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
    print("Kelime sözlükte var")
    if word == "CRINGE":
        print("Garip ya da utandırıcı bir şey")

    if word == "LOL":
         print("Komik bir şeye verilen cevap")

    if word == "ROFL":
         print("Garip ya da utandırıcı bir şey")

    if word == "SHEESH":
         print("Garip ya da utandırıcı bir şey")

    if word == "CREEPY":
         print("Garip ya da utandırıcı bir şey")

    if word == "AGGRO":
         print("Garip ya da utandırıcı bir şey")
    # Kelime eşleşiyorsa ne yapmalıyız?
else:
    print("Böyle bir kelime bulunamadı")
    # Kelime eşleşmiyorsa ne yapmalıyız?
