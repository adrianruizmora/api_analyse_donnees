import unittest
from app import app


class TestApi(unittest.TestCase):
    # On crée une test client

    def setUp(self):
        self.app = app.test_client()

    # On test la requete '/'

    def test_hello_world(self):
        rv = self.app.get('/')
        assert rv.status == '200 OK'
        error = self.app.get('/foo')
        self.assertEqual(error.status, '404 NOT FOUND')

    # On test la requete '/latest_by_country/France'

    def test_by_country(self):
        rv = self.app.get('/latest_by_country/France')
        assert rv.status == '200 OK'
        error = self.app.get('/latest_by_country/foo')
        self.assertEqual(error.status, '404 NOT FOUND')

    # On test la requete '/average_by_year/1975'

    def test_average_for_year(self):
        rv = self.app.get('/average_by_year/1975')
        assert rv.status == '200 OK'
        error = self.app.get('/average_by_year/foo')
        self.assertEqual(error.status, '404 NOT FOUND')

    # On test la requete '/per_capita/Albania'

    def test_per_capita(self):
        rv = self.app.get('/per_capita/Albania')
        assert rv.status == '200 OK'
        error = self.app.get('/per_capita/foo')
        self.assertEqual(error.status, '404 NOT FOUND')


if __name__ == '__main__':
    unittest.main()