def main():
    from gtrans import translate

    translate_str = """Mr. and Mrs. Dursley, of number four, Privet Drive, \
were proud to say that they were perfectly normal, thank you very much. \
They were the last people you'd expect to be involved in anything strange or mysterious, \
because they just didn't hold with such nonsense."""

    print(translate(translate_str, "ko"))
    print(translate(translate_str, "ja"))
    print(translate(translate(translate_str, "ja"), "ko"))

if __name__ == "__main__":
    main()
