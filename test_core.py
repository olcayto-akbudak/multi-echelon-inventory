import unittest, tempfile, json, sqlite3, copy
from pathlib import Path
import app as c

class CoreTests(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'test.sqlite'
        self.config = json.loads((Path(__file__).resolve().parent / 'scenario.json').read_text(encoding='utf-8'))

    def test_capacity(self):
        self.assertTrue(all((x['shipped'] <= self.config['daily_capacity'] for x in c.run(self.config)['daily'])))

    def test_nonnegative(self):
        self.assertTrue(all((x['central'] >= 0 for x in c.run(self.config)['daily'])))

    def test_demand_conservation(self):
        for x in c.run(self.config)['stores'].values():
            self.assertEqual(x['demand'], x['sold'] + x['lost'])

    def test_seed(self):
        self.assertEqual(c.run(self.config), c.run(self.config))

    def test_lead(self):
        cfg = copy.deepcopy(self.config)
        cfg['lead_time'] = 0
        with self.assertRaises(ValueError):
            c.run(cfg)

    def test_duplicate_store(self):
        cfg = copy.deepcopy(self.config)
        cfg['stores'] *= 2
        with self.assertRaises(ValueError):
            c.run(cfg)

    def test_negative_supply(self):
        cfg = copy.deepcopy(self.config)
        cfg['daily_supply'] = -1
        with self.assertRaises(ValueError):
            c.run(cfg)

    def test_supply_conservation(self):
        r = c.run(self.config)
        self.assertEqual(r['central_final'] + sum((x['shipped'] for x in r['daily'])), self.config['central_stock'] + self.config['days'] * self.config['daily_supply'])
if __name__ == '__main__':
    unittest.main()
