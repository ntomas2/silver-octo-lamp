import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', choices=['diff', 'annuity'])
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')
parser.add_argument('--payment')
args = parser.parse_args()
annuity_parameters1 = [args.periods, args.interest, args.payment]
annuity_parameters2 = [args.principal, args.interest, args.payment]
annuity_parameters3 = [args.principal, args.periods, args.interest]
annuity_correct_parameters = [all(annuity_parameters1), all(annuity_parameters2), all(annuity_parameters3)]
diff_correct_parameters = [args.principal, args.periods, args.interest]
if args.type == 'diff' and all(diff_correct_parameters):
    loan_principal = int(args.principal)
    periods = int(args.periods)
    loan_interests = float(args.interest)
    correct_args = [loan_principal > 0, periods > 0, loan_interests > 0]
    if all(correct_args):
        nominalInterestRate = loan_interests / (12 * 100)
        total_payment = 0
        for m in range(1, periods + 1):
            monthly_payment = loan_principal / periods + nominalInterestRate * (
                    loan_principal - (loan_principal * (m - 1) / periods)
            )
            total_payment += math.ceil(monthly_payment)
            print(f'Month {m}: payment is {math.ceil(monthly_payment)}')
        print()
        print(f'Overpayment = {total_payment - loan_principal}')
    else:
        print('Incorrect parameters')
if args.type == 'annuity' and any(annuity_correct_parameters):
    if not args.principal:
        annuity_payments = float(args.payment)
        periods = int(args.periods)
        loan_interests = float(args.interest)
        correct_args = [annuity_payments > 0, periods > 0, loan_interests > 0]
        if all(correct_args):
            nominalInterestRate = loan_interests / (12 * 100)
            loan_principal = annuity_payments / ((nominalInterestRate * math.pow(1 + nominalInterestRate, periods))
                                                 / (math.pow(1 + nominalInterestRate, periods) - 1))
            print(f'Your loan principal = {math.floor(loan_principal)}!')
            print(f'Overpayment = {math.ceil(annuity_payments * periods - loan_principal)}')
        else:
            print('Incorrect parameters')
    if not args.periods:
        loan_principal = int(args.principal)
        monthly_payment = float(args.payment)
        loan_interests = float(args.interest)
        correct_args = [loan_principal > 0, monthly_payment > 0, loan_interests > 0]
        if all(correct_args):
            nominalInterestRate = loan_interests / (12 * 100)
            numberOfMonths = math.ceil(
                math.log((monthly_payment / (monthly_payment - nominalInterestRate * loan_principal)),
                         1 + nominalInterestRate))
            if numberOfMonths % 12 == 0:
                print(f'It will take {numberOfMonths // 12} years to repay this loan!')
                print(f'Overpayment = {monthly_payment * numberOfMonths - loan_principal}')
            else:
                print(f'It will take {numberOfMonths // 12} years and {numberOfMonths % 12} months to repay this loan!')
                print(f'Overpayment = {math.ceil(monthly_payment * numberOfMonths) - loan_principal}')
        else:
            print('Incorrect parameters')
    if not args.payment:
        loan_principal = int(args.principal)
        periods = int(args.periods)
        loan_interests = float(args.interest)
        correct_args = [loan_principal > 0, periods > 0, loan_interests > 0]
        if all(correct_args):
            nominalInterestRate = loan_interests / (12 * 100)
            annuity_payments = loan_principal * ((nominalInterestRate * math.pow(1 + nominalInterestRate, periods))
                                                 / (math.pow(1 + nominalInterestRate, periods) - 1))
            print(f'Your monthly payment = {math.ceil(annuity_payments)}!')
            print(f'Overpayment = {math.ceil(annuity_payments) * periods - loan_principal}')
        else:
            print('Incorrect parameters')
else:
    print('Incorrect parameters')
