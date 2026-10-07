import pandas as pd


def calculate_demographic_data(print_data=True):
    # 1. قراءة البيانات من ملف CSV
    df = pd.read_csv('adult.data.csv')

    # 2. كم عدد الأشخاص من كل عرْق (race)؟
    race_count = df['race'].value_counts()

    # 3. متوسط عمر الرجال
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 4. نسبة الأشخاص الحاصلين على شهادة البكالوريوس (Bachelors)
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 5. تحديد أصحاب التعليم العالي وغير العالي
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # نسبة من يتقاضون أكثر من 50K بين أصحاب التعليم العالي
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)

    # نسبة من يتقاضون أكثر من 50K بين من ليس لديهم تعليم عالٍ
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)

    # 6. الحد الأدنى لساعات العمل في الأسبوع
    min_work_hours = df['hours-per-week'].min()

    # 7. نسبة من يتقاضون أكثر من 50K من الذين يعملون الحد الأدنى من الساعات
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # 8. الدولة التي لديها أعلى نسبة من الأشخاص الذين يتقاضون >50K ونسبتهم
    country_counts = df['native-country'].value_counts()
    country_rich_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_rich_percentage = (country_rich_counts / country_counts) * 100

    highest_earning_country = country_rich_percentage.idxmax()
    highest_earning_country_percentage = round(country_rich_percentage.max(), 1)

    # 9. المهنة الأكثر شعبية للذين يتقاضون >50K في الهند (India)
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
    