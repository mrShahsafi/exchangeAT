# Django
from django.utils.timezone import now
from backend.settings import BASE_DIR


def get_first_matching_attr(obj, *attrs, default=None):
    for attr in attrs:
        if hasattr(obj, attr):
            return getattr(obj, attr)

    return default


def find_mailing_path(web_app=None, module=None):
    """
        this function will generate the path of an e-mail\
            directory to reduce hard-code action.
    :param web_app:
    :param module:
    :return: email template path
    """
    if web_app is None:
        path = f"emails/{module}"
    else:
        path = f"{web_app}/emails/{module}"

    return path


def get_n_first_chars(text: str, limit=512):
    return text[:limit]


def get_request_language(request):
    try:
        lang = request.headers.get("site-language")
        return lang
    except Exception:
        return "en-us"


def write_log(log_file, status, url, error=None):
    try:
        logs_url = f"{BASE_DIR}/logs/{log_file}.log"
        file_object = open(f"{logs_url}", "a")

        file_object.write(
            f'time={now().strftime("%X %d/%m/%Y %Z")} -- path={url} -- status={status} -- error={error} end. \n'
        )
        file_object.close()
    except Exception:
        pass
