from math import ceil

wine_yard_area = int(input())
grapes_produced_per_sq_meter = float(input())
wine_required_for_sale_in_litres = int(input())
workers_quantity = int(input())

GRAPES_FOR_WINE_PRODUCTION = 0.4
GRAPES_REQUIRED_TO_PRODUCE_LTR_WINE = 2.5  # kilos

grapes_produced = wine_yard_area * grapes_produced_per_sq_meter
wine_produced = grapes_produced * GRAPES_FOR_WINE_PRODUCTION / GRAPES_REQUIRED_TO_PRODUCE_LTR_WINE

wine_per_worker = 0
if wine_produced < wine_required_for_sale_in_litres:
    wine_in_deficit = wine_required_for_sale_in_litres - wine_produced
    print(f"It will be a tough winter! More {int(wine_in_deficit)} liters wine needed.")
else:  # elif wine_produced >= wine_required_for_sale_in_litres:
    wine_in_surplus = wine_produced - wine_required_for_sale_in_litres
    wine_per_worker = wine_in_surplus / workers_quantity
    print(f"Good harvest this year! Total wine: {int(wine_produced)} liters.")
    print(f"{ceil(wine_in_surplus)} liters left -> {ceil(wine_per_worker)} liters per person.")
