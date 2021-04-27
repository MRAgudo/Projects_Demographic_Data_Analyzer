import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    
    # What is the average age of men?
    sex_male = df[df['sex'] == 'Male']
    average_age_men = round(sex_male['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    ed_count = df['education'].value_counts()
    ed_total = ed_count.sum()
    bach_count = ed_count['Bachelors'].sum()
    percentage_bachelors = round(bach_count/ed_total * 100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?

    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    overfifty = df[['salary','education']].value_counts()['>50K']
    overfifty_higher = overfifty[['Bachelors','Masters','Doctorate']].sum()
    underfifty = df[['salary','education']].value_counts()['<=50K']
    underfifty_higher = underfifty[['Bachelors','Masters','Doctorate']].sum()
    
    overfifty_lower = overfifty.sum() - overfifty_higher
    underfifty_lower = underfifty.sum() - underfifty_higher
    
    #adv_ed_fifty = advanced_ed['>50K']

    # percentage with salary >50K
    higher_education_rich = round(overfifty_higher / (overfifty_higher+underfifty_higher) * 100,1)
    
    lower_education_rich = round(overfifty_lower / (overfifty_lower+underfifty_lower) * 100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()


    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None

    salary_min_hrs = df[['hours-per-week','salary']].value_counts()

    rich_percentage = salary_min_hrs[min_work_hours]['>50K'] / salary_min_hrs[min_work_hours].sum() * 100

    # What country has the highest percentage of people that earn >50K?
    overfifty_country = df[df['salary'] == '>50K'].groupby('native-country')['native-country'].count()
    country_total_sal = df.groupby('native-country')['native-country'].count()
    highest_earning_country = (overfifty_country / country_total_sal * 100).idxmax()
    highest_earning_country_percentage = round((overfifty_country / country_total_sal * 100).max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_info = df[df['native-country'] == 'India']
    top_IN_occupation = india_info[india_info['salary'] == '>50K'].groupby('occupation')['occupation'].count().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print("Country with highest percentage of rich:",
              highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
