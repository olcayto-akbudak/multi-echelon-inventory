"""Çok Kademeli Stok ve Kapasite.

Problem: Mağaza replenishment taleplerini sınırlı merkez kapasitesi ve yoldaki stokla birlikte değerlendirmek.
Method: Merkez/depo, lead time, stok pozisyonu, adil tahsis
Invariant: Günlük deterministik zaman adımı ve seeded sentetik talep; satış kaybı backorder olmaz.
Boundary: Talep korelasyonu, kapasite kesintileri ve optimizasyon dışarıdan eklenmelidir."""
import random

def simulate(config):
    days = config.get('days', 90)
    stores = config['stores']
    lead = config.get('lead_time', 4)
    if days < 1 or lead < 1 or (not stores) or any((s['base_stock'] < 0 for s in stores)):
        raise ValueError('configuration')
    rng = random.Random(config.get('seed', 42))
    central = config.get('central_stock', 100)
    capacity = config.get('daily_capacity', 20)
    if type(capacity) is not int or central < 0 or capacity < 1 or (config.get('daily_supply', 12) < 0) or any((type(s['max_demand']) is not int or s['max_demand'] < 0 for s in stores)):
        raise ValueError('capacity')
    stock = {s['id']: s['initial'] for s in stores}
    pipeline = []
    metrics = {s['id']: {'demand': 0, 'sold': 0, 'lost': 0, 'holding_units': 0} for s in stores}
    log = []
    if len(stock) != len(stores) or any((v < 0 for v in stock.values())):
        raise ValueError('stores')
    for day in range(days):
        arrived = [p for p in pipeline if p['due'] == day]
        for p in arrived:
            stock[p['store']] += p['quantity']
        pipeline = [p for p in pipeline if p['due'] > day]
        central += config.get('daily_supply', 12)
        requests = []
        for s in stores:
            demand = rng.randrange(s['max_demand'] + 1)
            sold = min(stock[s['id']], demand)
            stock[s['id']] -= sold
            m = metrics[s['id']]
            m['demand'] += demand
            m['sold'] += sold
            m['lost'] += demand - sold
            m['holding_units'] += stock[s['id']]
            position = stock[s['id']] + sum((p['quantity'] for p in pipeline if p['store'] == s['id']))
            requests.append([s['id'], max(0, s['base_stock'] - position)])
        budget = min(capacity, central)
        shipped = 0
        allocations = {s['id']: 0 for s in stores}
        while budget and any((q for _, q in requests)):
            for request in requests:
                if request[1] and budget:
                    request[1] -= 1
                    budget -= 1
                    shipped += 1
                    allocations[request[0]] += 1
        central -= shipped
        for key, q in allocations.items():
            if q:
                pipeline.append({'store': key, 'due': day + lead, 'quantity': q})
        log.append({'day': day, 'central': central, 'shipped': shipped, 'backlog': sum((q for _, q in requests))})
    for m in metrics.values():
        m['fill_rate'] = m['sold'] / max(1, m['demand'])
    return {'stores': metrics, 'central_final': central, 'in_transit': pipeline, 'daily': log}

def run(config):
    return simulate(config)

import argparse, json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Run reproducible synthetic project scenario')
    parser.add_argument('command', choices=['demo'])
    parser.add_argument('--input', default='scenario.json')
    parser.add_argument('--output', default='report.json')
    args = parser.parse_args()
    report = run(json.loads(Path(args.input).read_text(encoding='utf-8')))
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')
    print(f'Report: {target}')
if __name__ == '__main__':
    main()
