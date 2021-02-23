import unittest
import fonctions as f
import test_values as tv

class TestCreateJson(unittest.TestCase):
    pass
    

class TestGetLatestByCountry(unittest.TestCase):

    def test_return_type(self):
        self.assertIsNone(f.get_latest_by_country('foo'))
        self.assertIsNone(f.get_latest_by_country('123'))
        self.assertIsNone(f.get_latest_by_country(456))
        self.assertIsNone(f.get_latest_by_country(''))
        self.assertIsNone(f.get_latest_by_country('.'))
        self.assertIsNone(f.get_latest_by_country('/'))
        self.assertIsNotNone(f.get_latest_by_country('Albania'))
        self.assertIsNotNone(f.get_latest_by_country('Japan'))
        self.assertIsNotNone(f.get_latest_by_country('Kazakhstan'))
    
    def test_country(self):
        info = tv.info_latest_by_country()
        info_keys = list(info.keys())
        info_values = list(info.values())
        for i in range(len(info)):
            self.assertEqual(f.get_latest_by_country(info_keys[i]), info_values[i])

    def test_upper(self):
        info = tv.info_latest_by_country()
        info_keys = list(info.keys())
        info_values = list(info.values())
        for i in range(len(info)):
            self.assertEqual(f.get_latest_by_country(info_keys[i].upper()), info_values[i])

    def test_lower(self):
        info = tv.info_latest_by_country()
        info_keys = list(info.keys())
        info_values = list(info.values())
        for i in range(len(info)):
            self.assertEqual(f.get_latest_by_country(info_keys[i].lower()), info_values[i])
    

if __name__ == '__main__':
    unittest.main()