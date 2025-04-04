import logging
import constants
import hello

def configure_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d :message:  %(message)s ",
        handlers=[logging.FileHandler("logs.log"), logging.StreamHandler()],
    )


if __name__ == "__main__":
    configure_logging()
    try:
        for word in constants.WORDLIST:
            try:
                logging.debug(word)
                assert isinstance(word, str)
            except Exception as e:
                logging.error(e)
                logging.exception(f"Word {word} is not a string")
        logging.info("This is an info entry!")        
    except:
        logging.exception("An error occurred")
    finally:
        hello.sayHi()


# DEBUG -> INFO -> WARNING-> ERROR -> CRITICAL
