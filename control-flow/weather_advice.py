weather_ai = input("What's the weather like today? (sunny/rainy/cold):").lower()
if weather_ai == 'sunny':
    print("Wear a t-shirt and sunglasses.")
elif weather_ai == 'rainy':
    print("Don't forget your umbrella and a raincoat.")
elif weather_ai == 'cold':
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")

