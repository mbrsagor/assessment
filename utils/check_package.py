def category_package(package_type, categories):
    if package_type == 1 and not len(categories) < 20:
        return False
    elif package_type == 2 and not len(categories) < 50:
        return False
    else:
        return True
