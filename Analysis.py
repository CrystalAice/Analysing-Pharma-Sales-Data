#importing libraries
import pandas as pd
import matplotlib.pyplot as plot

#loading dataset
def loading_and_clean():
    #opening the dataset
    salesdaily = pd.read_csv('salesdaily.csv')
    salesdaily['datum'] = pd.to_datetime(salesdaily["datum"])

    #cleaning the data
    salesdaily = salesdaily.drop_duplicates()
    atc_col = ["M01AB", "M01AE", "N02BA", "N02BE", "N05B", "N05C", "R03", "R06"]
    salesdaily[atc_col] = salesdaily[atc_col].apply(pd.to_numeric, errors='coerce')
    salesdaily = salesdaily[(salesdaily[atc_col] >= 0).all(axis=1)]

    return salesdaily

data_table = loading_and_clean()
print(data_table)

#calculating total quantity sold for each drug category (ATC code)
def total_quantity():
    salesdaily = loading_and_clean()
    atc_col = ["M01AB", "M01AE", "N02BA", "N02BE", "N05B", "N05C", "R03", "R06"]
    #summing up the columns
    total_q = salesdaily[atc_col].sum()

    return total_q

totals = total_quantity()
print(totals)

print("\n The N05B has the highest total quantity.\n") #the highest total sales quantity(daily)

def by_month(): #highest in January 2015, July 2016, September 2017
    sales_by_month = loading_and_clean()

    #for January 2015
    jan_2015 = sales_by_month[
    (sales_by_month["datum"].dt.year == 2015) & 
    (sales_by_month["datum"].dt.month == 1)]

    #for July 2016
    jul_2016 = sales_by_month[
    (sales_by_month["datum"].dt.year == 2016) & 
    (sales_by_month["datum"].dt.month == 7)]

    #for September 2017
    sep_2017 = sales_by_month[
    (sales_by_month["datum"].dt.year == 2017) & 
    (sales_by_month["datum"].dt.month == 9)]

    #sum up the total sales to find the highest
    atc_col = ["M01AB", "M01AE", "N02BA", "N02BE", "N05B", "N05C", "R03", "R06"]
    total_sales_jan = jan_2015[atc_col].sum().sort_values(ascending = False).head(3)
    total_sales_jul = jul_2016[atc_col].sum().sort_values(ascending = False).head(3)
    total_sales_sep = sep_2017[atc_col].sum().sort_values(ascending = False).head(3)

    return total_sales_jan, total_sales_jul, total_sales_sep

print("\n The highest sold drugs in January 2015, July 2016, and September 2017 are:\n")

totals_monthly = by_month()
for total in totals_monthly:
    print(f"{total}\n")

def year():
    sales_in_2017 = loading_and_clean()

    #ranking 2017 sales
    sales_in_2017 = sales_in_2017[sales_in_2017["datum"].dt.year == 2017]
    atc_col = ["M01AB", "M01AE", "N02BA", "N02BE", "N05B", "N05C", "R03", "R06"]
    sales_in_2017 = sales_in_2017[atc_col].sum()
    sales_in_2017 = sales_in_2017.sort_values(ascending = False).head(1)

    return sales_in_2017

print("\nThe highest selling drug in 2017 is:\n")

sales2017 = year()
print(f"{sales2017}\n")

def avg_dailysales():
    sales_avg = loading_and_clean()

    #calculating the average daily sales
    atc_col = ["M01AB", "M01AE", "N02BA", "N02BE", "N05B", "N05C", "R03", "R06"]
    sales_avg = sales_avg[atc_col].mean()
    sales_avg = sales_avg.sort_values(ascending = False).head(1)

    return sales_avg

print("\nDrug with the highest average is:\n")

avg_sales = avg_dailysales()
print(f"{avg_sales}\n")

#plotting the data
atc_col = ["M01AB", "M01AE", "N02BA", "N02BE", "N05B", "N05C", "R03", "R06"]
graph_data = loading_and_clean()

#plotting the totals' graph
totals = graph_data[atc_col].sum()
totals.plot(kind = 'bar')
plot.title("Total Quantity per Drug.")
plot.show()

#plotting the R03 vs months group
r03_monthly = graph_data.groupby("Month")["R03"].sum()
r03_monthly.plot(kind = "line")
plot.title('R03 per month')
plot.show()

print("\nRespiratory drugs are sold more during the months of February to April.")

