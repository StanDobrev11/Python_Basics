fat_cals_per_gr = 9
protein_cals_per_gr = 4
carbs_cals_pre_gr = 4

fat_percent = int(input())
protein_percent = int(input())
carbs_percent = int(input())
ttl_calories = int(input())
water_content_percent = int(input())

grams_fat = (ttl_calories * fat_percent / 100) / fat_cals_per_gr
grams_protein = (ttl_calories * protein_percent / 100) / protein_cals_per_gr
grams_carbs = (ttl_calories * carbs_percent / 100) / carbs_cals_pre_gr

food_weight = grams_fat + grams_carbs + grams_protein
calories_per_gram_food_inc_water = ttl_calories / food_weight

final_calories_wout_water = calories_per_gram_food_inc_water * (100 - water_content_percent) / 100

print(f"{final_calories_wout_water :.4f}")

