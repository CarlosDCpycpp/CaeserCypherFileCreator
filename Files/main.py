import encryptor
import auto_decryptor
import essencial


class TxtFile:
    def __init__(self, file, new=False):
        self.file = file
        if new:
            self.txt = ""
        else:
            with open(self.file, "r") as file_:
                self.txt = file_.read()

    def lower(self):
        self.txt = self.txt.lower()

    def write(self, content):
        with open(self.file, "w") as file_:
            file_.write(content)

    def update(self):
        with open(self.file, "r") as file_:
            self.txt = file_.read()


@essencial.time_func
def encrypt_file(og_file, new_file, shift_):
    with open(new_file.file, "w") as n_f:
        n_f.write(encryptor.encrypt(og_file.txt, shift_))


@essencial.time_func
def decrypt_file(og_file, new_file, shift_):
    with open(new_file.file, "w") as n_f:
        n_f.write(encryptor.decrypt(og_file.txt, shift_))


def main():
    print("1 -> encrypt\n2 -> decrypt\n3 -> auto-decrypt\n")
    while True:
        input_ = input("-> ")

        if input_ == "1":  # encrypt
            file_a_name = input("Enter original file name (include extension): ")
            file_a = TxtFile(file_a_name)
            shift = int(input("Enter shift: "))  # Convert shift to integer

            input_a = input("Would you like to choose the name of the new file [y/n]: ").lower()
            if input_a == "y":  # name file
                new_file_name = input("Enter new file name (include extension): ")
            else:
                new_file_name = "hello_world_auto_decrypted.txt"

            new_file = TxtFile(new_file_name)

            encrypt_file(file_a, new_file, shift)
            print("Done")
            essencial.terminate()

        elif input_ == "2":  # decrypt
            file_a_name = input("Enter original file name (include extension): ")
            file_a = TxtFile(file_a_name)
            shift = int(input("Enter shift: "))  # Convert shift to integer

            input_a = input("Would you like to choose the name of the new file [y/n]: ").lower()
            if input_a == "y":  # name file
                new_file_name = input("Enter new file name (include extension): ")
            else:
                new_file_name = "hello_world_auto_decrypted.txt"

            new_file = TxtFile(new_file_name, True)

            decrypt_file(file_a, new_file, shift)
            print("Done")
            essencial.terminate()

        elif input_ == "3":  # auto-decrypt
            file_a_name = input("Enter original file name (include extension): ")
            file_a = TxtFile(file_a_name)

            input_a = input("Would you like to choose the name of the new file [y/n]: ").lower()
            if input_a == "y":  # name file
                new_file_name = input("Enter new file name (include extension): ")
            else:
                new_file_name = "hello_world_auto_decrypted.txt"

            new_file = TxtFile(new_file_name, True)
            auto_decryptor.a_decrypt(file_a, new_file)
            print("Done")
            essencial.terminate()

        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()

    essencial.terminate()
