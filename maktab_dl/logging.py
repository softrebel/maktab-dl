import logging


# Define a function to set up logging
def setup_logging(log_file="maktab_dl.log", log_level=logging.INFO):
    """
    Configures logging to output to console and a rotating log file.

    Args:
        log_file (str): Path to the log file.
        log_level (int): Logging level (e.g., logging.DEBUG, logging.INFO).
    """

    # Configure httpx logging to avoid spamming logs
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)

    # Set up the logger
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # Formatter for logs
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # TODO: Add FileHandler for logging to a file
    # Ensure the directory exists for the log file
    # package_dir = get_user_default_path()
    # log_dir = os.path.join(package_dir, log_file)

    # File Handler with rotation
    # file_handler = RotatingFileHandler(
    #     log_dir, maxBytes=5 * 1024 * 1024, backupCount=5, encoding="UTF-8"
    # )
    # file_handler.setLevel(log_level)
    # file_handler.setFormatter(formatter)
    # logger.addHandler(file_handler)


# Initialize logging
setup_logging()
