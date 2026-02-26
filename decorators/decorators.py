from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Invalid command. Provide name and phone number."
        except KeyError as e:
            return f"{e.args[0]}. Provide  name of an existing contact."
        except IndexError:
            return "Invalid command. Provide a valid contact name."

    return inner
