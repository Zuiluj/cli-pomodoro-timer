"""Top-level package for pmodoro cli"""

__app_name__ = "pmodoro"
__version__ = "0.1.0"

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    JSON_ERROR,
    ID_ERROR,
) = range(5)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    ID_ERROR: "to-do id error",
}
