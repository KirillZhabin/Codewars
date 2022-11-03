def duty_free(price, discount, holiday_cost):
    new_discount = price * discount / 100        # скидка
    num_of_bottle = holiday_cost // new_discount    # кол-во бутылок
    return num_of_bottle