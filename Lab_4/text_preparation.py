# ukr_alpha = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
# ukr_alpha = "АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгдеєжзиіїйклмнопрстуфхцчшщьюя ,.!?:;—"
ukr_alpha = "АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгдеєжзиіїйклмнопрстуфхцчшщьюя ,.!?:;"

def main():
    with open("Lab_4/pre_text.txt", mode="rt", encoding="utf-8") as ffrom:
        with open("Lab_4/out_text.txt", mode="wt", encoding="utf-8") as fto:
            for line in ffrom:
                for c in line:
                    if c == "Ґ":
                        fto.write("Г")
                    elif c == "ґ":
                        fto.write("г")
                    elif c == "\n":
                        fto.write(" ")
                    elif c in ukr_alpha:
                        fto.write(c)

if __name__ == "__main__":
    main()