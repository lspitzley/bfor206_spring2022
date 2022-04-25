"""
Functions to parse information from
IRC chat files.

"""
#%%
import re


def sanity_check():
    """This test should always pass.
    The purpose is to make sure Github actions are functioning properly.
    """
    return True

def get_chat_message(row):
    
    message = re.split(r'> ', row)
    # print(message)
    # return the second part of the split.
    # and join, just in case there is another '> ' in the message
    return "> ".join(message[1:])


def get_current_date(dateline):
    """    Parse the IRC log date format to find the current date

    Return a POSIX (datetime) form date for midnight

    Args:
        dateline (str): Row that begins with `---`

    Returns:
        datetime: datetime object with the date from the row 
    """

    pass


def get_hours_minutes(time_row):
    """ covered in class 11-2 """
    pass



def get_join_quit_type(row):
    """Returns if a row is a join or a quit,


    Args:
        row (str): join or quit row

    Returns:
        str: "join" or "quit"
    """
    pass


def get_join_quit_username(row):
    """ Input a join/quit row, get a username back.

    Args:
        row (str): Must be a join/quit row. These
        have `-!-` after the timestamp.

    Returns:
        str: the username from the row.
    """
    pass

def get_user_name(row):
    """
    Find the username in a chat row.

    Parameters
    ----------
    row : str
        row that contains a message.

    Returns
    -------
    string
        string with username.

    """
    pass



def get_user_prefix(row):
    """ Gets the prefix of a username, if any.
    If there is not a prefix, return None.

    For example, '@' or '+'.

    Args:
        row (str): chat message row.

    Returns:
        str: the user prefix (if any)
    """
    pass

def is_date_row(row):
    """
    Check if row indicates date change.
    Row contains --- at the start

    Parameters
    ----------
    row : TYPE
        DESCRIPTION.

    Returns
    -------
    bool
        DESCRIPTION.

    """
    if re.search(r'---', row):
        return True
    return False
    


def is_join_quit(row):
    """
    Check if message is a join/quit/metadata row.
    Row contains -!- at the start

    Parameters
    ----------
    row : str
        row that you want to check.
    

    Returns
    -------
    bool
        DESCRIPTION.

    """
    pass


def is_message(row):
    """
    Determine if a row contains a message.

    Parameters
    ----------
    row : str
        row from chat log.

    Returns
    -------
    bool
        True if row belongs to chat log.

    """
    if row[6] == '<':
        return True
    return False


def find_urls(text):
    pass
    















