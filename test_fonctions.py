import unittest
import fonctions as f
import test_values as tv


class TestCreateJson(unittest.TestCase):

    def test_filename(self):
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

    def test_return_type(self):
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
    
    def test_country(self):
        countries = tv.countries()
        for country in range(len(countries)):
            self.assertIsNotNone(f.get_latest_by_country(countries[country]))


class TestAverageForYear(unittest.TestCase):
    
    def test_year(self):
        self.assertIsInstance(f.average_for_year(''),float)
        self.assertIsInstance(f.average_for_year('_'),float)
        self.assertIsInstance(f.average_for_year(2017), float)
        self.assertIsInstance(f.average_for_year('2017'), float)
        self.assertIsInstance(f.average_for_year('2024'), float)
        info = tv.info_latest_by_country()
        info_keys = list(info.keys())
        for i in range(len(info)):
            self.assertIsNotNone(f.get_latest_by_country(info_keys[i]))

if __name__ == '__main__':
    unittest.main()
