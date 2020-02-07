import sys
std_deduction = 50000
taxable_hra = 0
while True:
    print("\n T A X   C A L C U L A T O R \n")
    tax_option = int(input('''Enter the tax regime you would like to opt for:
            1 - FY 2019-20
            2 - FY 2020-21
            Your Choice :   '''))
    if tax_option > 2 or tax_option <= 0:
        print("Invalid Choice")
        break
    else:

        print("INCOME : ")
        print("--------------------------------------------------------------")
        ctc = float(input("\tEnter your CTC : "))
        print("\n")
        basic = 0.4 * ctc

        if tax_option == 1:
            print("HRA : ")
            print("--------------------------------------------------------------")
            hra_recieved = float(input("\tEnter HRA recieved per annum : "))
            rent = float(input("\tEnter Total Rent paid per annum : "))
            city = int(input('''\tAre you from Metropolitan City ? :
                                Press 1 for YES
                                Press 2 for NO
                                Your Choice : '''))
            print("\n")
            # HRA can be claimed in three ways
            # 1. Rent - 10% of basic
            # 2. Actual HRA
            # 3. 50% or 40% of basic
            # Select lowest one
            hra_1 = rent - 0.1 * basic
            hra_2 = hra_recieved
            if city == 1:
                hra_3 = 0.5 * basic
            else:
                hra_3 = 0.4 * basic
                min_hra = min(hra_1, hra_2, hra_3)
                if min_hra <= 0:
                    taxable_hra = hra_recieved
                else:
                    taxable_hra = min_hra

            print("DEDUCTIONS : ")
            print("--------------------------------------------------------------")
            # taking only EPF and Investments under 80C along with home loan
            EPF = float(input("\tEnter EPF : "))
            i80C = float(input("\tEnter Investments under 80C : "))
            i80D = float(input("\tEnter Investments under 80D : "))
            i80 = float(input("\tEnter Investments under sec 80 (other than C and D and E) : "))
            home_loan = float(input("\tEnter Home Loan: "))
            education_loan = float(input("\tEnter Education Loan Interest amount: "))
            print("\n")
            if EPF + i80C >= 150000:  # max allowance is 1.5 lakhs
                if home_loan >= 200000: #max allowance is 2 lakhs
                    if i80D >= 150000:
                        if i80 >= 100000:
                            deductions = 600000 + education_loan
                        else:
                            deductions = 500000 + i80 + education_loan
                    else:
                        if i80 >= 100000:
                            deductions = 450000 + i80D + education_loan
                        else:
                            deductions = 350000 + i80 + i80D + education_loan
                else:
                    if i80D >= 150000:
                        if i80 >= 100000:
                            deductions = 400000 + home_loan + education_loan
                        else:
                            deductions = 300000 + i80 + home_loan + education_loan
                    else:
                        if i80 >= 100000:
                            deductions = 250000 + home_loan + i80D + education_loan
                        else:
                            deductions = 150000 + home_loan + i80D + i80 + education_loan
            else:
                if home_loan >= 200000:
                    if i80D >= 150000:
                        if i80 >= 100000:
                            deductions = EPF + i80C + 450000 + education_loan
                        else:
                            deductions = EPF + i80C + 350000 + i80 + education_loan
                    else:
                        if i80 >= 100000:
                            deductions = EPF + i80C + i80D + 300000 + education_loan
                        else:
                            deductions = EPF + i80C + i80D + i80 + 200000 + education_loan
                else:
                    if i80D >= 150000:
                        if i80 >= 100000:
                            deductions = EPF + i80C + home_loan + 250000 + education_loan
                        else:
                            deductions = EPF + i80C + i80D + home_loan + i80 + 150000 + education_loan
                    else:
                        if i80 >= 100000:
                            deductions = EPF + i80C + i80D + home_loan + 100000 + education_loan
                        else:
                            deductions = EPF + i80C + i80D + home_loan + i80 + education_loan

            # gross salary = ctc - (EPF + gratuity)
            # there is no gratuity
            gross_salary = ctc - EPF
            # calculating total taxable income (also known as Gross Taxable income)
            # Taxable Income = Gross Salary – Section 80C deduction – Standard Deduction – HRA – Professional Tax
            # There is no professional tax
            taxable_income = gross_salary - std_deduction - taxable_hra - (deductions - EPF)
            # Calculating Tax
            # Tax Slab for fy 2019-20
            if taxable_income < 250000:
                final_tax = 0
            elif 250000 < taxable_income < 500000:
                tax = 0.05 * (taxable_income - 250000)
                final_tax = tax + (0.04 * tax)
            elif 500000 < taxable_income < 1000000:
                tax = 12500 + (0.2 * (taxable_income - 500000))
                final_tax = tax + (0.04 * tax)
            elif 1000000 < taxable_income < 5000000:
                tax = 112500 + (0.312 * (taxable_income - 1000000))
                final_tax = tax + (0.04 * tax)
            elif 5000000 < taxable_income < 10000000:
                tax = 112500 + (0.3432 * (taxable_income - 1000000))
                final_tax = tax + (0.04 * tax)

        if tax_option == 2:
            print("HRA : ")
            print("--------------------------------------------------------------")
            hra_recieved = 0.0
            rent = 0.0
            city = 0
            print("You will not get HRA or rent!!!")
            print("\n")
            taxable_hra = hra_recieved
            print("DEDUCTIONS : ")
            print("--------------------------------------------------------------")
            EPF = float(input("\tEnter EPF : "))
            i80C = float(input("\tEnter Investments under 80C : "))
            i80D = float(input("\tEnter Investments under 80D : "))
            home_loan = float(input("\tEnter Home Loan: "))
            print("There will be NO deductions on EPF, Ivestments under 80C or home loan!")
            print("\n")
            deductions = 0.0

            # gross salary = ctc - (EPF + gratuity)
            # there is no gratuity
            gross_salary = ctc - EPF
            # calculating total taxable income (also known as Gross Taxable income)
            # Taxable Income = Gross Salary – Section 80C deduction – Standard Deduction – HRA – Professional Tax
            # There is no professional tax
            taxable_income = gross_salary - taxable_hra
            # Calculating Tax
            # Tax slab for fy 2020-21
            if taxable_income < 250000:
                final_tax = 0
            elif 250000 < taxable_income < 500000:
                tax = 0.05 * (taxable_income - 250000)
                final_tax = tax + (0.04 * tax)
            elif 500000 < taxable_income < 750000:
                tax = 25000 + (0.104 * (taxable_income - 500000))
                final_tax = tax + (0.04 * tax)
            elif 750000 < taxable_income < 1000000:
                tax = 37500 + (0.156 * (taxable_income - 750000))
                final_tax = tax + (0.04 * tax)
            elif 1000000 < taxable_income < 1250000:
                tax = 62500 + (0.208 * (taxable_income - 1000000))
                final_tax = tax + (0.04 * tax)
            elif 1250000 < taxable_income < 1500000:
                tax = 75000 + (0.26 * (taxable_income - 1250000))
                final_tax = tax + (0.04 * tax)
            elif 1500000 < taxable_income < 5000000:
                tax = 75000 + (0.312 * (taxable_income - 1500000))
                final_tax = tax + (0.04 * tax)
            elif 5000000 < taxable_income < 10000000:
                tax = 85800 + (0.3432 * (taxable_income - 1500000))
                surcharge = 1.1 * tax
                final_tax = surcharge + (0.04 * tax)

        print("FINAL REPORT : ")
        print("--------------------------------------------------------------")
        print("\t\tBASIC INCOME : ", basic)
        print("\t\tGROSS SALARY:", gross_salary)
        print("\t\tHRA EXEMPTION : ", taxable_hra)
        print("\t\tTAXABLE INCOME : ", taxable_income)
        print("\t\tT A X : ", int(final_tax))
        # Take Home Salary = Gross Salary – (Income Tax + Professional Tax)
        print("\t\tTAKE-HOME SALARY : ", gross_salary - final_tax)
        print("\n")

        while True:
            choice = int(input('''Press 1 to Calculate again\nPress 2 to Exit '''))
            if choice == 1:
                break
            elif choice == 2:
                sys.exit()
            else:
                print("Invalid Choice")
                continue
