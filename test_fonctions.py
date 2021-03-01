import unittest
import fonctions as f
import values as v


class TestCreateJson(unittest.TestCase):

    def test_parametres(self):
        self.assertEqual(f.create_json(""), 1)
        self.assertEqual(f.create_json("",""), 1)
        self.assertEqual(f.create_json("foo"), 1)
        self.assertEqual(f.create_json("/"), 1)
        self.assertEqual(f.create_json(123), 1)
        self.assertEqual(f.create_json(123.1), 1)
        self.assertEqual(f.create_json('estimates.json'),1)
        self.assertEqual(f.create_json('estimates.csv', '/'), 1)
        self.assertEqual(f.create_json('estimates.csv','estimates'), 1)
        self.assertEqual(f.create_json('estimates.csv','estimates.csv'), 1)
        self.assertEqual(f.create_json('estimates.csv','estimates.txt'), 1)
        self.assertEqual(f.create_json('estimates.csv','estimates.json'), 0)
        self.assertEqual(f.create_json('estimates.csv'), 0)
        self.assertEqual(f.create_json(), 0)
        

class TestGetLatestByCountry(unittest.TestCase):

    def test_parametres(self):
        self.assertIsNone(f.get_latest_by_country('foo'))
        self.assertIsNone(f.get_latest_by_country('123'))
        self.assertIsNone(f.get_latest_by_country(456))
        self.assertIsNone(f.get_latest_by_country(456.1))
        self.assertIsNone(f.get_latest_by_country(''))
        self.assertIsNone(f.get_latest_by_country('.'))
        self.assertIsNone(f.get_latest_by_country('/'))
        self.assertIsNone(f.get_latest_by_country('Albania', 'estimates.csv'))
        self.assertIsNone(f.get_latest_by_country('estimates.csv', 'Albania'))
        self.assertIsNotNone(f.get_latest_by_country('Albania', 'estimates.json'))
    
    def test_return_value(self):
        countries = v.countries
        values = v.values_latest
        for i in range(len(countries)):
            self.assertEqual(f.get_latest_by_country(countries[i]), values[i])


class TestAverageForYear(unittest.TestCase):
    
    def test_parametres(self):
        self.assertIsInstance(f.average_for_year(''), int)
        self.assertIsInstance(f.average_for_year('_'), int)
        self.assertIsInstance(f.average_for_year(2017), int)
        self.assertIsInstance(f.average_for_year('2017'), float)
        self.assertIsInstance(f.average_for_year('2024'), int)

    def test_return_value(self):
        years = v.years
        values = v.values_years
        for i in range(len(years)):
            self.assertEqual(f.average_for_year(years[i]), values[i])

class TestPerCapita(unittest.TestCase):

    def test_parametres(self):
        self.assertEqual(f.get_per_capita('France', ''), False)
        self.assertEqual(f.get_per_capita('France', '/'), False)
        self.assertEqual(f.get_per_capita('France', '.'), False)
        self.assertEqual(f.get_per_capita('France', '_'), False)
        self.assertEqual(f.get_per_capita('France', '2015'), False)
        self.assertEqual(f.get_per_capita('France', 2015), False)
        self.assertEqual(f.get_per_capita('foo', '2017'), False)
        self.assertEqual(f.get_per_capita(2015, '2017'), False)
        self.assertEqual(f.get_per_capita('2015', '2017'), False)
        self.assertIsInstance(f.get_per_capita('France', 'estimates.json'), dict)

    def test_return_value(self):
        countries = v.countries
        values = v.values_capita
        for i in range(len(countries)):
            self.assertEqual(f.get_per_capita(countries[i]), values[i])
        

if __name__ == '__main__':
    unittest.main()