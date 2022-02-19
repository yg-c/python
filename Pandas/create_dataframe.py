# Create a DataFrame
import pandas as pd

""" Lists """

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)


""" CSV """
df = pd.read_csv('data.csv')

""" JSON """

df = pd.read_json('data.json')


calendar_data = [{'ColA': 'V1', 'ColB': 'Ete', 'from': date(2019, 5, 1), 'to': date(2019, 10, 31)},
                 {'ColA': 'V1', 'ColB': 'Hiver', 'from': date(2019, 11, 1), 'to': date(2020, 4, 30)},
                 {'ColA': 'V2', 'ColB': 'Ete', 'from': date(2020, 5, 1), 'to': date(2020, 10, 31)},
                 {'ColA': 'V2', 'ColB': 'Hiver', 'from': date(2020, 11, 1), 'to': date(2021, 4, 30)},
                 {'ColA': 'V3', 'ColB': 'Ete', 'from': date(2021, 5, 1), 'to': date(2021, 10, 31)},
                 {'ColA': 'V3', 'ColB': 'Hiver', 'from': date(2021, 11, 1), 'to': date(2022, 4, 30)}]
calendar_matrix = pd.json_normalize(calendar_data)