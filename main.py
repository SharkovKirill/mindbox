def customer_groups_from_zero(n_customers: int) -> dict:
    """
    A function that counts the number of customers that fall into each group if the ID numbering is continuous
    and starts from 0.

    :param n_customers: number of customers
    :return: a dictionary where the keys are the number of the group and the values
             are the number of clients in this group
    """
    if n_customers - 1 > 9999999:
        raise ValueError("ID cannot be more than 7 digits")
    clients_in_groups = {}
    for customer_id in range(12, n_customers):
        sum_of_digits = 0
        while customer_id:
            sum_of_digits, customer_id = sum_of_digits + customer_id % 10, customer_id // 10
        if sum_of_digits not in clients_in_groups.keys():
            clients_in_groups[sum_of_digits] = 1
        else:
            clients_in_groups[sum_of_digits] += 1
    return clients_in_groups


def customer_groups_from_specific_id(n_customers: int, n_first_id: int) -> dict:
    """
    A function that counts the number of customers that fall into each group if the ID starts with an arbitrary number.

    :param n_customers: number of customers
    :param n_first_id: first ID in sequence
    :return: a dictionary where the keys are the number of the group and the values
             are the number of clients in this group
    """
    if n_first_id > 9999999 or n_first_id < 10000:
        raise ValueError("ID cannot be more than 7 digits or less then 5 digits")
    elif n_customers + n_first_id - 1 > 9999999:
        raise ValueError("ID cannot be more than 7 digits")
    clients_in_groups = {}
    for customer_id in range(n_first_id, n_customers + n_first_id):
        sum_of_digits = 0
        while customer_id:
            sum_of_digits, customer_id = sum_of_digits + customer_id % 10, customer_id // 10
        if sum_of_digits not in clients_in_groups.keys():
            clients_in_groups[sum_of_digits] = 1
        else:
            clients_in_groups[sum_of_digits] += 1
    return clients_in_groups
