def find_element_by_xpath(driver, name, ignore_message=True):
    """Finds an element in the current page by its xpath.

    Args:
        driver: The WebDriver instance to use.
        name: The name of the element to find.
        ignore_message: Whether to ignore the message that is printed when the
            element is not found.

    Returns:
        The element if it is found, or None otherwise.
    """

    try:
        return driver.find_element_by_xpath(name)
    except NoSuchElementException:
        if not ignore_message:
            print('Element not found: {}'.format(name))
        return None

