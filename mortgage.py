from functools import reduce

def monthly_annuity_payment(credit_size, mortgage_year_percent, mortgage_period_in_years):
    """
    Формула рассчета ежемесячного ануитетного платежа
    """

    mortgage_month_percent = mortgage_year_percent / 12
    return credit_size * (mortgage_month_percent) / (1 - pow(1 + mortgage_month_percent, - mortgage_period_in_years * 12))


def sum_bonds_cost(purchased_bonds_cost, bonds_year_percent, cur_month):
    bonds_month_percent = bonds_year_percent / 12
    costs = [c * (1 + bonds_month_percent * (cur_month - m)) for m, c in purchased_bonds_cost.items()]
    return reduce(lambda c, s: c + s, costs)


if __name__ == "__main__":
    mortgage_year_percent = 0.04
    mortgage_first_payment_percent = 0.2
    mortgage_size = 16_000_000
    mortgage_period_in_years = 30

    bonds_year_percent = 0.12

    monthly_investments = 100_000

    credit_size = mortgage_size * (1 - mortgage_first_payment_percent)

    print("Производим минимальный платеж по ипотеке, на оставшуюся часть покупаем облигации:")
    
    bonds_cost_per_month = {}
    cur_month = 0
    remaining_credit_size = credit_size

    minimal_payment = monthly_annuity_payment(credit_size, mortgage_year_percent, mortgage_period_in_years)
    assert minimal_payment < monthly_investments

    while True:
        monthly_accrual_of_interest = remaining_credit_size * mortgage_year_percent / 12
        remaining_credit_size += monthly_accrual_of_interest

        bonds_cost_per_month[cur_month] = bonds_cost_per_month.get(cur_month, 0) + (monthly_investments - minimal_payment)
        bonds_cost = sum_bonds_cost(bonds_cost_per_month, bonds_year_percent, cur_month)

        if remaining_credit_size <= (minimal_payment + bonds_cost):
            print("Year: %s, month: %s, credit_size: %s, minimal_payment: %s, bonds_cost: %s"
                % (round(cur_month / 12), cur_month % 12, round(remaining_credit_size), round(minimal_payment), round(bonds_cost)))
            break

        if cur_month % 12 == 0 and cur_month != 0:
            bonds_cost_per_month = {cur_month: bonds_cost}

        # print("Year: %s, month: %s, credit_size: %s, minimal_payment: %s, bonds_cost: %s"
        #       % (round(cur_month / 12), cur_month % 12, round(remaining_credit_size), round(minimal_payment), round(bonds_cost)))

        cur_month += 1
        remaining_credit_size -= minimal_payment

    print()
    print("Выплачиваем ипотеку досрочно:")
    
    cur_month = 0
    remaining_credit_size = credit_size
    while True:
        monthly_accrual_of_interest = remaining_credit_size * mortgage_year_percent / 12
        remaining_credit_size += monthly_accrual_of_interest

        minimal_payment = monthly_annuity_payment(remaining_credit_size, mortgage_year_percent, mortgage_period_in_years)
        assert minimal_payment < monthly_investments

        if remaining_credit_size <= monthly_investments:
            print("Year: %s, month: %s"
                % (round(cur_month / 12), cur_month % 12))
            break

        # print("Year: %s, month: %s, credit_size: %s, minimal_payment: %s"
        #       % (round(cur_month / 12), cur_month % 12, round(remaining_credit_size), round(minimal_payment)))

        cur_month += 1
        remaining_credit_size -= monthly_investments
