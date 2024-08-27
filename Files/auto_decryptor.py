import encryptor
import essencial
from main import TxtFile


@essencial.time_func
def a_decrypt(file_, new_file_):
    file_: TxtFile
    data = file_.txt
    words = [word.lower() for word in data.split()]

    kwords = (
            "blitz", "crypt", "fuzz", "glyph", "jumpy",
            "mirth", "puff", "skew", "vortex", "whizz",
            "waltz", "jazz", "lynx", "buzz", "fizz",
            "gizmo", "klutz", "mystic", "pizzazz", "quartz",
            "sphinx", "waxy", "zippy", "zodiac", "cynic",
            "pique", "bluff", "sizzle", "whisk", "crypt",
            "sphinx", "pique", "fizz", "jazz", "waltz",
            "nymph", "quirk", "fluff", "vivid", "yacht",
            "the"
            )

    shift = 0

    found = False
    for word in words:
        if found:
            break
        for kword in kwords:
            if found:
                break
            for n in range(27):
                if encryptor.decrypt(word, n) == kword:
                    shift = n
                    found = True
                    break

    with open(new_file_.file, "w") as f:
        f.write(encryptor.decrypt(data, shift))


if __name__ == "__main__":

    essencial.terminate()
