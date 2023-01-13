if not (user.has_logged_in and user.is_from_chrome):
    return "our service is only available for chrome logged in user"